import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_cell_border(cell, **kwargs):
    """
    kwargs: top, bottom, left, right
    values: dict(val='single', sz='4', color='000000', space='0')
    """
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = OxmlElement('w:tcBorders')
    for border_name in ['top', 'left', 'bottom', 'right']:
        if border_name in kwargs:
            b_el = OxmlElement(f'w:{border_name}')
            for k, v in kwargs[border_name].items():
                b_el.set(qn(f'w:{k}'), str(v))
            tcBorders.append(b_el)
    tcPr.append(tcBorders)

doc = docx.Document()

# Margins 2cm around (0.79 inch)
for section in doc.sections:
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

# ----------------- HEADER TABLE -----------------
tbl_header = doc.add_table(rows=1, cols=2)
tbl_header.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_header.autofit = False

c_left = tbl_header.rows[0].cells[0]
c_right = tbl_header.rows[0].cells[1]
c_left.width = Inches(3.6)
c_right.width = Inches(3.4)

set_cell_margins(c_left, top=60, bottom=60, left=60, right=60)
set_cell_margins(c_right, top=60, bottom=60, left=60, right=60)

# Left Header
p_hl = c_left.paragraphs[0]
p_hl.alignment = WD_ALIGN_PARAGRAPH.CENTER
r1 = p_hl.add_run('SỞ GIÁO DỤC VÀ ĐÀO TẠO\nTHÀNH PHỐ HỒ CHÍ MINH\n')
r1.font.name = 'Times New Roman'
r1.font.size = Pt(10.5)
r1.bold = True

r2 = p_hl.add_run('HỘI THI THIẾT KẾ CHỦ ĐỀ STEM/STEAM,\nCHỦ ĐỀ DẠY HỌC SỐ NĂM HỌC 2026 - 2027')
r2.font.name = 'Times New Roman'
r2.font.size = Pt(10)
r2.bold = True
r2.font.color.rgb = RGBColor(0, 32, 96)

# Right Header
p_hr = c_right.paragraphs[0]
p_hr.alignment = WD_ALIGN_PARAGRAPH.CENTER
r3 = p_hr.add_run('CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM\n')
r3.font.name = 'Times New Roman'
r3.font.size = Pt(10.5)
r3.bold = True

r4 = p_hr.add_run('Độc lập - Tự do - Hạnh phúc\n')
r4.font.name = 'Times New Roman'
r4.font.size = Pt(10.5)
r4.bold = True

r5 = p_hr.add_run('-----------------------')
r5.font.name = 'Times New Roman'
r5.font.size = Pt(9.5)

# Remove borders for header table
for cell in (c_left, c_right):
    set_cell_border(cell, 
                    top={'val': 'none'}, 
                    bottom={'val': 'none'}, 
                    left={'val': 'none'}, 
                    right={'val': 'none'})

# ----------------- MAIN TITLE -----------------
p_title = doc.add_paragraph()
p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_title.paragraph_format.space_before = Pt(12)
p_title.paragraph_format.space_after = Pt(2)

rt1 = p_title.add_run('PHẦN 1: PHẦN TỔNG QUAN\n')
rt1.font.name = 'Times New Roman'
rt1.font.size = Pt(14)
rt1.bold = True
rt1.font.color.rgb = RGBColor(192, 0, 0)

rt2 = p_title.add_run('THÔNG TIN THÍ SINH DỰ THI VÀ BỐI CẢNH THỰC HIỆN CHỦ ĐỀ\n')
rt2.font.name = 'Times New Roman'
rt2.font.size = Pt(13)
rt2.bold = True
rt2.font.color.rgb = RGBColor(0, 32, 96)

rt3 = p_title.add_run('MÔN LỊCH SỬ VÀ ĐỊA LÍ – CẤP TRUNG HỌC CƠ SỞ\n(LỚP 8 – BỘ SÁCH KẾT NỐI TRI THỨC VỚI CUỘC SỐNG)\n')
rt3.font.name = 'Times New Roman'
rt3.font.size = Pt(12)
rt3.bold = True

rt4 = p_title.add_run('(Thực hiện theo Kế hoạch số 12070/KH-SGDĐT ngày 09/11/2026 của Sở GD&ĐT TP. Hồ Chí Minh)')
rt4.font.name = 'Times New Roman'
rt4.font.size = Pt(10.5)
rt4.italic = True

# ----------------- SECTION I: THÔNG TIN GIÁO VIÊN -----------------
p_s1 = doc.add_heading('I. THÔNG TIN GIỚI THIỆU VỀ GIÁO VIÊN VÀ ĐƠN VỊ', level=1)
p_s1.paragraph_format.space_before = Pt(14)
p_s1.paragraph_format.space_after = Pt(6)
for r in p_s1.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 32, 96)

tbl_gv = doc.add_table(rows=7, cols=2)
tbl_gv.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_gv.autofit = False

gv_info = [
    ('Họ và tên giáo viên:', 'NGUYỄN ĐỨC AN'),
    ('Năm sinh / Giới tính:', '1990   |   Giới tính: Nam'),
    ('Bộ môn đăng ký dự thi:', 'Lịch sử và Địa lí (Phân môn Lịch sử 8 - Cấp THCS)'),
    ('Thâm niên công tác:', '10 năm giảng dạy môn Lịch sử THCS'),
    ('Tên đơn vị công tác:', 'Trường Liên cấp TH - THCS Nguyễn Quốc Phú'),
    ('Số điện thoại liên lạc cá nhân:', '0972020819'),
    ('Địa chỉ thư điện tử (Email):', 'anndnqp@tu.sgdbinhduong.edu.vn')
]

