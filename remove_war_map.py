# -*- coding: utf-8 -*-
"""
Remove the 'Sa Bàn Tác Chiến Động' section from index.html
"""

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

start_marker = '<!-- ========================================== -->\n            <!-- SA BÀN CHIẾN LƯỢC: 5 CHẶNG HÀNH QUÂN THẦN TỐC (1788 - 1789) -->'
end_marker = '<!-- 4 Mission Cards for the 4 Groups -->'

start_pos = html.find(start_marker)
end_pos = html.find(end_marker)

if start_pos != -1 and end_pos != -1:
    html = html[:start_pos] + html[end_pos:]
    print("Successfully removed 'Sa Bàn Tác Chiến Động' HTML block!")
else:
    print(f"Markers not found: start_pos={start_pos}, end_pos={end_pos}")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated successfully!")
