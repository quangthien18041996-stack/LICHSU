import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

doc = docx.Document()

# Page setup margins
sections = doc.sections
for s in sections:
    s.top_margin = Inches(0.8)
    s.bottom_margin = Inches(0.8)
    s.left_margin = Inches(0.8)
    s.right_margin = Inches(0.8)

# Header title
p_header = doc.add_paragraph()
p_header.alignment = WD_ALIGN_PARAGRAPH.CENTER
run_h1 = p_header.add_run('HỘI THI THIẾT KẾ CHỦ ĐỀ DẠY HỌC STEM / CHỦ ĐỀ DẠY HỌC SỐ\nNĂM HỌC 2026 - 2027\n')
run_h1.bold = True
run_h1.font.size = Pt(13)
run_h1.font.name = 'Times New Roman'
run_h1.font.color.rgb = RGBColor(0, 32, 96)

run_h2 = p_header.add_run('HỒ SƠ DỰ THI - PHẦN 1: PHẦN TỔNG QUAN\n(Kèm theo Kế hoạch số 12070/KH-SGDĐT của Sở GD&ĐT TP.HCM)\n')
run_h2.bold = True
run_h2.font.size = Pt(14)
run_h2.font.name = 'Times New Roman'
run_h2.font.color.rgb = RGBColor(192, 0, 0)

# Section 1: Thông tin giáo viên
p1 = doc.add_heading('I. THÔNG TIN GIỚI THIỆU VỀ GIÁO VIÊN VÀ ĐƠN VỊ DỰ THI', level=1)
p1.paragraph_format.space_before = Pt(12)
p1.paragraph_format.space_after = Pt(6)