for idx, (lbl, val) in enumerate(gv_info):
    row = tbl_gv.rows[idx]
    c1, c2 = row.cells[0], row.cells[1]
    c1.width = Inches(2.3)
    c2.width = Inches(4.7)
    
    set_cell_margins(c1, top=80, bottom=80, left=100, right=100)
    set_cell_margins(c2, top=80, bottom=80, left=100, right=100)
    set_cell_shading(c1, 'F2F2F2')
    
    p1 = c1.paragraphs[0]
    p1.paragraph_format.space_before = Pt(2)
    p1.paragraph_format.space_after = Pt(2)
    r = p1.add_run(lbl)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    r.bold = True
    
    p2 = c2.paragraphs[0]
    p2.paragraph_format.space_before = Pt(2)
    p2.paragraph_format.space_after = Pt(2)
    r = p2.add_run(val)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(11)
    if '[' in val:
        r.font.color.rgb = RGBColor(192, 0, 0)
        r.bold = True

    border_spec = {'val': 'single', 'sz': '4', 'color': 'D3D3D3', 'space': '0'}
    set_cell_border(c1, top=border_spec, bottom=border_spec, left=border_spec, right=border_spec)
    set_cell_border(c2, top=border_spec, bottom=border_spec, left=border_spec, right=border_spec)

# ----------------- SECTION II: TÊN VÀ TÓM LƯỢC NỘI DUNG -----------------
p_s2 = doc.add_heading('II. TÊN VÀ TÓM LƯỢC NỘI DUNG CHỦ ĐỀ DỰ THI', level=1)
p_s2.paragraph_format.space_before = Pt(14)
p_s2.paragraph_format.space_after = Pt(6)
for r in p_s2.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 32, 96)

# Table Box for Topic Title
tbl_topic = doc.add_table(rows=1, cols=1)
tbl_topic.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_topic.autofit = False
c_topic = tbl_topic.rows[0].cells[0]
c_topic.width = Inches(7.0)
set_cell_margins(c_topic, top=100, bottom=100, left=150, right=150)
set_cell_shading(c_topic, 'FFF8DC') # light golden cornsilk
border_gold = {'val': 'single', 'sz': '12', 'color': 'D4AF37', 'space': '0'}
set_cell_border(c_topic, top=border_gold, bottom=border_gold, left=border_gold, right=border_gold)

p_tbox = c_topic.paragraphs[0]
p_tbox.alignment = WD_ALIGN_PARAGRAPH.CENTER
rtb1 = p_tbox.add_run('TÊN CHỦ ĐỀ DẠY HỌC SỐ:\n')
rtb1.font.name = 'Times New Roman'
rtb1.font.size = Pt(12)
rtb1.bold = True
rtb1.font.color.rgb = RGBColor(192, 0, 0)

rtb2 = p_tbox.add_run('HÀO KHÍ TÂY SƠN (1771 – 1789) – TÁI HIỆN NHỮNG THẮNG LỢI TIÊU BIỂU TRÊN KHÔNG GIAN SỐ\n')
rtb2.font.name = 'Times New Roman'
rtb2.font.size = Pt(13.5)
rtb2.bold = True
rtb2.font.color.rgb = RGBColor(0, 32, 96)

rtb3 = p_tbox.add_run('(Xây dựng Bảo tàng số tương tác, Thu âm Podcast sử học, Giải mã mật mã tư liệu SGK và Hệ thống Đánh giá đồng đẳng trực tuyến thời gian thực phục vụ học sinh Lớp 8)')
rtb3.font.name = 'Times New Roman'
rtb3.font.size = Pt(11)
rtb3.italic = True

# 1. Đơn vị môn học
p_ii1 = doc.add_paragraph()
p_ii1.paragraph_format.space_before = Pt(8)
p_ii1.paragraph_format.space_after = Pt(4)
r = p_ii1.add_run('1. Đơn vị môn học đăng ký dự thi: ')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r2 = p_ii1.add_run('Môn Lịch sử và Địa lí – Phân môn Lịch sử 8 (Bộ sách Kết nối tri thức với cuộc sống – Chương 3, Bài 8: Phong trào Tây Sơn).')
r2.font.name = 'Times New Roman'
r2.font.size = Pt(11)

