# -*- coding: utf-8 -*-
"""
Replace the two buttons [ Trống Trận ] and [ Lời Dụ Quang Trung ] in the top bar
with a dedicated music player button for the song 'Hào Khí Việt Nam'.
"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace the 2 buttons in top bar
target_old = '''            <!-- Nút bật/tắt Trống trận Tây Sơn -->
            <button type="button" onclick="toggleBattleDrums()" id="btn-battle-drums" class="cursor-pointer px-2.5 py-1 rounded-lg bg-stone-900/90 hover:bg-red-950 border border-amber-500/40 text-amber-300 font-bold text-[11px] flex items-center gap-1.5 transition shadow" title="Bật/Tắt tiếng trống trận Tây Sơn hào hùng">
                <i class="fa-solid fa-drum text-amber-400"></i>
                <span>Trống Trận:</span>
                <span id="battle-drums-status" class="text-amber-200 font-bold">Bật</span>
            </button>
            <!-- Nút nghe Lời hiểu dụ -->
            <button type="button" onclick="playQuangTrungSpeech()" class="cursor-pointer px-2.5 py-1 rounded-lg bg-stone-900/90 hover:bg-amber-950 border border-amber-500/40 text-amber-300 font-bold text-[11px] flex items-center gap-1.5 transition shadow" title="Nghe diễn đọc hào hùng Lời Hiểu Dụ của Hoàng đế Quang Trung">
                <i class="fa-solid fa-bullhorn text-amber-400"></i>
                <span class="hidden sm:inline">Lời Dụ Quang Trung</span>
            </button>'''

replacement_new = '''            <!-- Ca khúc chủ đề: HÀO KHÍ VIỆT NAM -->
            <audio id="audio-hao-khi" src="images/hao_khi_viet_nam.mp3" preload="auto" loop></audio>
            <button type="button" onclick="toggleHaoKhiMusic()" id="btn-hao-khi" class="cursor-pointer px-3 py-1 rounded-lg bg-gradient-to-r from-red-950 via-stone-900 to-amber-950 hover:from-red-900 hover:to-amber-900 border border-amber-500/60 text-amber-200 font-bold text-[11px] flex items-center gap-2 transition shadow-lg shadow-red-950/40" title="Bật / Dừng ca khúc hào hùng: Hào Khí Việt Nam">
                <i class="fa-solid fa-music text-amber-400" id="icon-hao-khi"></i>
                <span>Nhạc: <strong class="text-yellow-300">Hào Khí Việt Nam</strong></span>
                <span id="status-hao-khi" class="text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40">Bật</span>
            </button>'''

if target_old in html:
    html = html.replace(target_old, replacement_new, 1)
    print("Top bar buttons replaced successfully!")
else:
    print("Warning: target_old not found in html")

# Add toggleHaoKhiMusic function into the JS script block
js_haokhi = '''
        // --- CA KHÚC CHỦ ĐỀ: HÀO KHÍ VIỆT NAM ---
        let isHaoKhiMusicPlaying = false;
        function toggleHaoKhiMusic() {
            const audio = document.getElementById('audio-hao-khi');
            const btn = document.getElementById('btn-hao-khi');
            const status = document.getElementById('status-hao-khi');
            const icon = document.getElementById('icon-hao-khi');

            if (!audio) return;

            if (isHaoKhiMusicPlaying) {
                audio.pause();
                isHaoKhiMusicPlaying = false;
                if (btn) {
                    btn.classList.remove('ring-2', 'ring-amber-400', 'bg-red-950');
                }
                if (status) {
                    status.textContent = 'Bật';
                    status.className = 'text-[10px] px-1.5 py-0.5 rounded bg-amber-500/20 text-amber-300 border border-amber-500/40 font-bold';
                }
                if (icon) {
                    icon.className = 'fa-solid fa-music text-amber-400';
                }
            } else {
                audio.volume = 0.65;
                audio.play().then(() => {
                    isHaoKhiMusicPlaying = true;
                    if (btn) {
                        btn.classList.add('ring-2', 'ring-amber-400', 'bg-red-950');
                    }
                    if (status) {
                        status.textContent = 'Đang phát ♪';
                        status.className = 'text-[10px] px-1.5 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold';
                    }
                    if (icon) {
                        icon.className = 'fa-solid fa-compact-disc fa-spin text-yellow-300';
                    }
                }).catch(err => {
                    console.log("Audio play error:", err);
                    alert("Trình duyệt yêu cầu tương tác người dùng để phát nhạc. Vui lòng bấm lại nút!");
                });
            }
        }
'''

last_script_pos = html.rfind('</script>')
if last_script_pos != -1:
    html = html[:last_script_pos] + js_haokhi + '\n    ' + html[last_script_pos:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: index.html updated with Hao Khi Viet Nam music!")
