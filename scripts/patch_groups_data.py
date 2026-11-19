import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Score Cards initial HTML
for i in range(1, 5):
    html = re.sub(
        rf'<div class="text-3xl font-black text-amber-300 font-mono" id="score-val-{i}">[\d\.]+ / 10</div>',
        f'<div class="text-3xl font-black text-amber-300 font-mono" id="score-val-{i}">-- / 10</div>',
        html
    )
    html = re.sub(
        rf'<strong class="text-stone-200" id="reviews-count-{i}">\d+</strong>',
        f'<strong class="text-stone-200" id="reviews-count-{i}">0</strong>',
        html
    )
    html = re.sub(
        rf'<span id="likes-count-{i}">\d+</span>',
        f'<span id="likes-count-{i}">0</span>',
        html
    )

# 2. Update GROUPS_DATA block
gd_start = html.find('const GROUPS_DATA = {')
gd_end = html.find('let currentActiveGroup = 1;', gd_start)
gd_block = html[gd_start:gd_end]

# For each group block 1 to 4 in gd_block:
# Replace headline, slogan, time, location, commander, tactics, summary, quangTrungRole, members, audioData, status, teacherFeedback, likes, score, reviews
# Replace headline: "..." with headline: ""
gd_block = re.sub(r'headline:\s*".*?",', 'headline: "",', gd_block)
gd_block = re.sub(r'slogan:\s*".*?",', 'slogan: "",', gd_block)
gd_block = re.sub(r'time:\s*".*?",', 'time: "",', gd_block)
gd_block = re.sub(r'location:\s*".*?",', 'location: "",', gd_block)
gd_block = re.sub(r'commander:\s*".*?",', 'commander: "",', gd_block)
gd_block = re.sub(r'tactics:\s*".*?",', 'tactics: "",', gd_block)
gd_block = re.sub(r'summary:\s*".*?",', 'summary: "",', gd_block)
gd_block = re.sub(r'quangTrungRole:\s*".*?",', 'quangTrungRole: "",', gd_block)
gd_block = re.sub(r'members:\s*".*?",', 'members: "",', gd_block)
gd_block = re.sub(r'audioData:\s*".*?",', 'audioData: null,', gd_block)
gd_block = re.sub(r'status:\s*".*?",', 'status: "draft",', gd_block)
gd_block = re.sub(r'teacherFeedback:\s*".*?",', 'teacherFeedback: "",', gd_block)
gd_block = re.sub(r'likes:\s*\d+,', 'likes: 0,', gd_block)
gd_block = re.sub(r'score:\s*[\d\.]+,', 'score: 0,', gd_block)
gd_block = re.sub(r'reviews:\s*\[[\s\S]*?\],', 'reviews: [],', gd_block)

html = html[:gd_start] + gd_block + html[gd_end:]

# 3. Update clearCurrentGroupData()
old_clear = """        function clearCurrentGroupData() {
            const g = GROUPS_DATA[currentActiveGroup];
            if (confirm(`Bạn có chắc muốn xóa trắng biểu mẫu của ${g.name} để học sinh thực hành từ đầu không?`)) {
                g.headline = "";
                g.slogan = "";
                g.time = "";
                g.location = "";
                g.commander = "";
                g.tactics = "";
                g.summary = "";
                g.quangTrungRole = "";
                g.members = "";
                g.audioData = null;
                renderAudioPlayer(null);
                renderActiveGroupForm(currentActiveGroup);
                saveGroupData(false);
            }
        }"""