# 2. Tình huống thực tiễn
p_ii2 = doc.add_paragraph()
p_ii2.paragraph_format.space_before = Pt(4)
p_ii2.paragraph_format.space_after = Pt(4)
r = p_ii2.add_run('2. Tình huống thực tiễn và vấn đề đặt ra:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)

p_ii2_text = (
    'Phong trào Tây Sơn (1771 – 1789) là một trong những giai đoạn lịch sử hào hùng, bi tráng và đạt đến đỉnh cao chói lọi '
    'của nghệ thuật quân sự dân tộc Việt Nam với hàng loạt chiến công vĩ đại: lật đổ chúa Nguyễn ở Đàng Trong, lật đổ chúa Trịnh – vua Lê ở Bắc Hà, '
    'đánh tan 5 vạn quân Xiêm tại Rạch Gầm – Xoài Mút và đỉnh cao là cuộc hành quân thần tốc đại phá 29 vạn quân Mãn Thanh mùa xuân Kỷ Dậu 1789.\n\n'
    'Tuy nhiên, trong thực tiễn dạy học lịch sử hiện nay tại các trường THCS, việc giảng dạy chủ đề này thường gặp phải các hạn chế lớn:\n'
    '• Diễn biến lịch sử kéo dài gần 2 thập kỷ với không gian tác chiến trải dài khắp ba miền đất nước khiến học sinh khó ghi nhớ các mốc sự kiện, dễ nhầm lẫn diễn biến và cảm thấy quá tải.\n'
    '• Phương pháp dạy học truyền thống nặng về thuyết giảng một chiều và trình chiếu slide tĩnh, thiếu tính trực quan sử thi và chưa tạo được xúc cảm hào hùng trước thiên tài quân sự của người anh hùng áo vải Quang Trung – Nguyễn Huệ.\n'
    '• Thiếu không gian để học sinh được trực tiếp đóng vai trò là "Nhà nghiên cứu sử học số nhí", tự tay tra cứu tư liệu chuẩn SGK, phân tích lược đồ chiến dịch và chia sẻ tiếng nói cảm thụ lịch sử của thế hệ trẻ.\n\n'
    '👉 Câu hỏi dẫn dắt dự án (Driving Question):\n'
    '“Làm thế nào để học sinh Lớp 8 không chỉ học thuộc lòng các mốc niên đại khô khan, mà có thể hóa thân thành các \'Nhà sử học số nhí\', '
    'tự lực khai thác tư liệu SGK Kết nối tri thức, thu âm bản tin Podcast lịch sử hào hùng, giải mã mật mã trận đánh '
    'và cùng nhau kiến tạo Phòng Triển Lãm Di Sản Số tương tác đa nền tảng thông qua mã QR và công nghệ đồng bộ thời gian thực?”'
)
r_text = p_ii2.add_run(p_ii2_text)
r_text.font.name = 'Times New Roman'
r_text.font.size = Pt(11)

# 3. Tóm lược nội dung chủ đề
p_ii3 = doc.add_paragraph()
p_ii3.paragraph_format.space_before = Pt(6)
p_ii3.paragraph_format.space_after = Pt(4)
r = p_ii3.add_run('3. Tóm lược nội dung chủ đề:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)

p_ii3_text = (
    'Chủ đề được thiết kế trong thời lượng chuẩn 02 tiết học trên lớp (90 phút) kết hợp không gian số hóa trải nghiệm đa chiều, '
    'bám sát mục tiêu cần đạt của Bài 8 – SGK Lịch sử 8 (Bộ sách Kết nối tri thức với cuộc sống). Học sinh hoạt động theo 4 nhóm chuyên trách '
    'độc lập, tương ứng với 4 trạm chiến công lịch sử vĩ đại nhất của phong trào Tây Sơn:\n'
    '• Nhóm 1: Tiếng sấm khởi nghĩa Tây Sơn thượng đạo và quá trình lật đổ chính quyền chúa Nguyễn ở Đàng Trong (1771 – 1777).\n'
    '• Nhóm 2: Nghệ thuật thủy chiến mai phục tài tình – Trận Rạch Gầm – Xoài Mút đại phá 5 vạn quân Xiêm (1785).\n'
    '• Nhóm 3: Tiến quân ra Bắc Hà lật đổ hai tập đoàn phong kiến Trịnh – Nguyễn (1786 – 1788), xóa bỏ chia cắt Đàng Trong – Đàng Ngoài hơn hai thế kỉ, đặt nền tảng thống nhất quốc gia.\n'
    '• Nhóm 4: Bản hùng ca mùa xuân Kỷ Dậu 1789 – Thiên tài quân sự Quang Trung đại phá 29 vạn quân Mãn Thanh tại Ngọc Hồi – Đống Đa.\n\n'
    'Tiến trình học tập diễn ra hoàn toàn trên nền tảng học liệu số chuyên biệt (https://lichsu-eight.vercel.app/):\n'
    '• Tầng 1 (Tự chủ nghiên cứu): Từng nhóm tiếp cận nguồn tư liệu chuẩn SGK trang 35-39, phân tích lược đồ trận đánh số hóa độ phân giải cao, trả lời câu hỏi định hướng tư duy và giải mật mã lịch sử độc quyền.\n'
    '• Tầng 2 (Sáng tạo nội dung số): Học sinh sử dụng bộ công cụ Micro-Podcast tích hợp trực tiếp trên trình duyệt để thu âm giọng kể thuyết minh lịch sử truyền cảm (thời lượng 1 - 2 phút) tái hiện thời khắc chiến thắng oanh liệt.\n'
    '• Tầng 3 (Kiểm duyệt sư phạm chuẩn mực): Sản phẩm của học sinh được chuyển về "Trung tâm kiểm duyệt của Giáo viên" để người dạy thẩm định tính chính xác sử liệu, ghi chú phản hồi trước khi bấm duyệt xuất bản.\n'
    '• Tầng 4 (Xuất bản & Tương tác số): Sau khi duyệt, hệ thống tự động sinh 4 Poster Infographic nghệ thuật Trống đồng Đông Sơn và mã QR tương tác, hiển thị trực tiếp trên Dòng thời gian sử học của bảo tàng số.'
)
r_text = p_ii3.add_run(p_ii3_text)
r_text.font.name = 'Times New Roman'
r_text.font.size = Pt(11)

# 4. Điểm mới, độc đáo
p_ii4 = doc.add_paragraph()
p_ii4.paragraph_format.space_before = Pt(6)
p_ii4.paragraph_format.space_after = Pt(4)
r = p_ii4.add_run('4. Điểm mới, độc đáo và tính đột phá phù hợp lứa tuổi học sinh Lớp 8:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)

points_unique = [
    ('Rạp chiếu 3D sử thi nổi & Lời hiệu triệu Quang Trung (Cinematic Theater): ',
     'Website mở đầu bằng 10 tác phẩm tranh điện ảnh 3D 4K chuyển cảnh luân phiên 60fps trên nền ca khúc hào hùng "Hào khí Việt Nam" và giọng đọc tái hiện Lời hiểu dụ bất hủ của vua Quang Trung năm 1788 ("Đánh cho để dài tóc / Đánh cho để đen răng..."), đánh thức mạnh mẽ lòng yêu nước và niềm tự hào dân tộc ngay từ giây đầu tiên.'),
    
    ('Tính năng "Góc phóng viên - Thu âm Podcast lịch sử" độc quyền trên Web: ',
     'Học sinh không chỉ viết bài tóm tắt thông thường mà được trực tiếp thu âm giọng kể podcast qua micro ngay trên giao diện web (không cần cài app ngoài, có đồng hồ đếm giây và hiệu ứng sóng âm). Giúp các em rèn luyện kỹ năng diễn đạt hùng hồn, truyền cảm và vượt qua rào cản thụ động.'),

    ('Trung tâm kiểm duyệt sư phạm của Giáo viên (Teacher Moderation Dashboard): ',
     'Khắc phục triệt để lỗ hổng của các công cụ web tự do: bài làm của học sinh phải qua quy trình kiểm duyệt nội dung của giáo viên mới được cấp phép xuất bản lên phòng triển lãm chung, bảo đảm tính tôn nghiêm và chính xác tuyệt đối của tri thức lịch sử.'),

    ('Đánh giá đồng đẳng thời gian thực qua mã QR (Realtime Cloud Sync & Peer Review): ',
     'Mỗi poster di sản được gắn mã QR chuẩn ISO/IEC 18004. Ở Tiết 2, cả lớp dùng điện thoại quét mã QR nhóm bạn để nghe podcast, bấm "❤️ Thả tim" và gửi bình luận nhận xét trực tiếp hiển thị ngay trên màn hình máy chiếu lớp học; kết hợp giáo viên đánh giá toàn diện theo bảng kiểm Rubric.'),

    ('Đóng góp vào Kho học liệu số ngành GD&ĐT TP.HCM: ',
     'Dự án được xây dựng dưới dạng ứng dụng Web chuẩn Single Page Application (SPA), vận hành độc lập tại https://lichsu-eight.vercel.app/, tương thích 100% với màn hình tương tác, máy chiếu, máy tính bảng và điện thoại di động, đồng thời hỗ trợ chế độ ngoại tuyến (offline) phòng khi mất mạng trường.')
]

for title, desc in points_unique:
    p_pt = doc.add_paragraph()
    p_pt.paragraph_format.space_before = Pt(2)
    p_pt.paragraph_format.space_after = Pt(2)
    p_pt.paragraph_format.left_indent = Inches(0.2)
    r_pt1 = p_pt.add_run('• ' + title)
    r_pt1.bold = True
    r_pt1.font.name = 'Times New Roman'
    r_pt1.font.size = Pt(11)
    r_pt2 = p_pt.add_run(desc)
    r_pt2.font.name = 'Times New Roman'
    r_pt2.font.size = Pt(11)

# ----------------- SECTION III: VỊ TRÍ KIẾN THỨC VÀ TÍCH HỢP LIÊN MÔN -----------------
p_s3 = doc.add_heading('III. VỊ TRÍ KIẾN THỨC VÀ TÍCH HỢP LIÊN MÔN STEM / DẠY HỌC SỐ CHO LỚP 8', level=1)
p_s3.paragraph_format.space_before = Pt(14)
p_s3.paragraph_format.space_after = Pt(6)
for r in p_s3.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 32, 96)

p_iii1 = doc.add_paragraph()
p_iii1.paragraph_format.space_before = Pt(4)
p_iii1.paragraph_format.space_after = Pt(4)
r = p_iii1.add_run('1. Vị trí trong Chương trình GDPT 2018 môn Lịch sử và Địa lí 8:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r_text = p_iii1.add_run(
    '• Trọng tâm chương trình: Thuộc Chương 3: Đại Việt thời Lê sơ và thời Mạc, các cuộc chiến tranh Nam - Bắc triều, Trịnh - Nguyễn; '
    'Bài 8: Phong trào Tây Sơn (Thời lượng phân phối: 02 tiết).\n'
    '• Kiến thức cốt lõi: Bối cảnh bùng nổ khởi nghĩa Tây Sơn; nguyên nhân, diễn biến và ý nghĩa của các thắng lợi tiêu biểu (lật đổ chúa Nguyễn ở Đàng Trong 1771-1777, '
    'chiến thắng Rạch Gầm - Xoài Mút 1785, lật đổ tập đoàn phong kiến Trịnh - Lê 1786-1788, đại phá quân Thanh 1789); '
    'nghệ thuật tác chiến quân sự và vai trò của Quang Trung - Nguyễn Huệ trong sự nghiệp thống nhất và bảo vệ Tổ quốc.'
)
r_text.font.name = 'Times New Roman'
r_text.font.size = Pt(11)

p_iii2 = doc.add_paragraph()
p_iii2.paragraph_format.space_before = Pt(4)
p_iii2.paragraph_format.space_after = Pt(4)
r = p_iii2.add_run('2. Xác định Kiến thức và Kỹ năng nền (Prerequisites):\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r_text = p_iii2.add_run(
    '• Môn Lịch sử: Kiến thức về tình hình chia cắt Đàng Trong - Đàng Ngoài thế kỉ XVII - XVIII, sự suy yếu của chế độ phong kiến và đời sống cùng cực của nhân dân; '
    'kỹ năng khai thác kênh hình, đọc hiểu tư liệu văn bản và khai thác lược đồ chiến dịch quân sự.\n'
    '• Môn Ngữ văn: Kỹ năng tóm tắt văn bản thông tin, kỹ năng viết bản tin ngắn, kỹ năng kể chuyện truyền cảm (kỹ thuật đọc diễn cảm văn bản sử thi hùng tráng).\n'
    '• Môn Tin học / Công nghệ số: Kỹ năng sử dụng trình duyệt web, tìm kiếm thông tin có chọn lọc, thao tác thu âm giọng nói trên thiết bị số, quét mã QR trên điện thoại thông minh.\n'
    '• Môn Âm nhạc / Mỹ thuật: Cảm thụ âm hưởng hào hùng của âm nhạc truyền thống và bố cục hoa văn Trống đồng Đông Sơn.'
)
r_text.font.name = 'Times New Roman'
r_text.font.size = Pt(11)

p_iii3 = doc.add_paragraph()
p_iii3.paragraph_format.space_before = Pt(4)
p_iii3.paragraph_format.space_after = Pt(4)
r = p_iii3.add_run('3. Ma trận tích hợp liên môn và phương pháp Dạy học số:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)

tbl_stem = doc.add_table(rows=6, cols=2)
tbl_stem.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_stem.autofit = False

stem_data = [
    ('Khoa học (Science - Lịch sử):', 'Khám phá sự thật lịch sử qua tư liệu SGK Kết nối tri thức; phân tích bản chất chiến thuật quân sự (thủy chiến nghi binh, chia 5 cánh quân thần tốc); giải mã các câu hỏi mật mã sử liệu.'),
    ('Công nghệ (Technology):', 'Khai thác ứng dụng Web SPA hiện đại, công nghệ thu âm Web Audio API không cần cài đặt, công nghệ mã QR tương tác ISO/IEC 18004, hệ thống máy chủ đám mây đồng bộ lượt thả tim và bình luận theo thời gian thực.'),
    ('Kỹ thuật (Engineering):', 'Quy trình 4 bước thiết kế sản phẩm số: Khám phá tư liệu → Viết kịch bản bản tin → Thu âm podcast đạt chuẩn âm thanh trong trẻo → Xuất bản poster infographic triển lãm.'),
    ('Nghệ thuật (Art):', 'Thiết kế Poster triển lãm độc bản lấy cảm hứng từ hoa văn Trống đồng Đông Sơn hoàng kim, cờ lệnh Tây Sơn viền lửa; nghệ thuật diễn đọc podcast truyền cảm lay động lòng người.'),
    ('Toán học (Mathematics):', 'Quản trị thời gian biểu 2 tiết học (90 phút); kiểm soát dung lượng kịch bản (150 - 250 từ) và thời lượng podcast (60 - 120 giây); thống kê định lượng lượt tương tác thả tim và điểm số đánh giá chéo theo thang Rubric 10.')
]

for idx, (lbl, val) in enumerate(stem_data):
    row = tbl_stem.rows[idx]
    c1, c2 = row.cells[0], row.cells[1]
    c1.width = Inches(2.2)
    c2.width = Inches(4.8)
    set_cell_margins(c1, top=70, bottom=70, left=90, right=90)
    set_cell_margins(c2, top=70, bottom=70, left=90, right=90)
    set_cell_shading(c1, 'F9F9F9')
    
    p1 = c1.paragraphs[0]
    p1.paragraph_format.space_before = Pt(2)
    p1.paragraph_format.space_after = Pt(2)
    r = p1.add_run(lbl)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10.5)
    r.bold = True
    
    p2 = c2.paragraphs[0]
    p2.paragraph_format.space_before = Pt(2)
    p2.paragraph_format.space_after = Pt(2)
    r = p2.add_run(val)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(10.5)

    border_spec = {'val': 'single', 'sz': '4', 'color': 'D3D3D3', 'space': '0'}
    set_cell_border(c1, top=border_spec, bottom=border_spec, left=border_spec, right=border_spec)
    set_cell_border(c2, top=border_spec, bottom=border_spec, left=border_spec, right=border_spec)

# ----------------- SECTION IV: PHẨM CHẤT VÀ NĂNG LỰC -----------------
p_s4 = doc.add_heading('IV. PHẨM CHẤT VÀ NĂNG LỰC HỌC SINH ĐẠT ĐƯỢC (THEO CT GDPT 2018)', level=1)
p_s4.paragraph_format.space_before = Pt(14)
p_s4.paragraph_format.space_after = Pt(6)
for r in p_s4.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 32, 96)

p_iv1 = doc.add_paragraph()
p_iv1.paragraph_format.space_before = Pt(4)
p_iv1.paragraph_format.space_after = Pt(2)
r = p_iv1.add_run('1. Năng lực đặc thù – Năng lực Lịch sử Lớp 8:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r_text = p_iv1.add_run(
    '• Tìm hiểu lịch sử: Biết khai thác và sử dụng các nguồn tư liệu lịch sử đa phương tiện (tư liệu văn bản trích dẫn SGK Kết nối tri thức, trích dẫn Đại Nam thực lục, lược đồ trận đánh số hóa, tranh điện ảnh 3D) để nhận thức sự kiện.\n'
    '• Nhận thức và tư duy lịch sử: Trình bày được nguyên nhân bùng nổ, diễn biến chính của 4 chiến dịch lớn; phân tích được nét độc đáo trong nghệ thuật quân sự của phong trào Tây Sơn; giải thích được nguyên nhân thắng lợi và ý nghĩa lịch sử to lớn của phong trào.\n'
    '• Vận dụng kiến thức, kỹ năng đã học: Bước đầu biết đánh giá công lao vĩ đại của người anh hùng dân tộc Quang Trung - Nguyễn Huệ; liên hệ bài học đoàn kết toàn dân và bảo vệ độc lập, chủ quyền lãnh thổ trong bối cảnh hiện nay.'
)
r_text.font.name = 'Times New Roman'
r_text.font.size = Pt(11)

p_iv2 = doc.add_paragraph()
p_iv2.paragraph_format.space_before = Pt(4)
p_iv2.paragraph_format.space_after = Pt(2)
r = p_iv2.add_run('2. Năng lực chung:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r_text = p_iv2.add_run(
    '• Tự chủ và tự học: Tự giác nghiên cứu nguồn học liệu số tích hợp, chủ động phân công vai trò trong nhóm, tự lực viết kịch bản và thu âm podcast nhiều lần để đạt chất lượng tốt nhất.\n'
    '• Giao tiếp và hợp tác: Biết lắng nghe, tôn trọng ý kiến đồng đội; phối hợp nhịp nhàng giữa thành viên thu âm, thành viên nhập dữ liệu và báo cáo viên; tự tin thuyết trình trước lớp bằng Chế độ Cinema Presentation.\n'
    '• Giải quyết vấn đề và sáng tạo: Vận dụng tư duy logic để giải mã "Mật mã lịch sử" của nhóm; biết ứng dụng công nghệ số để biến kiến thức lịch sử khô khan thành sản phẩm truyền thông số hấp dẫn.'
)
r_text.font.name = 'Times New Roman'
r_text.font.size = Pt(11)

p_iv3 = doc.add_paragraph()
p_iv3.paragraph_format.space_before = Pt(4)
p_iv3.paragraph_format.space_after = Pt(2)
r = p_iv3.add_run('3. Năng lực số (Digital Competence):\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r_text = p_iv3.add_run(
    '• Khai thác thành thạo nền tảng bảo tàng số tương tác, làm chủ tính năng ghi âm trình duyệt, thao tác nộp bài số hóa lên cổng kiểm duyệt của giáo viên; '
    'sử dụng smartphone quét mã QR tương tác văn minh, đóng góp nhận xét và bình chọn có trách nhiệm trên môi trường internet.'
)
r_text.font.name = 'Times New Roman'
r_text.font.size = Pt(11)

p_iv4 = doc.add_paragraph()
p_iv4.paragraph_format.space_before = Pt(4)
p_iv4.paragraph_format.space_after = Pt(2)
r = p_iv4.add_run('4. Phẩm chất chủ yếu:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r_text = p_iv4.add_run(
    '• Yêu nước: Bồi đắp sâu sắc lòng yêu nước, niềm tự hào vô bờ bến về truyền thống chống giặc ngoại xâm quật cường của dân tộc và ý chí độc lập tự chủ bất diệt.\n'
    '• Trách nhiệm: Nâng cao ý thức trân trọng, gìn giữ và lan tỏa các giá trị di sản văn hóa - lịch sử dân tộc trong kỷ nguyên chuyển đổi số.\n'
    '• Chăm chỉ và Trung thực: Kiên trì tra cứu sử liệu chính thống, tôn trọng tính khách quan của sự thật lịch sử và công bằng khi đánh giá chéo nhóm bạn.'
)
r_text.font.name = 'Times New Roman'
r_text.font.size = Pt(11)

# ----------------- SECTION V: THỜI LƯỢNG VÀ KHÔNG GIAN -----------------
p_s5 = doc.add_heading('V. THỜI LƯỢNG VÀ KHÔNG GIAN THỰC HIỆN', level=1)
p_s5.paragraph_format.space_before = Pt(14)
p_s5.paragraph_format.space_after = Pt(6)
for r in p_s5.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 32, 96)

