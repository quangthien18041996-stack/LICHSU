# -*- coding: utf-8 -*-
"""
Remove 'Đấu Trường 60s' button and modal from index.html
"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove from desktop navbar
desktop_btn = '''                <button type="button" onclick="openArenaQuizModal()" class="cursor-pointer px-3.5 py-2 rounded-xl bg-gradient-to-r from-red-800 via-amber-700 to-amber-600 hover:from-red-700 hover:to-amber-500 text-yellow-100 font-bold text-xs flex items-center gap-2 shadow-lg shadow-amber-900/40 border border-yellow-400/50 transition transform hover:scale-105" title="Đấu trường thử tài chiến lược 60 giây">
                    <i class="fa-solid fa-bolt text-yellow-300 animate-pulse"></i> Đấu Trường 60s
                </button>'''

if desktop_btn in html:
    html = html.replace(desktop_btn, '', 1)
    print("Removed desktop navbar button!")
else:
    print("Desktop button not found with exact match, searching fuzzy...")
    import re
    html = re.sub(r'<button[^>]*onclick="openArenaQuizModal\(\)"[^>]*>[\s\S]*?Đấu Trường 60s[\s\S]*?</button>\s*', '', html, count=1)

# 2. Remove from mobile navbar
mobile_btn = '<button type="button" onclick="openArenaQuizModal()" class="cursor-pointer mobile-nav-btn px-3 py-1.5 rounded-lg whitespace-nowrap font-bold text-yellow-300 bg-red-950/80 border border-amber-500/40"><i class="fa-solid fa-bolt mr-1"></i>Đấu Trường 60s</button>'
if mobile_btn in html:
    html = html.replace(mobile_btn, '', 1)
    print("Removed mobile navbar button!")

# 3. Remove the entire Modal 1 HTML block
start_marker = '<!-- MODAL 1: ĐẤU TRƯỜNG TRÍ TUỆ QUANG TRUNG (60s QUIZ) -->'
end_marker = '<!-- ========================================== -->\n    <!-- MODAL 2: PHÒNG TRÌNH CHIẾU BÁO CÁO (CINEMA PRESENTATION SUITE) -->'

# Find the header before start_marker
sep = '<!-- ========================================== -->\n    ' + start_marker
start_pos = html.find(sep)
if start_pos == -1:
    start_pos = html.find(start_marker)

end_pos = html.find(end_marker)

if start_pos != -1 and end_pos != -1:
    html = html[:start_pos] + html[end_pos:]
    print("Removed Modal 1 HTML block successfully!")
else:
    print(f"Warning: Modal 1 markers not found: start={start_pos}, end={end_pos}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated successfully!")