new_clear = """        function clearCurrentGroupData() {
            const g = GROUPS_DATA[currentActiveGroup];
            if (confirm(`Bạn có chắc muốn xóa trắng toàn bộ dữ liệu, điểm số và bài làm của ${g.name} để học sinh thực hành từ đầu không?`)) {
                g.headline = "";
                g.slogan = "";
                g.time = "";
                g.location = "";
                g.commander = "";
                g.tactics = "";
                g.summary = "";
                g.quangTrungRole = "";
                g.members = "";
                g.audioData = null;
                g.status = "draft";
                g.teacherFeedback = "";
                g.score = 0;
                g.likes = 0;
                g.reviews = [];
                
                renderAudioPlayer(null);
                renderActiveGroupForm(currentActiveGroup);
                saveGroupData(false);
                saveToLocalStorage();
                updateTeacherDashboard();
                renderGalleryTimeline();
                generateAllQRCodes();
                
                alert(`✅ Đã xóa trắng toàn bộ dữ liệu và điểm số của ${g.name}! Biểu mẫu hiện đã sạch để học sinh làm bài.`);
            }
        }"""

if old_clear in html:
    html = html.replace(old_clear, new_clear)
    print("Replaced clearCurrentGroupData successfully!")
else:
    print("WARNING: old_clear not found exactly, will check.")

# 4. Update loadSampleForCurrentGroup() and add loadAllSamplesForDemo()
old_sample = """        function loadSampleForCurrentGroup() {
            const sample = SAMPLE_DATA[currentActiveGroup];
            if (sample) {
                const g = GROUPS_DATA[currentActiveGroup];
                g.headline = sample.headline;
                g.slogan = sample.slogan;
                g.time = sample.time;
                g.location = sample.location;
                g.commander = sample.commander;
                g.tactics = sample.tactics;
                g.summary = sample.summary;
                g.quangTrungRole = sample.quangTrungRole;
                g.members = sample.members;
                renderActiveGroupForm(currentActiveGroup);
                saveGroupData(false);
                alert(`Đã nạp nội dung gợi ý mẫu cho ${g.name}!`);
            }
        }"""

new_sample = """        function loadSampleForCurrentGroup() {
            const sample = SAMPLE_DATA[currentActiveGroup];
            if (sample) {
                const g = GROUPS_DATA[currentActiveGroup];
                g.headline = sample.headline;
                g.slogan = sample.slogan;
                g.time = sample.time;
                g.location = sample.location;
                g.commander = sample.commander;
                g.tactics = sample.tactics;
                g.summary = sample.summary;
                g.quangTrungRole = sample.quangTrungRole;
                g.members = sample.members;
                g.audioData = `images/poster_audio_group_${currentActiveGroup}.mp3`;
                g.status = "approved";
                g.teacherFeedback = "Bài làm rất xuất sắc! Sử liệu chuẩn xác, phân tích sâu sắc. Đã phê duyệt và xuất bản Poster.";
                g.score = (9.5 + Math.random() * 0.4).toFixed(1);
                g.likes = Math.floor(15 + Math.random() * 10);
                g.reviews = [
                    { reviewer: "Nhóm bạn đánh giá", score: 10, comment: "Nội dung phân tích rất sắc bén, giọng đọc thuyết minh hào hùng!", time: "08:15" }
                ];
                renderActiveGroupForm(currentActiveGroup);
                renderAudioPlayer(g.audioData);
                saveGroupData(false);
                saveToLocalStorage();
                updateTeacherDashboard();
                renderGalleryTimeline();
                generateAllQRCodes();
                alert(`🎉 Đã nạp đầy đủ nội dung gợi ý mẫu, bản thu âm và điểm số cho ${g.name}!`);
            }
        }

        function loadAllSamplesForDemo() {
            if (confirm("Bạn có muốn nạp dữ liệu mẫu cho CẢ 4 NHÓM để thực hiện bài thuyết trình / demo không?")) {
                for (let i = 1; i <= 4; i++) {
                    const sample = SAMPLE_DATA[i];
                    const g = GROUPS_DATA[i];
                    if (sample && g) {
                        g.headline = sample.headline;
                        g.slogan = sample.slogan;
                        g.time = sample.time;
                        g.location = sample.location;
                        g.commander = sample.commander;
                        g.tactics = sample.tactics;
                        g.summary = sample.summary;
                        g.quangTrungRole = sample.quangTrungRole;
                        g.members = sample.members;
                        g.audioData = `images/poster_audio_group_${i}.mp3`;
                        g.status = "approved";
                        g.teacherFeedback = "Tác phẩm xuất sắc! Đã kiểm duyệt đạt chuẩn.";
                        g.score = (9.6 + (i * 0.1)).toFixed(1);
                        g.likes = 15 + i * 5;
                        g.reviews = [
                            { reviewer: `Nhóm ${i === 1 ? 2 : 1} đánh giá`, score: 10, comment: "Poster rất đẹp, nội dung lịch sử hào hùng!", time: "08:20" }
                        ];
                    }
                }
                saveToLocalStorage();
                renderActiveGroupForm(currentActiveGroup);
                updateTeacherDashboard();
                renderGalleryTimeline();
                generateAllQRCodes();
                
                // Đồng bộ lên cloud nếu có mạng
                try {
                    const endpoint = getCloudSyncEndpoint();
                    fetch(endpoint, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ type: 'load_sample' })
                    }).catch(() => {});
                } catch(e) {}

                alert("🎉 Đã nạp dữ liệu mẫu cho toàn bộ 4 nhóm thành công!");
            }
        }"""