p_v1 = doc.add_paragraph()
p_v1.paragraph_format.space_before = Pt(4)
p_v1.paragraph_format.space_after = Pt(4)
r = p_v1.add_run('1. Thời lượng thực hiện: ')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r2 = p_v1.add_run('Đúng chuẩn quy định 02 tiết học trên lớp (90 phút), kết hợp linh hoạt mô hình lớp học đảo ngược (Flipped Classroom) và nền tảng số hóa:')
r2.font.name = 'Times New Roman'
r2.font.size = Pt(11)

# Table 4 Stages
tbl_stages = doc.add_table(rows=5, cols=3)
tbl_stages.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_stages.autofit = False

col_widths = [Inches(1.8), Inches(4.0), Inches(1.2)]
stages_data = [
    ('Giai đoạn thực hiện', 'Nội dung hoạt động trọng tâm', 'Thời lượng'),
    ('Giai đoạn 1\n(Trước Tiết 1 – Ngoài lớp)', 
     'Học sinh truy cập đường link nền tảng web https://lichsu-eight.vercel.app/ để xem trước 10 đại cảnh điện ảnh 3D và nghe Lời hiệu triệu Quang Trung; đọc trước Bài 8 trong SGK Kết nối tri thức.', 
     'Giao trước 2 – 3 ngày'),
    ('Giai đoạn 2\n(Tiết 1 – Trên lớp học)', 
     '• Khởi động (7 phút): Trực tiếp cảm nhận khí thế hào hùng qua rạp chiếu điện ảnh 3D và Lời hiệu triệu Quang Trung.\n'
     '• Khám phá & Làm việc nhóm (35 phút): 4 nhóm tiến vào 4 không gian làm việc số riêng biệt; đọc tư liệu SGK, khai thác lược đồ số, viết bản tin tóm tắt diễn biến & phân tích nghệ thuật quân sự; thu âm Podcast lịch sử trực tiếp trên web; giải Mật mã lịch sử và nộp bài lên Giáo viên kiểm duyệt.\n'
     '• Giáo viên phê duyệt bài trực tiếp trên Teacher Moderation Dashboard để xuất bản lên Triển lãm.\n'
     '• Tổng kết tiết 1 (3 phút): Nhận xét tinh thần làm việc, dặn dò chuẩn bị Tiết 2.', 
     '45 phút\n(Tiết 1)'),
    ('Giai đoạn 3\n(Giữa 2 tiết – Ngoài lớp)', 
     'Đại diện người báo cáo của 4 nhóm chuẩn bị bài nói thuyết trình trước lớp; cả lớp chuẩn bị điện thoại thông minh/máy tính bảng phục vụ hoạt động quét mã QR trải nghiệm.', 
     '1 – 2 ngày giữa hai tiết'),
    ('Giai đoạn 4\n(Tiết 2 – Trên lớp học)', 
     '• Báo cáo thuyết trình (24 phút – 6 phút/nhóm): Mở phòng Triển lãm Poster Di sản, bật Chế độ Cinema Presentation; lần lượt 4 nhóm lên bảng thuyết trình trước toàn trường/lớp.\n'
     '• Trải nghiệm & Đánh giá đồng đẳng qua QR Code (14 phút): Cả lớp dùng điện thoại quét mã QR của nhóm bạn để nghe podcast, bấm "❤️ Thả tim" và gửi nhận xét trực tiếp; Giáo viên chấm điểm theo Rubric.\n'
     '• Tổng kết & Vận dụng (7 phút): GV chuẩn hóa kiến thức, vinh danh nhóm xuất sắc và liên hệ bài học trách nhiệm bảo vệ chủ quyền biên cương, biển đảo.', 
     '45 phút\n(Tiết 2)')
]

