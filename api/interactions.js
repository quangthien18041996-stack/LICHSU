// Vercel Serverless Function: In-memory & resilient interaction sync
// Endpoint: /api/interactions

let syncState = {
    likes: {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0
    },
    reviews: {
        "1": [],
        "2": [],
        "3": [],
        "4": []
    },
    lastUpdated: Date.now()
};

export default function handler(req, res) {
    // CORS headers
    res.setHeader('Access-Control-Allow-Credentials', 'true');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
    res.setHeader('Access-Control-Allow-Headers', 'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version');
    res.setHeader('Cache-Control', 'no-store, no-cache, must-revalidate, proxy-revalidate');

    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }

    if (req.method === 'POST') {
        try {
            const body = typeof req.body === 'string' ? JSON.parse(req.body) : (req.body || {});
            const { type, groupId, data, currentLikes, fullState } = body;

            // Xử lý Reset sạch toàn bộ dữ liệu trên Cloud
            if (type === 'reset') {
                syncState = {
                    likes: { "1": 0, "2": 0, "3": 0, "4": 0 },
                    reviews: { "1": [], "2": [], "3": [], "4": [] },
                    isReset: true,
                    lastUpdated: Date.now()
                };
                return res.status(200).json({ success: true, data: syncState });
            }

            // Xử lý Nạp bản mẫu Demo
            if (type === 'load_sample') {
                syncState = {
                    likes: { "1": 18, "2": 22, "3": 19, "4": 35 },
                    reviews: {
                        "1": [{ reviewer: "Nhóm 2 (Trần Hoàng)", score: 10, comment: "Lược đồ căn cứ Tây Sơn phân tích rất chi tiết, giọng đọc truyền cảm và hào hùng!", time: "08:15" }],
                        "2": [{ reviewer: "Nhóm 1 (Lê Quốc Dũng)", score: 10, comment: "Bản đồ phục kích Rạch Gầm vẽ rất sinh động, giọng đọc thuyết minh nghe rất hào hứng!", time: "08:18" }],
                        "3": [{ reviewer: "Nhóm 4 (Lê Lan Anh)", score: 10, comment: "Bài phân tích chiến thuật tạm hòa hoãn với quân Trịnh rất sâu sắc, xứng đáng 10 điểm!", time: "08:20" }],
                        "4": [{ reviewer: "Nhóm 3 (Nguyễn Mai Chi)", score: 10, comment: "Lời hiệu triệu Quang Trung quá hào hùng, poster đẹp xuất sắc!", time: "08:25" }]
                    },
                    lastUpdated: Date.now()
                };
                return res.status(200).json({ success: true, data: syncState });
            }

            // Merge full state if provided (e.g. from local client sync)
            if (fullState) {
                if (fullState.likes) {
                    for (let i = 1; i <= 4; i++) {
                        const sLikes = Number(fullState.likes[String(i)] || fullState.likes[i] || 0);
                        if (sLikes > Number(syncState.likes[String(i)] || 0)) {
                            syncState.likes[String(i)] = sLikes;
                        }
                    }
                }
                if (fullState.reviews) {
                    for (let i = 1; i <= 4; i++) {
                        const sRevs = fullState.reviews[String(i)] || fullState.reviews[i] || [];
                        if (Array.isArray(sRevs) && sRevs.length > 0) {
                            if (!syncState.reviews[String(i)]) syncState.reviews[String(i)] = [];
                            const existing = new Set(syncState.reviews[String(i)].map(r => (r.comment || '').trim()));
                            sRevs.forEach(r => {
                                if (r.comment && !existing.has(r.comment.trim())) {
                                    syncState.reviews[String(i)].unshift(r);
                                    existing.add(r.comment.trim());
                                }
                            });
                        }
                    }
                }
            }

            if (type === 'like' && groupId) {
                const g = String(groupId);
                const cur = Number(syncState.likes[g] || 0);
                syncState.likes[g] = cur + 1;
            } else if (type === 'comment' && groupId && data) {
                const g = String(groupId);
                if (!syncState.reviews[g]) syncState.reviews[g] = [];
                const exists = syncState.reviews[g].some(r => (r.comment || '').trim() === (data.comment || '').trim());
                if (!exists) {
                    syncState.reviews[g].unshift(data);
                }
            }

            syncState.lastUpdated = Date.now();
            return res.status(200).json({ success: true, data: syncState });
        } catch (err) {
            return res.status(400).json({ success: false, error: err.message });
        }
    }

    // Default GET: Return current synced interactions
    return res.status(200).json({
        success: true,
        data: syncState
    });
}
