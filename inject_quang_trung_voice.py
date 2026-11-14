# -*- coding: utf-8 -*-
"""
Inject the epic Quang Trung imperial proclamation audio into index.html
"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update quote button in hero banner
old_btn = '''                                <button type="button" onclick="playQuangTrungSpeech()" class="cursor-pointer px-2.5 py-1 rounded-lg bg-amber-500/20 hover:bg-amber-500/40 text-amber-300 text-xs font-bold border border-amber-500/40 transition flex items-center gap-1.5 not-italic font-sans">
                                    <i class="fa-solid fa-volume-high text-amber-400"></i> Nghe Giọng Đọc
                                </button>'''

new_btn = '''                                <audio id="audio-quang-trung-speech" src="images/giong_quang_trung.mp3?v=1" preload="auto"></audio>
                                <button type="button" onclick="playQuangTrungSpeech()" id="btn-quang-trung-speech" class="cursor-pointer px-3 py-1.5 rounded-xl bg-gradient-to-r from-red-950 via-red-900 to-amber-950 hover:from-red-900 hover:to-amber-900 text-yellow-300 text-xs font-bold border border-amber-500/60 shadow-lg shadow-red-950/60 transition flex items-center gap-2 not-italic font-sans">
                                    <i class="fa-solid fa-volume-high text-amber-400" id="icon-quang-trung-speech"></i>
                                    <span id="lbl-quang-trung-speech">Nghe Vua Quang Trung Hiệu Triệu</span>
                                </button>'''

if old_btn in html:
    html = html.replace(old_btn, new_btn, 1)
    print("Replaced quote button with audio player element!")
else:
    print("Warning: old_btn not found with exact match, using regex...")
    import re
    html = re.sub(r'<button[^>]*onclick="playQuangTrungSpeech\(\)"[^>]*>[\s\S]*?Nghe Giọng Đọc[\s\S]*?</button>', new_btn, html, count=1)

# 2. Update playQuangTrungSpeech function in JavaScript
import re
old_func_pattern = r'function playQuangTrungSpeech\(\) \{[\s\S]*?window\.speechSynthesis\.speak\(utterance\);[\s\S]*?\} else \{[\s\S]*?alert\([^\)]+\);[\s\S]*?\}[\s\S]*?\}'

new_func = '''let isQuangTrungSpeechPlaying = false;
        function playQuangTrungSpeech() {
            const audio = document.getElementById('audio-quang-trung-speech') || new Audio('images/giong_quang_trung.mp3');
            const quoteBox = document.getElementById('hero-quote-container');
            const btn = document.getElementById('btn-quang-trung-speech');
            const icon = document.getElementById('icon-quang-trung-speech');
            const lbl = document.getElementById('lbl-quang-trung-speech');

            // Bấm lại để dừng nếu đang phát
            if (isQuangTrungSpeechPlaying) {
                audio.pause();
                audio.currentTime = 0;
                isQuangTrungSpeechPlaying = false;
                if (quoteBox) quoteBox.classList.remove('ring-4', 'ring-amber-400', 'shadow-[0_0_35px_rgba(245,158,11,0.7)]');
                if (icon) icon.className = "fa-solid fa-volume-high text-amber-400";
                if (lbl) lbl.textContent = "Nghe Vua Quang Trung Hiệu Triệu";
                return;
            }

            // Trống lệnh mở màn dồn dập
            playBassDrum(125, 0.5, 0.9);

            audio.currentTime = 0;
            audio.volume = 1.0;
            audio.play().then(() => {
                isQuangTrungSpeechPlaying = true;
                if (quoteBox) quoteBox.classList.add('ring-4', 'ring-amber-400', 'shadow-[0_0_35px_rgba(245,158,11,0.7)]');
                if (icon) icon.className = "fa-solid fa-volume-high text-yellow-300 animate-bounce";
                if (lbl) lbl.textContent = "Đang Hiệu Triệu Ba Quân...";

                audio.onended = () => {
                    isQuangTrungSpeechPlaying = false;
                    if (quoteBox) quoteBox.classList.remove('ring-4', 'ring-amber-400', 'shadow-[0_0_35px_rgba(245,158,11,0.7)]');
                    if (icon) icon.className = "fa-solid fa-volume-high text-amber-400";
                    if (lbl) lbl.textContent = "Nghe Lại Lời Dụ";
                    playChiengDong(380, 2.0, 0.4);
                };
            }).catch(err => {
                console.log("Audio play error:", err);
            });
        }'''

html = re.sub(old_func_pattern, new_func, html, count=1)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: index.html updated with epic Quang Trung voice!")
