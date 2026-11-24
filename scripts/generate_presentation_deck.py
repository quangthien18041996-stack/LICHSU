import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette - Historical Noble Theme
    BG_DARK = RGBColor(18, 14, 13)       # #120e0d Deep Charcoal Brown
    BG_CARD = RGBColor(28, 21, 19)       # #1c1513 Card Background
    RED_BURGUNDY = RGBColor(136, 19, 19) # #881313 Royal Crimson
    GOLD_AMBER = RGBColor(217, 119, 6)   # #d97706 Warm Gold
    GOLD_LIGHT = RGBColor(254, 243, 199) # #fef3c7 Light Parchment Gold
    GOLD_BRIGHT = RGBColor(245, 158, 11) # #f59e0b Bright Amber
    TEXT_WHITE = RGBColor(245, 245, 244) # #f5f5f4 Off-white
    TEXT_MUTED = RGBColor(168, 162, 158) # #a8a29e Muted stone
    BORDER_GOLD = RGBColor(180, 83, 9)   # #b45309 Amber border
    GREEN_ACCENT = RGBColor(16, 185, 129)# #10b981 Emerald
    BLUE_ACCENT = RGBColor(14, 165, 233) # #0ea5e9 Cyan
    PURPLE_ACCENT = RGBColor(168, 85, 247) # Purple

    # Helper: Set slide background
    def set_slide_bg(slide, color=BG_DARK):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = color

    # Helper: Add header bar
    def add_header(slide, title_text, category_text="LỊCH SỬ 8 - KẾT NỐI TRI THỨC VỚI CUỘC SỐNG", step_badge=None):
        # Top gradient-like ribbon shape
        header_bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(0.4), Inches(12.333), Inches(0.95))
        header_bar.fill.solid()
        header_bar.fill.fore_color.rgb = BG_CARD
        header_bar.line.color.rgb = BORDER_GOLD
        header_bar.line.width = Pt(1.5)

        # Left accent stripe
        accent = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.5), Inches(0.4), Inches(0.15), Inches(0.95))
        accent.fill.solid()
        accent.fill.fore_color.rgb = RED_BURGUNDY
        accent.line.fill.background()

        tf = header_bar.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf.margin_left = Inches(0.35)
        tf.margin_top = Inches(0.08)

        # Paragraph 1: Category / Subtitle
        p1 = tf.paragraphs[0]
        p1.text = category_text.upper()
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.name = "Arial"
        p1.font.color.rgb = GOLD_BRIGHT

        # Paragraph 2: Title
        p2 = tf.add_paragraph()
        p2.text = title_text
        p2.font.size = Pt(19)
        p2.font.bold = True
        p2.font.name = "Arial"
        p2.font.color.rgb = GOLD_LIGHT

        # Optional Step badge on top right
        if step_badge:
            badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.8), Inches(0.55), Inches(1.8), Inches(0.65))
            badge.fill.solid()
            badge.fill.fore_color.rgb = RED_BURGUNDY
            badge.line.color.rgb = GOLD_BRIGHT
            badge.line.width = Pt(1)
            btf = badge.text_frame
            btf.vertical_anchor = MSO_ANCHOR.MIDDLE
            bp = btf.paragraphs[0]
            bp.alignment = PP_ALIGN.CENTER
            bp.text = step_badge
            bp.font.size = Pt(11)
            bp.font.bold = True
            bp.font.name = "Arial"
            bp.font.color.rgb = GOLD_LIGHT

    # Helper: Add slide footer
    def add_footer(slide, current_page, total_pages=12):
        footer_box = slide.shapes.add_textbox(Inches(0.5), Inches(7.0), Inches(12.333), Inches(0.4))
        ftf = footer_box.text_frame
        ftf.word_wrap = True
        fp = ftf.paragraphs[0]
        fp.font.size = Pt(9.5)
        fp.font.name = "Arial"
        fp.font.color.rgb = TEXT_MUTED

        # Left side info, right side page number
        fp.text = f"Trường Liên cấp TH - THCS Nguyễn Quốc Phú  |  GV: Nguyễn Đức An  |  Học liệu số: https://lichsu-eight.vercel.app/            Trang {current_page}/{total_pages}"

    # Helper: Add card with styling
    def add_card(slide, left, top, width, height, title, items=[], border_color=BORDER_GOLD, fill_color=BG_CARD, title_color=GOLD_BRIGHT):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = fill_color
        card.line.color.rgb = border_color
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        tf.margin_left = Inches(0.2)
        tf.margin_right = Inches(0.2)
        tf.margin_top = Inches(0.2)
        tf.margin_bottom = Inches(0.2)

        # Title
        p_title = tf.paragraphs[0]
        p_title.text = title
        p_title.font.size = Pt(14)
        p_title.font.bold = True
        p_title.font.name = "Arial"
        p_title.font.color.rgb = title_color

        # Items
        for it in items:
            p = tf.add_paragraph()
            p.text = f"• {it}"
            p.font.size = Pt(11)
            p.font.name = "Arial"
            p.font.color.rgb = TEXT_WHITE
            p.space_before = Pt(4)

        return card

    # ==============================================================
    # SLIDE 1: BÌA TRÌNH CHIẾU (TITLE SLIDE)
    # ==============================================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)

    # Top Banner Badge
    top_badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.5), Inches(11.733), Inches(0.55))
    top_badge.fill.solid()
    top_badge.fill.fore_color.rgb = RED_BURGUNDY
    top_badge.line.color.rgb = GOLD_BRIGHT
    top_badge.line.width = Pt(1)
    p = top_badge.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "HỘI THI THIẾT KẾ BÀI DẠY TÍCH HỢP STEM & DẠY HỌC SỐ CẤP THÀNH PHỐ NĂM HỌC 2026 - 2027"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_LIGHT

    # Main Card Box
    main_box = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.2), Inches(7.5), Inches(5.6))
    main_box.fill.solid()
    main_box.fill.fore_color.rgb = BG_CARD
    main_box.line.color.rgb = BORDER_GOLD
    main_box.line.width = Pt(2)
    tf1 = main_box.text_frame
    tf1.word_wrap = True
    tf1.margin_left = Inches(0.4)
    tf1.margin_right = Inches(0.4)
    tf1.margin_top = Inches(0.4)

    p = tf1.paragraphs[0]
    p.text = "TRƯỜNG LIÊN CẤP TH - THCS NGUYỄN QUỐC PHÚ"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_BRIGHT

    p = tf1.add_paragraph()
    p.text = "Môn: Lịch sử và Địa lí 8 (Bộ sách Kết nối tri thức với cuộc sống)"
    p.font.size = Pt(11)
    p.font.name = "Arial"
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(4)

    p = tf1.add_paragraph()
    p.text = "BÀI 8: PHONG TRÀO TÂY SƠN"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_LIGHT
    p.space_before = Pt(14)

    p = tf1.add_paragraph()
    p.text = "(GIAI ĐOẠN 1771 - 1789)"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_BRIGHT

    p = tf1.add_paragraph()
    p.text = "HƯỚNG DẪN HỌC TẬP & THAO TÁC TRÊN NỀN TẢNG SỐ"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = RED_BURGUNDY
    p.space_before = Pt(12)

    p = tf1.add_paragraph()
    p.text = "Không gian học tập số tương tác: 'Hào Khí Tây Sơn'"
    p.font.size = Pt(12)
    p.font.italic = True
    p.font.name = "Arial"
    p.font.color.rgb = TEXT_WHITE

    p = tf1.add_paragraph()
    p.text = "------------------------------------------------------------"
    p.font.size = Pt(10)
    p.font.color.rgb = BORDER_GOLD
    p.space_before = Pt(10)

    p = tf1.add_paragraph()
    p.text = "• Giáo viên thực hiện: Thầy NGUYỄN ĐỨC AN"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_LIGHT
    p.space_before = Pt(8)

    p = tf1.add_paragraph()
    p.text = "• Thời lượng: 02 Tiết (90 phút)  |  Định dạng chuẩn CV 5512/BGDĐT"
    p.font.size = Pt(11)
    p.font.name = "Arial"
    p.font.color.rgb = TEXT_WHITE
    p.space_before = Pt(4)

    p = tf1.add_paragraph()
    p.text = "• Địa chỉ web trực tuyến: https://lichsu-eight.vercel.app/"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_BRIGHT
    p.space_before = Pt(4)

    # Right Image
    img_path = "images/quang_trung_epic_victory_1789.jpg"
    if os.path.exists(img_path):
        pic = s1.shapes.add_picture(img_path, Inches(8.5), Inches(1.2), Inches(4.033), Inches(5.6))

    add_footer(s1, 1)

    # ==============================================================
    # SLIDE 2: MỤC TIÊU BÀI HỌC & LỘ TRÌNH 2 TIẾT
    # ==============================================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "MỤC TIÊU BÀI HỌC & HÀNH TRÌNH HỌC TẬP SỐ", "TỔNG QUAN CHƯƠNG TRÌNH", "LỘ TRÌNH 2 TIẾT")

    # Column 1: Năng lực Lịch sử
    add_card(s2, Inches(0.5), Inches(1.6), Inches(3.9), Inches(5.1),
             "1. NĂNG LỰC LỊCH SỬ",
             [
                 "Khám phá 4 mốc son lịch sử tiêu biểu của phong trào Tây Sơn (1771 - 1789).",
                 "Phân tích tài nghệ quân sự tài tình: thủy chiến Rạch Gầm - Xoài Mút, tiến quân thần tốc Ngọc Hồi - Đống Đa.",
                 "Đánh giá công lao to lớn của Hoàng đế Quang Trung - Nguyễn Huệ trong sự nghiệp thống nhất và bảo vệ Tổ quốc.",
                 "Khai thác và xử lý nguồn tư liệu lịch sử SGK Kết nối tri thức."
             ],
             BORDER_GOLD, BG_CARD, GOLD_BRIGHT)

    # Column 2: Năng lực Số & STEM
    add_card(s2, Inches(4.7), Inches(1.6), Inches(3.9), Inches(5.1),
             "2. NĂNG LỰC SỐ & STEM",
             [
                 "Làm chủ không gian học tập số tương tác trực tuyến 60fps.",
                 "Xử lý dữ liệu đa phương tiện: tranh điện ảnh 3D, lược đồ tương tác, thuyết minh audio HD.",
                 "Thực hành giải 'Mật mã Lịch sử' và ứng dụng công cụ thu âm thuyết minh trực tiếp trên web.",
                 "Trải nghiệm quét mã QR ISO/IEC 18004 và đánh giá đồng đẳng Realtime Cloud Sync thời gian thực."
             ],
             BORDER_GOLD, BG_CARD, GOLD_LIGHT)

    # Column 3: Tiến trình 4 Trạm học tập
    add_card(s2, Inches(8.9), Inches(1.6), Inches(3.9), Inches(5.1),
             "3. HÀNH TRÌNH 4 TRẠM SỐ",
             [
                 "TRẠM 1: Khởi động hào hùng - Nghe lời hiệu triệu Quang Trung & ca khúc Hào Khí Việt Nam (7').",
                 "TRẠM 2: 4 Nhóm chiến dịch khai thác tư liệu SGK, giải mật mã & làm hồ sơ số (25').",
                 "TRẠM 3: Giáo viên kiểm duyệt sư phạm & tự động xuất bản Poster Triển lãm (7').",
                 "TRẠM 4 (Tiết 2): Thuyết trình Poster, quét mã QR Thả tim ❤️ và nhận xét chéo Realtime (35')."
             ],
             RED_BURGUNDY, BG_CARD, GOLD_BRIGHT)

    add_footer(s2, 2)

    # ==============================================================
    # SLIDE 3: KHỞI ĐỘNG HÀO HÙNG - LỜI HIỆU TRIỆU QUANG TRUNG
    # ==============================================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "HOẠT ĐỘNG 1: KHỞI ĐỘNG HÀO HÙNG TRÊN KHÔNG GIAN SỐ", "TIẾT 1 - BÀI DẠY SỐ", "TRẠM 1 (7 PHÚT)")

    # Left: Content & Quote
    quote_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.6), Inches(5.8), Inches(5.1))
    quote_card.fill.solid()
    quote_card.fill.fore_color.rgb = BG_CARD
    quote_card.line.color.rgb = BORDER_GOLD
    quote_card.line.width = Pt(1.5)
    tf3 = quote_card.text_frame
    tf3.word_wrap = True
    tf3.margin_left = Inches(0.3)
    tf3.margin_right = Inches(0.3)
    tf3.margin_top = Inches(0.3)

    p = tf3.paragraphs[0]
    p.text = "🎬 TRẢI NGHIỆM ĐIỆN ẢNH SỬ THI"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_BRIGHT

    p = tf3.add_paragraph()
    p.text = "• Giáo viên mở Tab 'Tổng Quan & Phim Tư Liệu' trên máy chiếu lớn."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_WHITE
    p.space_before = Pt(6)

    p = tf3.add_paragraph()
    p.text = "• Ca khúc chủ đề vang lên: 'Hào Khí Việt Nam' kết hợp hiệu ứng tàn lửa chiến trận sống động."
    p.font.size = Pt(11)
    p.font.color.rgb = TEXT_WHITE
    p.space_before = Pt(4)

    p = tf3.add_paragraph()
    p.text = "📜 LỜI HIỂU DỤ ĐANH THÉP CỦA HOÀNG ĐẾ QUANG TRUNG (1788):"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = GOLD_LIGHT
    p.space_before = Pt(10)

    p = tf3.add_paragraph()
    p.text = '“Đánh cho để dài tóc,\n Đánh cho để đen răng,\n Đánh cho nó chích luân bất phản,\n Đánh cho nó phiến giáp bất hoàn,\n Đánh cho sử tri nam quốc anh hùng chi hữu chủ!”'
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.italic = True
    p.font.name = "Georgia"
    p.font.color.rgb = GOLD_BRIGHT
    p.space_before = Pt(8)

    p = tf3.add_paragraph()
    p.text = "💡 Câu hỏi định hướng: Em cảm nhận được khí phách và quyết tâm gì của nghĩa quân Tây Sơn qua lời hiệu dụ trên?"
    p.font.size = Pt(11)
    p.font.italic = True
    p.font.color.rgb = TEXT_MUTED
    p.space_before = Pt(10)

    # Right: Screenshot Tab 1
    img1 = "images/hinh1_tong_quan.png"
    if os.path.exists(img1):
        s3.shapes.add_picture(img1, Inches(6.6), Inches(1.6), Inches(6.2), Inches(5.1))

    add_footer(s3, 3)

    # ==============================================================
    # SLIDE 4: PHÂN CHIA 4 NHÓM CHIẾN DỊCH & NHIỆM VỤ
    # ==============================================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "PHÂN CÔNG 4 NHÓM CHIẾN DỊCH & NHIỆM VỤ TRỌNG TÂM", "HOẠT ĐỘNG NHÓM HÌNH THÀNH KIẾN THỨC", "4 CHUYÊN ĐỀ")

    # 4 Cards in 2x2 Grid
    # Card Nhóm 1
    add_card(s4, Inches(0.5), Inches(1.6), Inches(5.9), Inches(2.45),
             "NHÓM 1: KHỞI NGHĨA & LẬT ĐỔ CHÚA NGUYỄN (1771 - 1777)",
             [
                 "Địa bàn: Căn cứ Tây Sơn thượng đạo (An Khê, Gia Lai) & hạ đạo.",
                 "Lực lượng: Nông dân nghèo, đồng bào thiểu số Bana, Chăm, thợ thủ công.",
                 "Chiến công: 4 lần tiến quân vào Gia Định lật đổ chính quyền chúa Nguyễn.",
                 "Từ khóa trọng tâm: Căn cứ địa, cờ đào áo vải, lấy của nhà giàu chia cho người nghèo."
             ],
             BORDER_GOLD, BG_CARD, GOLD_BRIGHT)

    # Card Nhóm 2
    add_card(s4, Inches(6.9), Inches(1.6), Inches(5.9), Inches(2.45),
             "NHÓM 2: KHÁNG CHIẾN CHỐNG QUÂN XIÊM - RẠCH GẦM (1785)",
             [
                 "Bối cảnh: Nguyễn Ánh cầu viện 5 vạn quân Xiêm tràn sang cướp phá miền Tây.",
                 "Địa bàn quyết chiến: Khúc sông Tiền từ Rạch Gầm đến Xoài Mút (Tiền Giang).",
                 "Nghệ thuật quân sự: Thủy chiến kết hợp pháo binh, nghi binh nhử địch vào bẫy mai phục.",
                 "Kết quả: Đánh tan 5 vạn quân giặc, 'người Xiêm sau trận ấy sợ Tây Sơn như sợ cọp'."
             ],
             RED_BURGUNDY, BG_CARD, GOLD_LIGHT)

    # Card Nhóm 3
    add_card(s4, Inches(0.5), Inches(4.3), Inches(5.9), Inches(2.45),
             "NHÓM 3: TIẾN QUÂN RA BẮC HÀ LẬT ĐỔ TRỊNH - NGUYỄN (1786 - 1788)",
             [
                 "Chiến công Phú Xuân: Hạ thành Phú Xuân, giải phóng toàn bộ Đàng Trong (1786).",
                 "Tiến thẳng Thăng Long: Với khẩu hiệu 'Phù Lê diệt Trịnh', đánh sụp tập đoàn chúa Trịnh.",
                 "Lật đổ vua Lê Chiêu Thống: Chấm dứt hoàn toàn chế độ phong kiến thối nát (1788).",
                 "Ý nghĩa: Đặt nền móng vững chắc cho sự nghiệp thống nhất giang sơn sau hơn 200 năm chia cắt."
             ],
             BLUE_ACCENT, BG_CARD, GOLD_LIGHT)

    # Card Nhóm 4
    add_card(s4, Inches(6.9), Inches(4.3), Inches(5.9), Inches(2.45),
             "NHÓM 4: ĐẠI PHÁ 29 VẠN QUÂN THANH - KỶ DẬU (1789)",
             [
                 "Bối cảnh: Lê Chiêu Thống rước 29 vạn quân Mãn Thanh do Tôn Sĩ Nghị chỉ huy sang xâm lược.",
                 "Hành quân thần tốc: Nguyễn Huệ lên ngôi Hoàng đế tại Phú Xuân, hành quân ngày đêm ra Bắc.",
                 "Quyết chiến đỉnh cao: Đêm mùng 4 rạng mùng 5 Tết đánh chiếm Ngọc Hồi, Khương Thượng, Đống Đa.",
                 "Chiến thắng huy hoàng: Trưa mùng 5 Tết Kỷ Dậu 1789, Quang Trung ngự trên lưng voi vào Thăng Long."
             ],
             GREEN_ACCENT, BG_CARD, GOLD_BRIGHT)

    add_footer(s4, 4)

    # ==============================================================
    # SLIDE 5: HƯỚNG DẪN BƯỚC 1 - QUÉT MÃ QR & VÀO KHÔNG GIAN NHÓM
    # ==============================================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "HƯỚNG DẪN THAO TÁC - BƯỚC 1: QUÉT MÃ QR & CHỌN NHÓM", "QUY TRÌNH HỌC TẬP SỐ", "BƯỚC 1 / 4")

    # Left Instructions
    inst1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.6), Inches(5.5), Inches(5.1))
    inst1.fill.solid()
    inst1.fill.fore_color.rgb = BG_CARD
    inst1.line.color.rgb = BORDER_GOLD
    inst1.line.width = Pt(1.5)
    tfi1 = inst1.text_frame
    tfi1.word_wrap = True
    tfi1.margin_left = Inches(0.3)
    tfi1.margin_right = Inches(0.3)
    tfi1.margin_top = Inches(0.3)

    p = tfi1.paragraphs[0]
    p.text = "📲 CÁC THAO TÁC ĐẦU GIỜ CỦA NHÓM:"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_BRIGHT

    steps1 = [
        "1. Quét mã QR trên màn chiếu: Dùng Camera điện thoại hoặc Zalo quét mã QR toàn lớp (hoặc mở trình duyệt truy cập: https://lichsu-eight.vercel.app/).",
        "2. Chuyển sang Tab nhóm: Bấm vào mục '4 Nhóm Làm Việc' trên thanh Menu chính.",
        "3. Chọn đúng Nhóm của mình:\n   • Nhóm 1: Khởi nghĩa & Đàng Trong\n   • Nhóm 2: Thủy chiến Rạch Gầm\n   • Nhóm 3: Tiến quân ra Bắc Hà\n   • Nhóm 4: Đại phá quân Thanh 1789",
        "4. Nhập thông tin nhóm: Điền Tên nhóm sáng tạo và Danh sách thành viên cùng tham gia nghiên cứu."
    ]
    for s in steps1:
        p = tfi1.add_paragraph()
        p.text = s
        p.font.size = Pt(11.5)
        p.font.name = "Arial"
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(8)

    # Right: Screenshot Hinh 2
    img2 = "images/hinh2_khong_gian_nhom.png"
    if os.path.exists(img2):
        s5.shapes.add_picture(img2, Inches(6.3), Inches(1.6), Inches(6.5), Inches(5.1))

    add_footer(s5, 5)

    # ==============================================================
    # SLIDE 6: HƯỚNG DẪN BƯỚC 2 - KHAI THÁC TƯ LIỆU & LƯỢC ĐỒ SỐ
    # ==============================================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "HƯỚNG DẪN THAO TÁC - BƯỚC 2: KHAI THÁC TƯ LIỆU & LƯỢC ĐỒ SỐ", "QUY TRÌNH HỌC TẬP SỐ", "BƯỚC 2 / 4")

    # Left Instructions
    inst2 = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.6), Inches(5.5), Inches(5.1))
    inst2.fill.solid()
    inst2.fill.fore_color.rgb = BG_CARD
    inst2.line.color.rgb = BORDER_GOLD
    inst2.line.width = Pt(1.5)
    tfi2 = inst2.text_frame
    tfi2.word_wrap = True
    tfi2.margin_left = Inches(0.3)
    tfi2.margin_right = Inches(0.3)
    tfi2.margin_top = Inches(0.3)

    p = tfi2.paragraphs[0]
    p.text = "🔍 KHAI THÁC HỌC LIỆU SỐ TÍCH HỢP:"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_BRIGHT

    steps2 = [
        "1. Đọc đoạn trích SGK Lịch sử 8: Hệ thống tích hợp sẵn các đoạn trích nguyên văn chuẩn theo bộ sách Kết nối tri thức với cuộc sống.",
        "2. Quan sát Lược đồ trận đánh: Nhấp vào ảnh lược đồ để phóng to toàn màn hình, quan sát thế trận sông ngòi, hướng tiến công và các mũi vu hồi mai phục.",
        "3. Thảo luận nhóm giải quyết 3 câu hỏi cốt lõi:\n   • Ai là người chỉ huy tối cao và đóng vai trò quyết định?\n   • Đâu là nét đặc sắc trong nghệ thuật quân sự của Tây Sơn?\n   • Thắng lợi này có ý nghĩa gì đối với lịch sử dân tộc?",
        "4. Phân công ghi chép: Thư ký nhóm tổng hợp ý kiến để sẵn sàng điền vào các trường biểu mẫu số."
    ]
    for s in steps2:
        p = tfi2.add_paragraph()
        p.text = s
        p.font.size = Pt(11.5)
        p.font.name = "Arial"
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(8)

    # Right: Map Image
    img_map = "images/luoc_do_rach_gam_xoai_mut.jpg"
    if os.path.exists(img_map):
        s6.shapes.add_picture(img_map, Inches(6.3), Inches(1.6), Inches(6.5), Inches(5.1))

    add_footer(s6, 6)

    # ==============================================================
    # SLIDE 7: HƯỚNG DẪN BƯỚC 3 - HOÀN THIỆN HỒ SƠ & GIẢI MẬT MÃ
    # ==============================================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7)
    add_header(s7, "HƯỚNG DẪN THAO TÁC - BƯỚC 3: ĐIỀN BÀI LÀM & GIẢI MẬT MÃ", "QUY TRÌNH HỌC TẬP SỐ", "BƯỚC 3 / 4")

    # Column 1: Điền biểu mẫu số
    add_card(s7, Inches(0.5), Inches(1.6), Inches(6.0), Inches(5.1),
             "📝 4 NỘI DUNG BẮT BUỘC TRONG BÀI LÀM:",
             [
                 "1. Khẩu hiệu hành động (Slogan): Sáng tạo câu khẩu hiệu thể hiện ý chí quyết tâm của nghĩa quân (Ví dụ: 'Cờ đào phấp phới - Quét sạch giặc thù!').",
                 "2. Tóm tắt diễn biến chính: Trình bày súc tích các giai đoạn, địa danh lịch sử quan trọng theo thứ tự thời gian.",
                 "3. Nghệ thuật quân sự tiêu biểu: Nêu rõ chiến thuật độc đáo (Thủy chiến mai phục, Nghi binh lừa giặc, Tác chiến thần tốc bất ngờ...).",
                 "4. Đánh giá vai trò Quang Trung: Khẳng định tài năng lãnh đạo kiệt xuất và tinh thần vì dân vì nước của người anh hùng áo vải."
             ],
             BORDER_GOLD, BG_CARD, GOLD_LIGHT)

    # Column 2: Thử thách giải mật mã
    add_card(s7, Inches(6.8), Inches(1.6), Inches(6.0), Inches(5.1),
             "🔐 THỬ THÁCH ĐẶC BIỆT: 'MẬT MÃ LỊCH SỬ'",
             [
                 "Mỗi nhóm có một câu đố bí ẩn lịch sử độc quyền tích hợp ngay trong giao diện làm bài.",
                 "Cách giải mật mã:\n • Đọc kỹ câu đố bí ẩn gợi ý về địa danh, nhân vật hoặc sự kiện then chốt.\n • Đối chiếu với nguồn sử liệu SGK để tìm ra Từ khóa mật mã chính xác.\n • Nhập từ khóa vào ô 'Đáp án mật mã lịch sử'.",
                 "⭐ Phần thưởng sáng tạo:\n • Nhóm giải đúng mật mã sẽ được cộng điểm trực tiếp vào bảng điểm tổng hợp.\n • Nhận huy hiệu vinh danh 'Nhà Sử Học Xuất Sắc' trên Poster Triển Lãm!"
             ],
             RED_BURGUNDY, BG_CARD, GOLD_BRIGHT)

    add_footer(s7, 7)

    # ==============================================================
    # SLIDE 8: HƯỚNG DẪN BƯỚC 4 - THU ÂM THUYẾT MINH & NỘP BÀI
    # ==============================================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8)
    add_header(s8, "HƯỚNG DẪN THAO TÁC - BƯỚC 4: THU ÂM VOICE & NỘP BÀI", "QUY TRÌNH HỌC TẬP SỐ", "BƯỚC 4 / 4")

    # Left Instructions
    inst4 = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.6), Inches(5.5), Inches(5.1))
    inst4.fill.solid()
    inst4.fill.fore_color.rgb = BG_CARD
    inst4.line.color.rgb = BORDER_GOLD
    inst4.line.width = Pt(1.5)
    tfi4 = inst4.text_frame
    tfi4.word_wrap = True
    tfi4.margin_left = Inches(0.3)
    tfi4.margin_right = Inches(0.3)
    tfi4.margin_top = Inches(0.3)

    p = tfi4.paragraphs[0]
    p.text = "🎙️ CÔNG CỤ THU ÂM TRỰC TIẾP TRÊN WEB:"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_BRIGHT

    steps4 = [
        "1. Chuẩn bị giọng đọc: Cử 1 - 2 bạn đại diện nhóm có giọng đọc diễn cảm, rõ ràng, giàu cảm xúc lịch sử.",
        "2. Cách ghi âm:\n   • Cách 1: Bấm nút 'Bắt đầu thu âm' (Mic) trực tiếp trên giao diện web (thời lượng 60 - 90 giây).\n   • Cách 2: Tải tệp âm thanh ghi âm sẵn từ máy tính (.mp3, .wav).",
        "3. Nghe lại & Tinh chỉnh: Nhấn nút Play để nghe lại đoạn thu âm, kiểm tra âm lượng và độ rõ lời.",
        "4. Bấm nút nộp bài:\n   Nhấn nút to màu đỏ: 'GỬI BÀI CHO GIÁO VIÊN KIỂM DUYỆT' để chuyển giao sản phẩm lên bảng điều khiển sư phạm!"
    ]
    for s in steps4:
        p = tfi4.add_paragraph()
        p.text = s
        p.font.size = Pt(11.5)
        p.font.name = "Arial"
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(8)

    # Right: Screenshot Hinh 3
    img3 = "images/hinh3_thu_am_audio.png"
    if os.path.exists(img3):
        s8.shapes.add_picture(img3, Inches(6.3), Inches(1.6), Inches(6.5), Inches(5.1))

    add_footer(s8, 8)

    # ==============================================================
    # SLIDE 9: KIỂM DUYỆT SƯ PHẠM & XUẤT BẢN POSTER DI SẢN
    # ==============================================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9)
    add_header(s9, "QUY TRÌNH KIỂM DUYỆT CỦA GV & XUẤT BẢN POSTER DI SẢN", "CHUYỂN GIAO SẢN PHẨM HỌC TẬP SỐ", "KIỂM DUYỆT SỐ")

    # Left: Explanation
    inst_mod = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.6), Inches(5.5), Inches(5.1))
    inst_mod.fill.solid()
    inst_mod.fill.fore_color.rgb = BG_CARD
    inst_mod.line.color.rgb = BORDER_GOLD
    inst_mod.line.width = Pt(1.5)
    tfim = inst_mod.text_frame
    tfim.word_wrap = True
    tfim.margin_left = Inches(0.3)
    tfim.margin_right = Inches(0.3)
    tfim.margin_top = Inches(0.3)

    p = tfim.paragraphs[0]
    p.text = "🛡️ VAI TRÒ CỦA GIÁO VIÊN & HỆ THỐNG:"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_BRIGHT

    mod_steps = [
        "1. Trung tâm kiểm duyệt sư phạm:\n   Thầy giáo Nguyễn Đức An theo dõi trực tiếp bài nộp của 4 nhóm trên Bảng điều khiển (Teacher Moderation Dashboard).",
        "2. Đánh giá tính chuẩn xác sử liệu:\n   Thầy kiểm tra sử liệu, chính tả, cách phân tích chiến thuật và chất lượng tệp ghi âm giọng đọc.",
        "3. Phê duyệt & Chuyển đổi số:\n   Khi thầy bấm 'Phê duyệt đạt chuẩn', hệ thống lập tức tự động tổng hợp bài viết và bản ghi âm thành POSTER TRIỂN LÃM DI SẢN tuyệt đẹp tại Tab 2.",
        "4. Tạo mã QR định danh độc quyền:\n   Mỗi Poster được gắn tự động 1 mã QR chuẩn quốc tế ISO/IEC 18004 để phục vụ cho hoạt động tương tác chéo ở Tiết 2!"
    ]
    for ms in mod_steps:
        p = tfim.add_paragraph()
        p.text = ms
        p.font.size = Pt(11.5)
        p.font.name = "Arial"
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(8)

    # Right: Screenshot Hinh 4
    img4 = "images/hinh4_kiem_duyet_gv.png"
    if os.path.exists(img4):
        s9.shapes.add_picture(img4, Inches(6.3), Inches(1.6), Inches(6.5), Inches(5.1))

    add_footer(s9, 9)

    # ==============================================================
    # SLIDE 10: HƯỚNG DẪN TIẾT 2 - BÁO CÁO & QUÉT QR ĐÁNH GIÁ CHÉO
    # ==============================================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10)
    add_header(s10, "TIẾT 2: BÁO CÁO POSTER & QUÉT MÃ QR ĐÁNH GIÁ ĐỒNG ĐẲNG", "TRẢI NGHIỆM ĐỒNG BỘ ĐÁM MÂY REALTIME", "TIẾT 2 (45 PHÚT)")

    # Left Instructions
    inst_peer = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.5), Inches(1.6), Inches(5.5), Inches(5.1))
    inst_peer.fill.solid()
    inst_peer.fill.fore_color.rgb = BG_CARD
    inst_peer.line.color.rgb = BORDER_GOLD
    inst_peer.line.width = Pt(1.5)
    tfip = inst_peer.text_frame
    tfip.word_wrap = True
    tfip.margin_left = Inches(0.3)
    tfip.margin_right = Inches(0.3)
    tfip.margin_top = Inches(0.3)

    p = tfip.paragraphs[0]
    p.text = "🚀 BƯỚC ĐỘT PHÁ TƯƠNG TÁC SỐ:"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.name = "Arial"
    p.font.color.rgb = GOLD_BRIGHT

    peer_steps = [
        "1. Thuyết trình Poster (6 phút/nhóm):\n   Đại diện từng nhóm lên bục điều khiển máy chiếu, giới thiệu Poster và bật phát bản ghi âm thuyết minh hào sảng.",
        "2. Cả lớp quét mã QR bằng điện thoại:\n   Học sinh dưới lớp dùng điện thoại quét mã QR hiển thị ở góc Poster trên màn chiếu để mở thẳng trang tương tác của nhóm đó.",
        "3. Thả tim ❤️ yêu thích:\n   Bấm nút 'Thả Tim' để bình chọn cho Poster ấn tượng và bài thuyết trình xuất sắc.",
        "4. Gửi lời bình luận nhận xét:\n   Viết góp ý, khen ngợi và bấm 'Gửi Lên Màn Chiếu'. Dữ liệu được đồng bộ đám mây (Realtime Cloud Sync) hiển thị công khai ngay sau 2 giây!"
    ]
    for ps in peer_steps:
        p = tfip.add_paragraph()
        p.text = ps
        p.font.size = Pt(11.5)
        p.font.name = "Arial"
        p.font.color.rgb = TEXT_WHITE
        p.space_before = Pt(8)

    # Right: Screenshot Hinh 5
    img5 = "images/hinh5_quet_ma_qr.png"
    if os.path.exists(img5):
        s10.shapes.add_picture(img5, Inches(6.3), Inches(1.6), Inches(6.5), Inches(5.1))

    add_footer(s10, 10)

    # ==============================================================
    # SLIDE 11: TIÊU CHÍ ĐÁNH GIÁ & RUBRIC CHẤM ĐIỂM
    # ==============================================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s11)
    add_header(s11, "TIÊU CHÍ ĐÁNH GIÁ & BẢNG ĐIỂM RUBRIC SƯ PHẠM", "ĐÁNH GIÁ QUÁ TRÌNH & ĐỒNG ĐẲNG", "THANG ĐIỂM 10")

    # 4 Criteria Cards in a 2x2 grid
    add_card(s11, Inches(0.5), Inches(1.6), Inches(5.9), Inches(2.45),
             "1. TÍNH CHUẨN XÁC SỬ LIỆU (3.0 ĐIỂM)",
             [
                 "Tái hiện chính xác bối cảnh lịch sử, thời gian và địa bàn then chốt.",
                 "Nêu bật được các diễn biến cốt lõi, không sai lệch số liệu lịch sử.",
                 "Khai thác hiệu quả nguồn sử liệu SGK Kết nối tri thức và lược đồ số.",
                 "Đánh giá khách quan, sâu sắc về vai trò của lãnh tụ Quang Trung."
             ],
             BORDER_GOLD, BG_CARD, GOLD_BRIGHT)

    add_card(s11, Inches(6.9), Inches(1.6), Inches(5.9), Inches(2.45),
             "2. GIẢI MẬT MÃ & NGHỆ THUẬT QUÂN SỰ (2.5 ĐIỂM)",
             [
                 "Giải chính xác câu đố bí ẩn lịch sử và tìm đúng Từ khóa mật mã.",
                 "Phân tích sắc bén nét độc đáo trong nghệ thuật tác chiến Tây Sơn.",
                 "Nêu bật yếu tố bất ngờ, mai phục, nghi binh, thần tốc trong từng chiến dịch.",
                 "Khẩu hiệu hành động (Slogan) mang tính sáng tạo và cảm hứng thời đại."
             ],
             RED_BURGUNDY, BG_CARD, GOLD_LIGHT)

    add_card(s11, Inches(0.5), Inches(4.3), Inches(5.9), Inches(2.45),
             "3. THUYẾT MINH & CHẤT LƯỢNG ÂM THANH (2.5 ĐIỂM)",
             [
                 "Bản thu âm rõ ràng, không bị rè hoặc lẫn nhiều tạp âm môi trường.",
                 "Giọng đọc truyền cảm, hào sảng, đúng tinh thần sử thi Tây Sơn.",
                 "Poster trình bày trang trọng, bố cục hài hòa hoa văn Trống đồng.",
                 "Phối hợp nhịp nhàng giữa trình chiếu Poster và âm thanh minh họa."
             ],
             BLUE_ACCENT, BG_CARD, GOLD_LIGHT)

    add_card(s11, Inches(6.9), Inches(4.3), Inches(5.9), Inches(2.45),
             "4. THUYẾT TRÌNH & ĐÁNH GIÁ ĐỒNG ĐẲNG (2.0 ĐIỂM)",
             [
                 "Báo cáo viên tự tin, mạch lạc, làm chủ thời gian quy định (6 phút/nhóm).",
                 "Khả năng phản biện, trả lời lưu loát các câu hỏi gợi mở từ thầy cô và bạn học.",
                 "Nhận được nhiều lượt thả tim ❤️ và đánh giá tích cực từ cả lớp qua mã QR.",
                 "Tinh thần đoàn kết, hỗ trợ lẫn nhau của các thành viên trong nhóm."
             ],
             GREEN_ACCENT, BG_CARD, GOLD_BRIGHT)

    add_footer(s11, 11)

    # ==============================================================
    # SLIDE 12: TỔNG KẾT & THÔNG ĐIỆP KỶ NGUYÊN SỐ
    # ==============================================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s12)
    add_header(s12, "TỔNG KẾT BÀI HỌC & THÔNG ĐIỆP KỶ NGUYÊN SỐ", "Ý NGHĨA LỊCH SỬ & LIÊN HỆ", "THÔNG ĐIỆP")

    # Left: Historical Significance
    add_card(s12, Inches(0.5), Inches(1.6), Inches(6.0), Inches(5.1),
             "🌟 Ý NGHĨA LỊCH SỬ PHONG TRÀO TÂY SƠN:",
             [
                 "1. Đập tan các tập đoàn phong kiến cát cứ: Lật đổ Nguyễn ở Đàng Trong, Trịnh - Lê ở Đàng Ngoài, chấm dứt tình trạng chia cắt giang sơn hơn 200 năm.",
                 "2. Bảo vệ vững chắc độc lập chủ quyền: Đánh tan 5 vạn quân xâm lược Xiêm (1785) và đại phá 29 vạn quân Mãn Thanh (1789), lập nên những trang sử vàng chói lọi.",
                 "3. Tôn vinh thiên tài quân sự Quang Trung: Người anh hùng bách chiến bách thắng, biểu tượng sáng ngời của tinh thần quyết chiến quyết thắng và lòng yêu nước nồng nàn.",
                 "4. Để lại bài học quý báu: Lấy dân làm gốc, phát huy sức mạnh khối đại đoàn kết toàn dân tộc và nghệ thuật tác chiến thần tốc bất ngờ."
             ],
             BORDER_GOLD, BG_CARD, GOLD_BRIGHT)

    # Right: Message for Digital Era
    add_card(s12, Inches(6.8), Inches(1.6), Inches(6.0), Inches(5.1),
             "🚀 THÔNG ĐIỆP CHO HỌC SINH THỜI ĐẠI 4.0:",
             [
                 "Kế thừa hào khí hào hùng: Mỗi học sinh hôm nay hãy tự hào về truyền thống bất khuất của cha ông, biến niềm tự hào thành động lực học tập và rèn luyện.",
                 "Làm chủ công nghệ số: Tích cực ứng dụng học liệu số, chuyển đổi số trong học tập để khám phá kho tàng tri thức lịch sử vô tận của dân tộc.",
                 "Lan tỏa giá trị di sản: Chung tay gìn giữ và quảng bá các di sản lịch sử hào hùng trên không gian mạng một cách văn minh, sáng tạo.",
                 "--------------------------------------------------",
                 "CHÚC CÁC NHÓM CÓ MỘT TIẾT HỌC THÀNH CÔNG VÀ TRẢI NGHIỆM ĐẦY CẢM HỨNG!",
                 "Thầy giáo: Nguyễn Đức An - Trường TH - THCS Nguyễn Quốc Phú"
             ],
             RED_BURGUNDY, BG_CARD, GOLD_LIGHT)

    add_footer(s12, 12)

    # Save to both locations
    path1 = "docs/ho_so_hoi_thi/Folder_2_Ke_hoach_day_hoc/Slide_Trinh_Chieu_Huong_Dan_Hoc_Tap_So_Bai_8_Tay_Son.pptx"
    path2 = "docs/Slide_Trinh_Chieu_Huong_Dan_Hoc_Tap_So_Bai_8_Tay_Son.pptx"
    
    os.makedirs(os.path.dirname(path1), exist_ok=True)
    prs.save(path1)
    prs.save(path2)
    print(f"Presentation saved successfully to:\n1. {path1}\n2. {path2}")

if __name__ == "__main__":
    create_deck()