if old_sample in html:
    html = html.replace(old_sample, new_sample)
    print("Replaced loadSampleForCurrentGroup successfully!")
else:
    print("WARNING: old_sample not found exactly.")

# 5. Update resetClassData()
old_reset = """        function resetClassData() {
            if (confirm("Bạn có chắc muốn đặt lại toàn bộ dữ liệu ban đầu (xóa sạch bài làm của các nhóm) để bắt đầu tiết học mới không?")) {
                localStorage.removeItem('TAYSON_DATA_V1');
                localStorage.removeItem('TAYSON_STUDENT_DATA_V3');
                location.reload();
            }
        }"""

new_reset = """        function resetClassData() {
            if (confirm("Bạn có chắc muốn đặt lại toàn bộ dữ liệu ban đầu (xóa sạch bài làm, điểm số, lượt thả tim của TẤT CẢ 4 nhóm) để bắt đầu tiết học mới không?")) {
                for (let i = 1; i <= 4; i++) {
                    const g = GROUPS_DATA[i];
                    if (g) {
                        g.headline = "";
                        g.slogan = "";
                        g.time = "";
                        g.location = "";
                        g.commander = "";
                        g.tactics = "";
                        g.summary = "";
                        g.quangTrungRole = "";
                        g.members = "";
                        g.audioData = null;
                        g.status = "draft";
                        g.teacherFeedback = "";
                        g.score = 0;
                        g.likes = 0;
                        g.reviews = [];
                    }
                }
                
                // Lưu trạng thái trắng sạch vào localStorage để khi F5 / mở lại trang vẫn trắng 100%
                saveToLocalStorage();
                
                // Đồng thời reset trên Cloud Sync (nếu có kết nối)
                try {
                    const endpoint = getCloudSyncEndpoint();
                    fetch(endpoint, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ type: 'reset' })
                    }).catch(() => {});
                } catch(e) {}
                
                renderActiveGroupForm(currentActiveGroup);
                renderAudioPlayer(null);
                updateTeacherDashboard();
                renderGalleryTimeline();
                generateAllQRCodes();
                
                alert("✅ Đã đặt lại toàn bộ dữ liệu thành công! Cả 4 nhóm hiện đã ở trạng thái trắng sạch (điểm số và bài làm đã về 0), sẵn sàng cho học sinh bắt đầu tiết học mới.");
            }
        }"""

if old_reset in html:
    html = html.replace(old_reset, new_reset)
    print("Replaced resetClassData successfully!")
else:
    print("WARNING: old_reset not found exactly.")

# 6. Update score display in updateTeacherDashboard()
old_score_calc = """                    const scoreEl = document.getElementById(`score-val-${i}`);
                    const countEl = document.getElementById(`reviews-count-${i}`);
                    const likesEl = document.getElementById(`likes-count-${i}`);
                    if (scoreEl) scoreEl.textContent = `${g.score || '9.0'} / 10`;"""