table = doc.add_table(rows=8, cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.autofit = False

fields = [
    ('Họ và tên giáo viên dự thi:', '[Điền họ và tên giáo viên, ví dụ: NGUYỄN VĂN A]'),
    ('Năm sinh:', '[Điền năm sinh, ví dụ: 1996]'),
    ('Giới tính:', '[Nam / Nữ]'),
    ('Bộ môn đăng ký dự thi:', 'Lịch sử (Phân môn Lịch sử - Môn Lịch sử và Địa lí)'),
    ('Cấp học đăng ký:', 'Trung học cơ sở (THCS) - Khối lớp 8'),
    ('Thâm niên công tác:', '[Điền số năm, ví dụ: 06 năm]'),
    ('Tên đơn vị công tác (Trường):', '[Điền tên trường THCS, ví dụ: Trường THCS ...]'),
    ('Số điện thoại liên lạc cá nhân:', '[Điền số điện thoại liên hệ: 09xx xxx xxx]')
]

for i, (k, v) in enumerate(fields):
    row = table.rows[i]
    cell_k, cell_v = row.cells[0], row.cells[1]
    cell_k.width = Inches(2.5)
    cell_v.width = Inches(4.3)
    
    pk = cell_k.paragraphs[0]
    pk.paragraph_format.space_before = Pt(3)
    pk.paragraph_format.space_after = Pt(3)
    rk = pk.add_run(k)
    rk.bold = True
    rk.font.name = 'Times New Roman'
    rk.font.size = Pt(11)
    
    pv = cell_v.paragraphs[0]
    pv.paragraph_format.space_before = Pt(3)
    pv.paragraph_format.space_after = Pt(3)
    rv = pv.add_run(v)
    rv.font.name = 'Times New Roman'
    rv.font.size = Pt(11)
    if '[' in v:
        rv.font.color.rgb = RGBColor(192, 0, 0)

    # Shading for header column
    cell_k._tc.get_or_add_tcPr().append(parse_xml(r'<w:shd {} w:fill="F2F2F2"/>'.format(nsdecls('w'))))

# Section 2: Tên và tóm lược nội dung chủ đề
p2 = doc.add_heading('II. TÊN VÀ TÓM LƯỢC NỘI DUNG CHỦ ĐỀ DỰ THI', level=1)
p2.paragraph_format.space_before = Pt(14)
p2.paragraph_format.space_after = Pt(6)

p_name = doc.add_paragraph()
r = p_name.add_run('1. Tên chủ đề dạy học số: ')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(12)
r2 = p_name.add_run('HÀO KHÍ TÂY SƠN (1771 – 1789) – THIÊN TÀI QUÂN SỰ QUANG TRUNG')
r2.bold = True
r2.font.name = 'Times New Roman'
r2.font.size = Pt(12)
r2.font.color.rgb = RGBColor(192, 0, 0)

p_subj = doc.add_paragraph()
r = p_subj.add_run('2. Thuộc môn học: ')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(12)
r2 = p_subj.add_run('Lịch sử và Địa lí 8 (Bộ sách Kết nối tri thức với cuộc sống – Phân môn Lịch sử, Bài 8: Phong trào Tây Sơn).')
r2.font.name = 'Times New Roman'
r2.font.size = Pt(12)

p_sum = doc.add_paragraph()
r = p_sum.add_run('3. Tóm lược nội dung chủ đề:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(12)
summary_text = (
    'Chủ đề dạy học số "Hào khí Tây Sơn (1771 – 1789)" được xây dựng nhằm đổi mới căn bản phương pháp dạy học lịch sử '
    'truyền thống bằng việc tích hợp giải pháp học liệu số thông minh (Nền tảng Web tương tác trực tiếp tại https://lichsu-eight.vercel.app/). '
    'Chủ đề tái hiện toàn diện và sinh động 4 thắng lợi quân sự - chính trị vĩ đại nhất của phong trào Tây Sơn thông qua 4 trạm không gian số độc lập:\n'
    '• Trạm 1: Khởi nghĩa Tây Sơn bùng nổ, xây dựng căn cứ Tây Sơn thượng đạo & lật đổ chính quyền chúa Nguyễn ở Đàng Trong (1771 – 1777).\n'
    '• Trạm 2: Đại phá 5 vạn quân Xiêm – Nghệ thuật mai phục thủy chiến Rạch Gầm – Xoài Mút (1785).\n'
    '• Trạm 3: Tiến quân ra Bắc Hà lật đổ hai tập đoàn phong kiến Trịnh – Nguyễn (1786 – 1788), xóa bỏ ranh giới chia cắt Đàng Trong – Đàng Ngoài hơn 200 năm.\n'
    '• Trạm 4: Bản hùng ca mùa xuân Kỷ Dậu 1789 – Hoàng đế Quang Trung chỉ huy hành quân thần tốc đại phá 29 vạn quân Mãn Thanh tại Ngọc Hồi – Đống Đa.\n\n'
    'Đặc biệt, học sinh không tiếp thu một chiều mà tự lực làm chủ không gian làm việc số: phân tích tư liệu chuẩn SGK Kết nối tri thức, '
    'thu âm giọng đọc Podcast lịch sử ngay trên web, giải mật mã bí ẩn sử học, nộp bài qua Trung tâm kiểm duyệt sư phạm của giáo viên, '
    'và quét mã QR bằng điện thoại để thả tim, bình luận trực tiếp theo thời gian thực (Realtime Cloud Sync).'
)
r_sum_content = p_sum.add_run(summary_text)
r_sum_content.font.name = 'Times New Roman'
r_sum_content.font.size = Pt(11)

# Section 3: Vị trí kiến thức
p3 = doc.add_heading('III. VỊ TRÍ KIẾN THỨC NỀN VÀ KIẾN THỨC, KỸ NĂNG HÌNH THÀNH', level=1)
p3.paragraph_format.space_before = Pt(14)
p3.paragraph_format.space_after = Pt(6)

p_kn = doc.add_paragraph()
r = p_kn.add_run('1. Kiến thức và kĩ năng nền tảng của học sinh trước khi thực hiện chủ đề:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(12)
r_kn = p_kn.add_run(
    '• Kiến thức nền: Tình hình phân chia Đàng Trong – Đàng Ngoài thế kỉ XVII – XVIII, sự suy thoái mục nát của tập đoàn phong kiến Trịnh – Nguyễn '
    'và đời sống cùng cực của nhân dân làm bùng nổ các cuộc khởi nghĩa nông dân (đã học ở các bài trước thuộc Chương 3).\n'
    '• Kĩ năng nền: Kĩ năng đọc hiểu tư liệu văn bản lịch sử, kĩ năng đọc lược đồ chiến dịch quân sự, kĩ năng làm việc nhóm và kĩ năng sử dụng các thiết bị công nghệ thông tin (điện thoại thông minh, máy tính bảng/máy tính có kết nối mạng).'
)
r_kn.font.name = 'Times New Roman'
r_kn.font.size = Pt(11)

p_ht = doc.add_paragraph()
r = p_ht.add_run('2. Kiến thức và kĩ năng sẽ được hình thành sau chủ đề:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(12)
r_ht = p_ht.add_run(
    '• Kiến thức mới hình thành: Nắm vững tiến trình 4 mốc son của phong trào Tây Sơn; hiểu sâu sắc nghệ thuật tác chiến quân sự đỉnh cao '
    '(nghi binh thủy chiến Rạch Gầm, hành quân thần tốc chia 5 mũi giáp công Ngọc Hồi – Đống Đa); nhận thức toàn diện vai trò lịch sử của phong trào Tây Sơn '
    'và công lao vĩ đại của người anh hùng áo vải Quang Trung – Nguyễn Huệ.\n'
    '• Kĩ năng mới hình thành: Kĩ năng tự lực xử lý đa phương tiện số (văn bản SGK, lược đồ số, tranh điện ảnh 3D); kĩ năng tóm tắt diễn biến và tường thuật podcast lịch sử; '
    'kĩ năng phản biện, chấm điểm và đánh giá đồng đẳng (Peer Review) qua công nghệ quét mã QR trên môi trường số.'
)
r_ht.font.name = 'Times New Roman'
r_ht.font.size = Pt(11)

# Section 4: Phẩm chất & Năng lực
p4 = doc.add_heading('IV. PHẨM CHẤT VÀ NĂNG LỰC HỌC SINH ĐẠT ĐƯỢC', level=1)
p4.paragraph_format.space_before = Pt(14)
p4.paragraph_format.space_after = Pt(6)

p_nl = doc.add_paragraph()
r = p_nl.add_run('1. Năng lực hình thành:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(12)
r_nl = p_nl.add_run(
    '• Năng lực Lịch sử đặc thù: Năng lực tìm hiểu lịch sử thông qua khai thác nguồn học liệu số; năng lực nhận thức và tư duy lịch sử; năng lực vận dụng kiến thức, kĩ năng đã học để liên hệ bài học bảo vệ chủ quyền biên cương và biển đảo hôm nay.\n'
    '• Năng lực chung: Năng lực tự chủ và tự học (tự nghiên cứu tư liệu số và SGK Kết nối tri thức); năng lực giao tiếp và hợp tác (thảo luận nhóm phân công vai trò, thu âm podcast, báo cáo triển lãm); năng lực giải quyết vấn đề và sáng tạo (giải mã mật mã lịch sử).\n'
    '• Năng lực số (Digital Literacy): Sử dụng thành thạo nền tảng học liệu tương tác, ghi âm trực tiếp trên web, quét mã QR tương tác đa nền tảng và đánh giá trực tuyến theo thời gian thực.'
)
r_nl.font.name = 'Times New Roman'
r_nl.font.size = Pt(11)

p_pc = doc.add_paragraph()
r = p_pc.add_run('2. Phẩm chất hình thành:\n')
r.bold = True
r.font.name = 'Times New Roman'
r.font.size = Pt(12)
r_pc = p_pc.add_run(
    '• Yêu nước: Khơi dậy niềm tự hào sâu sắc về truyền thống quật cường chống giặc ngoại xâm của dân tộc, lòng biết ơn vô hạn đối với Hoàng đế Quang Trung và nghĩa quân Tây Sơn.\n'
    '• Trách nhiệm: Ý thức gìn giữ, phát huy giá trị di sản lịch sử văn hóa dân tộc và trách nhiệm lan tỏa tri thức lịch sử trên không gian mạng.'
)
r_pc.font.name = 'Times New Roman'
r_pc.font.size = Pt(11)

# Section 5: Thời lượng
p5 = doc.add_heading('V. THỜI LƯỢNG THỰC HIỆN CHỦ ĐỀ', level=1)
p5.paragraph_format.space_before = Pt(14)
p5.paragraph_format.space_after = Pt(6)
p_tl = doc.add_paragraph()
r_tl = p_tl.add_run('• Tổng thời lượng: 02 tiết (90 phút) – Chuẩn chỉnh theo phân phối chương trình và quy định của Hội thi (không vượt quá 02 tiết).\n'
                    '  - Tiết 1 (45 phút): Khởi động hào khí (Xem điện ảnh 3D & Lời hiệu triệu Quang Trung) -> Khám phá, làm việc nhóm trên Không gian số 4 chuyên đề, thu âm podcast và nộp bài lên Giáo viên kiểm duyệt.\n'
                    '  - Tiết 2 (45 phút): Khai mạc Phòng Triển lãm Poster Di sản -> Đại diện 4 nhóm thuyết trình -> Quét mã QR trải nghiệm chéo, thả tim và bình luận đồng đẳng -> Tổng kết, chuẩn hóa và dặn dò vận dụng.')
r_tl.font.name = 'Times New Roman'
r_tl.font.size = Pt(11)

# Section 6: Không gian thực hiện
p6 = doc.add_heading('VI. KHÔNG GIAN THỰC HIỆN CHỦ ĐỀ', level=1)
p6.paragraph_format.space_before = Pt(14)
p6.paragraph_format.space_after = Pt(6)
p_kg = doc.add_paragraph()
r_kg = p_kg.add_run('• Không gian kết hợp đa chiều:\n'
                    '  1. Không gian lớp học trực tiếp: Máy tính giáo viên kết nối máy chiếu/màn hình tương tác thông minh, bố trí 4 cụm bàn tương ứng 4 nhóm chiến dịch.\n'
                    '  2. Không gian số hóa trực tuyến (Website học liệu số): https://lichsu-eight.vercel.app/ (hỗ trợ cả kết nối Internet trực tuyến lẫn chạy offline mượt mà không cần mạng trường).\n'
                    '  3. Không gian học tập cá nhân/di động: Học sinh sử dụng điện thoại thông minh/máy tính bảng quét mã QR để tương tác, nghe podcast và chấm điểm đồng đẳng.')
r_kg.font.name = 'Times New Roman'
r_kg.font.size = Pt(11)

# Section 7: Mục tiêu cần đạt
p7 = doc.add_heading('VII. MỤC TIÊU CẦN ĐẠT SAU KHI THỰC HIỆN CHỦ ĐỀ', level=1)
p7.paragraph_format.space_before = Pt(14)
p7.paragraph_format.space_after = Pt(6)
p_mt = doc.add_paragraph()
r_mt = p_mt.add_run('Đối chiếu với Chương trình GDPT 2018 môn Lịch sử và Địa lí 8 (Bài 8: Phong trào Tây Sơn), sau khi hoàn thành chủ đề, 100% học sinh đạt được:\n'
                    '1. Trình bày được nguyên nhân bùng nổ phong trào Tây Sơn và các thắng lợi tiêu biểu: lật đổ chúa Nguyễn ở Đàng Trong, đánh tan 5 vạn quân Xiêm tại Rạch Gầm – Xoài Mút, tiến quân ra Bắc Hà lật đổ chúa Trịnh – vua Lê, đại phá 29 vạn quân Thanh mùa xuân Kỷ Dậu 1789.\n'
                    '2. Nêu và phân tích được nét độc đáo trong nghệ thuật quân sự của nghĩa quân Tây Sơn và tài năng quân sự kiệt xuất của Quang Trung – Nguyễn Huệ.\n'
                    '3. Đánh giá được nguyên nhân thắng lợi và ý nghĩa lịch sử sâu sắc của phong trào Tây Sơn đối với tiến trình thống nhất và bảo vệ độc lập dân tộc.\n'
                    '4. Phát triển vượt bậc năng lực tự học, thuyết trình tự tin, làm việc nhóm hợp tác và năng lực ứng dụng công nghệ thông tin trong học tập lịch sử.')
r_mt.font.name = 'Times New Roman'
r_mt.font.size = Pt(11)

# Save document
output_path = r'docs/ho_so_hoi_thi/Folder_1_Phan_tong_quan/Lichsu_THCS_[Ho-Va-Ten]_STEM_P1.docx'
doc.save(output_path)
print('Saved Lichsu_THCS_[Ho-Va-Ten]_STEM_P1.docx successfully.')