for row_idx, row_content in enumerate(stages_data):
    row = tbl_stages.rows[row_idx]
    is_hdr = (row_idx == 0)
    for col_idx, text in enumerate(row_content):
        cell = row.cells[col_idx]
        cell.width = col_widths[col_idx]
        set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
        
        if is_hdr:
            set_cell_shading(cell, '002060')
        elif row_idx % 2 == 1:
            set_cell_shading(cell, 'F9F9F9')
        else:
            set_cell_shading(cell, 'FFFFFF')
            
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        r = p.add_run(text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        if is_hdr:
            r.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif col_idx != 1:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        border_spec = {'val': 'single', 'sz': '4', 'color': 'D3D3D3', 'space': '0'}
        set_cell_border(cell, top=border_spec, bottom=border_spec, left=border_spec, right=border_spec)

p_v2 = doc.add_paragraph()
p_v2.paragraph_format.space_before = Pt(8)
p_v2.paragraph_format.space_after = Pt(4)
r = p_v2.add_run('2. Không gian thực hiện:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(11)

spaces_info = [
    ('Trong lớp học: ', 'Bố trí 4 cụm bàn học tập tương ứng 4 trạm chiến dịch lịch sử; bục giảng trang bị máy tính kết nối máy chiếu/màn hình tương tác thông minh hiển thị Chế độ Cinema Presentation và mã QR phóng to.'),
    ('Không gian số tương tác: ', 'Website Cổng học liệu số Hào Khí Tây Sơn (https://lichsu-eight.vercel.app/) vận hành mượt mà trên nền tảng đám mây Vercel và máy chủ dự phòng GitHub Pages; tích hợp đầy đủ công nghệ thu âm micro, sinh mã QR, đồng bộ thả tim và kiểm duyệt sư phạm.'),
    ('Ngoài lớp học: ', 'Góc học tập cá nhân tại nhà có kết nối mạng internet hoặc tải trước gói web offline để tìm hiểu sâu hơn về các di tích và nhân vật lịch sử thời Tây Sơn.')
]
for title, desc in spaces_info:
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(2)
    p_sp.paragraph_format.space_after = Pt(2)
    p_sp.paragraph_format.left_indent = Inches(0.2)
    r1 = p_sp.add_run('• ' + title)
    r1.bold = True
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(11)
    r2 = p_sp.add_run(desc)
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(11)

# ----------------- SECTION VI: MỤC TIÊU CẦN ĐẠT ĐƯỢC -----------------
p_s6 = doc.add_heading('VI. MỤC TIÊU CẦN ĐẠT ĐƯỢC SAU CHỦ ĐỀ', level=1)
p_s6.paragraph_format.space_before = Pt(14)
p_s6.paragraph_format.space_after = Pt(6)
for r in p_s6.runs:
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12.5)
    r.bold = True
    r.font.color.rgb = RGBColor(0, 32, 96)

goals = [
    ('1. Kiến thức Lịch sử chuẩn xác: ', '100% học sinh khối 8 nắm vững và tự tin trình bày được nguyên nhân, diễn biến cốt lõi, nét đặc sắc trong nghệ thuật tác chiến của 4 chiến công lớn của phong trào Tây Sơn; hiểu sâu sắc tài năng quân sự và công lao thống nhất giang sơn của vua Quang Trung.'),
    ('2. Sản phẩm học tập số độc bản: ', 'Mỗi nhóm học sinh hoàn thành 01 Bộ sản phẩm số chuẩn mực bao gồm: 01 Phiếu học tập số phân tích sử liệu, 01 Bản tin tóm tắt, 01 File thu âm Podcast lịch sử truyền cảm, 01 Mã QR tương tác và 01 Poster Infographic nghệ thuật Trống đồng Đông Sơn được Giáo viên phê duyệt chính thức.'),
    ('3. Kỹ năng Số & Tương tác văn minh: ', 'Học sinh làm chủ các công cụ học tập số hiện đại, tự tin thuyết trình trước đám đông, biết sử dụng smartphone quét mã QR tương tác học tập tích cực, thả tim và đóng góp ý kiến nhận xét chân thành cho bạn bè.'),
    ('4. Giá trị lan tỏa và Đóng góp học liệu: ', 'Toàn bộ sản phẩm được tích hợp hoàn chỉnh trên nền tảng Website https://lichsu-eight.vercel.app/, sẵn sàng kết nối, chia sẻ và đóng góp vào Hệ thống quản lý học liệu số dùng chung của ngành Giáo dục và Đào tạo TP. Hồ Chí Minh.')
]

for title, desc in goals:
    p_gl = doc.add_paragraph()
    p_gl.paragraph_format.space_before = Pt(3)
    p_gl.paragraph_format.space_after = Pt(3)
    r1 = p_gl.add_run(title)
    r1.bold = True
    r1.font.name = 'Times New Roman'
    r1.font.size = Pt(11)
    r2 = p_gl.add_run(desc)
    r2.font.name = 'Times New Roman'
    r2.font.size = Pt(11)

# ----------------- SIGNATURE TABLE -----------------
doc.add_paragraph().paragraph_format.space_before = Pt(16)

tbl_sign = doc.add_table(rows=1, cols=2)
tbl_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
tbl_sign.autofit = False

c_sleft = tbl_sign.rows[0].cells[0]
c_sright = tbl_sign.rows[0].cells[1]
c_sleft.width = Inches(3.5)
c_sright.width = Inches(3.5)

set_cell_margins(c_sleft, top=60, bottom=60, left=60, right=60)
set_cell_margins(c_sright, top=60, bottom=60, left=60, right=60)

# Left Sign
p_sl = c_sleft.paragraphs[0]
p_sl.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p_sl.add_run('XÁC NHẬN CỦA ĐƠN VỊ TRƯỜNG THCS\n')
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r.bold = True
r = p_sl.add_run('(Ký tên, đóng dấu)\n\n\n\n\n\n')
r.font.name = 'Times New Roman'
r.font.size = Pt(10)
r.italic = True

# Right Sign
p_sr = c_sright.paragraphs[0]
p_sr.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p_sr.add_run('TP. Hồ Chí Minh, ngày       tháng 11 năm 2026\n')
r.font.name = 'Times New Roman'
r.font.size = Pt(10.5)
r.italic = True
r = p_sr.add_run('GIÁO VIÊN XÂY DỰNG CHỦ ĐỀ\n')
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r.bold = True
r = p_sr.add_run('(Ký và ghi rõ họ tên)\n\n\n\n\n\n')
r.font.name = 'Times New Roman'
r.font.size = Pt(10)
r.italic = True
r = p_sr.add_run('Nguyễn Đức An')
r.font.name = 'Times New Roman'
r.font.size = Pt(11)
r.bold = True

# Remove borders for signature table
for cell in (c_sleft, c_sright):
    set_cell_border(cell, 
                    top={'val': 'none'}, 
                    bottom={'val': 'none'}, 
                    left={'val': 'none'}, 
                    right={'val': 'none'})

output_path = r'docs/ho_so_hoi_thi/Folder_1_Phan_tong_quan/Lichsu_THCS_Nguyen-Duc-An_STEM_P1.docx'
doc.save(output_path)
print('Document generated successfully at:', output_path)
