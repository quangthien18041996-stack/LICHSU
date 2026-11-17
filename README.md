# DỰ ÁN DẠY HỌC SỐ & KHÔNG GIAN BẢO TÀNG LỊCH SỬ 8
## CHỦ ĐỀ: PHONG TRÀO TÂY SƠN (1771 - 1789)
**Sản phẩm dự thi: "Chủ Đề Dạy Học Số / STEM Cấp Thành Phố Năm Học 2026 - 2027"**

---

### 🌐 Trải nghiệm Trực tuyến (Live Production)
👉 **Vercel Live:** [https://lichsu-eight.vercel.app/](https://lichsu-eight.vercel.app/)  
👉 **GitHub Mirror:** [https://quangthien18041996-stack.github.io/LICHSU/](https://quangthien18041996-stack.github.io/LICHSU/)

---

### 🏛️ Các Tính Năng Nổi Bật Của Hệ Thống

1. **Cổng Học Liệu Số & Lời Hiệu Triệu Ba Quân (Portal):**
   - Rạp chiếu 3D sử thi nổi (`Cinematic 3D Theater`) với 10 đại cảnh chuyển luân phiên theo âm nhạc hào hùng.
   - Trực tiếp lắng nghe giọng đọc hào khí *Lời Hiệu Triệu của Hoàng Đế Quang Trung*.
   - Khúc nhạc chủ đề *Hào Khí Việt Nam*.

2. **Không Gian Làm Việc 4 Nhóm Học Sinh (Workspaces):**
   - **Nhóm 1:** Lật đổ chúa Nguyễn ở Đàng Trong (1771 - 1777).
   - **Nhóm 2:** Đại phá 5 vạn quân Xiêm - Trận Rạch Gầm - Xoài Mút (1785).
   - **Nhóm 3:** Tiến quân ra Bắc Hà lật đổ chúa Trịnh - vua Lê, thống nhất non sông (1786 - 1788).
   - **Nhóm 4:** Mùa xuân Kỷ Dậu 1789 - Hoàng đế Quang Trung đại phá 29 vạn quân Mãn Thanh.
   - Tích hợp công cụ thu âm trực tiếp / tải file ghi âm thuyết minh thuyết trình.
   - Hệ thống chốt kiến thức và tạo Poster Triển Lãm & Mã QR tự động (1-Click Finalize).

3. **Phòng Triển Lãm Di Sản Số & Thách Thức Sử Liệu (Gallery & Timeline):**
   - 4 Poster triển lãm độc bản với khung viền hoa văn **Trống đồng Đông Sơn hoàng kim** và cờ lệnh Tây Sơn viền lửa.
   - Tích hợp nút nghe **Giọng đọc thuyết minh truyền cảm** cho từng chiến dịch.
   - Tính năng **Bí Ẩn Sử Liệu & Thách Thức Nhanh** riêng biệt cho từng nhóm (hiển thị câu hỏi thử thách tư duy và giải mã sử học chuẩn SGK Kết nối tri thức).
   - Hệ thống đánh giá đồng đẳng (Peer Review): Chấm điểm, thả tim realtime, quét mã QR điện thoại để tương tác và góp ý nhận xét giữa các nhóm.

4. **Hệ Thống Báo Cáo & Trình Chiếu Toàn Màn Hình (Presentation Suite):**
   - Chế độ Cinema Presentation hỗ trợ giáo viên và học sinh thuyết trình báo cáo sản phẩm trước lớp học ở Tiết 2.

5. **Bảng Điều Khiển Của Giáo Viên & Quy Trình Kiểm Duyệt (Teacher Moderation Dashboard):**
   - Quy trình sư phạm chặt chẽ: Học sinh nộp bài -> Giáo viên kiểm duyệt nội dung -> Bài xuất bản lên Phòng triển lãm & Dòng thời gian.
   - Quản lý tiến độ nộp bài của 4 nhóm, duyệt/yêu cầu chỉnh sửa, chấm điểm và xuất báo cáo tổng hợp.

---

### 📁 Cấu Trúc Thư Mục Chuẩn Hóa

```text
LICHSU/
├── index.html                  # Ứng dụng web tương tác chính (Single Page Application)
├── vercel.json                 # Cấu hình triển khai Serverless trên nền tảng Vercel
├── README.md                   # Hướng dẫn và tài liệu dự án
├── .gitignore                  # Cấu hình bỏ qua các tệp tin tạm và tệp nhị phân
│
├── api/                        # Serverless Functions (Backend API)
│   └── interactions.js         # API lưu trữ và đồng bộ Thả tim & Bình luận theo thời gian thực
│
├── docs/                       # Hồ sơ dự thi & Kế hoạch bài dạy
│   ├── ke_hoach_bai_day/       # Giáo án chuẩn theo Công văn 5512 (SGK Kết nối tri thức)
│   │   ├── Ke_Hoach_Bai_Day_Lich_Su_8_Phong_Trao_Tay_Son_Chuan_2_Tiet.docx
│   │   ├── KE_HOACH_BAI_DAY_LICH_SU_8_PHONG_TRAO_TAY_SON.md
│   │   ├── Phu_luc_4_Mau_Ke_hoach_bai_day_2020_c19a327da9.pdf
│   │   └── archive/            # Các bản nháp giáo án cũ
│   ├── ho_so_hoi_thi/          # Văn bản & thuyết minh dự án dự thi cấp Thành phố
│   │   ├── 12070kh-hoi-thi-thiet-ke-chu-de-tich-hop-stem-day-hoc-so-2026-2027 (1).pdf
│   │   └── BAN_DEMO_GIAI_PHAP_DAY_HOC_SO_LICH_SU_8.docx
│   └── tu_lieu_tham_khao/      # Sách giáo khoa & tư liệu video minh họa
│       ├── SGK Lịch sử và Địa lí 8-mau_removed.pdf
│       └── 1794588284880_1568779380718944690_7339907267052087467.mp4
│
├── images/                     # Kho tài nguyên hình ảnh & âm thanh sử thi
│   ├── hero_slide_1.jpg ...    # 10 bức tranh đại cảnh lịch sử sử thi 4K
│   ├── luoc_do_*.jpg           # Lược đồ các chiến dịch lớn (Căn cứ, Rạch Gầm, Ngọc Hồi)
│   ├── giong_quang_trung.mp3   # Lời hiệu triệu Hoàng đế Quang Trung
│   ├── hao_khi_viet_nam.mp3    # Ca khúc hào khí chủ đề
│   └── poster_audio_*.mp3      # Âm thanh thuyết minh mẫu cho 4 nhóm
│
└── scripts/                    # Công cụ tự động hóa & mã nguồn hỗ trợ phát triển
    ├── build_upgrade.py        # Kịch bản nâng cấp & đồng bộ giao diện
    ├── fix_interactive_features.py
    ├── inject_quang_trung_voice.py
    ├── qrcode.min.js
    └── archive/                # Bản sao lưu mã nguồn cũ
```
