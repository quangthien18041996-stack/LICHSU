// Vercel Serverless Function: In-memory & resilient interaction sync
// Endpoint: /api/interactions

let syncState = {
    likes: {
        "1": 35,
        "2": 28,
        "3": 25,
        "4": 40
    },
    reviews: {
        "1": [
            { reviewer: "Tổ 2 - Trải nghiệm", score: 10, comment: "Poster Tổ 1 thiết kế bố cục rất cổ kính, hào khí khởi nghĩa Lam Sơn - Tây Sơn rất rõ nét!", time: "08:15" }
        ],
        "2": [
            { reviewer: "Tổ 4 - Đánh giá chéo", score: 10, comment: "Chiến thuật nghi binh rạch Gầm Xoài Mút mô tả cực kỳ sinh động và thuyết phục!", time: "08:20" }
        ],
        "3": [
            { reviewer: "Tổ 1 - Bình chọn", score: 10, comment: "Lời bình lật đổ chúa Trịnh giải phóng Bắc Hà rất hào hùng!", time: "08:22" }
        ],
        "4": [
            { reviewer: "Tổ 3 - Cảm nhận", score: 10, comment: "Trận Ngọc Hồi Đống Đa thần tốc đại phá 29 vạn quân Thanh quá tự hào!", time: "08:25" }
        ]
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