new_score_calc = """                    const scoreEl = document.getElementById(`score-val-${i}`);
                    const countEl = document.getElementById(`reviews-count-${i}`);
                    const likesEl = document.getElementById(`likes-count-${i}`);
                    if (scoreEl) {
                        const numScore = Number(g.score);
                        if (g.reviews && g.reviews.length > 0 && numScore > 0) {
                            scoreEl.textContent = `${numScore.toFixed(1)} / 10`;
                        } else {
                            scoreEl.textContent = `-- / 10`;
                        }
                    }"""

if old_score_calc in html:
    html = html.replace(old_score_calc, new_score_calc)
    print("Replaced score display in updateTeacherDashboard successfully!")
else:
    print("WARNING: old_score_calc not found.")

# 7. Add Button "Nạp Bản Mẫu 4 Nhóm" next to "Phê Duyệt Cả 4 Nhóm" in Moderation Header
old_mod_btn = """                        <button onclick="approveAllGroups()" class="px-4 py-2 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold text-xs flex items-center gap-2 shadow-md transition">
                            <i class="fa-solid fa-check-double"></i> Phê Duyệt Cả 4 Nhóm
                        </button>"""

new_mod_btn = """                        <button type="button" onclick="loadAllSamplesForDemo()" class="cursor-pointer px-3.5 py-2 rounded-xl bg-stone-800 hover:bg-amber-950 text-amber-300 font-bold text-xs flex items-center gap-1.5 border border-amber-600/40 shadow transition">
                            <i class="fa-solid fa-wand-magic-sparkles text-amber-400"></i> Nạp Bản Mẫu 4 Nhóm
                        </button>
                        <button onclick="approveAllGroups()" class="px-4 py-2 rounded-xl bg-emerald-700 hover:bg-emerald-600 text-white font-bold text-xs flex items-center gap-2 shadow-md transition">
                            <i class="fa-solid fa-check-double"></i> Phê Duyệt Cả 4 Nhóm
                        </button>"""

if old_mod_btn in html:
    html = html.replace(old_mod_btn, new_mod_btn)
    print("Added Demo Button successfully!")
else:
    print("WARNING: old_mod_btn not found.")

# 8. Update applyCloudData to handle reset state
old_apply = """            // 1. Đồng bộ lượt thả tim (Likes) - chỉ tăng, không bao giờ bị giảm
            if (cloudData.likes) {
                for (let i = 1; i <= 4; i++) {
                    const cloudLikes = cloudData.likes[String(i)] ?? cloudData.likes[i];
                    if (cloudLikes !== undefined && Number(cloudLikes) > (GROUPS_DATA[i].likes || 0)) {
                        GROUPS_DATA[i].likes = Number(cloudLikes);
                        changed = true;
                    }
                }
            }"""

new_apply = """            // Xử lý nếu có lệnh Reset từ Cloud
            if (cloudData.isReset) {
                for (let i = 1; i <= 4; i++) {
                    GROUPS_DATA[i].likes = 0;
                    GROUPS_DATA[i].reviews = [];
                    GROUPS_DATA[i].score = 0;
                }
                saveToLocalStorage();
                updateTeacherDashboard();
                renderGalleryTimeline();
                return;
            }

            // 1. Đồng bộ lượt thả tim (Likes)
            if (cloudData.likes) {
                for (let i = 1; i <= 4; i++) {
                    const cloudLikes = cloudData.likes[String(i)] ?? cloudData.likes[i];
                    if (cloudLikes !== undefined && Number(cloudLikes) !== (GROUPS_DATA[i].likes || 0)) {
                        GROUPS_DATA[i].likes = Number(cloudLikes);
                        changed = true;
                    }
                }
            }"""

if old_apply in html:
    html = html.replace(old_apply, new_apply)
    print("Replaced applyCloudData successfully!")
else:
    print("WARNING: old_apply not found.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html patch completed!")
