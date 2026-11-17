# -*- coding: utf-8 -*-
"""
Fix script to cleanly integrate all 4 interactive features into index.html
without any duplication, with inline pointer-events:none on canvases,
and strictly targeting only the final main <script> tag.
"""

with open("index.html.bak", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Canvas Overlays right after <body> with explicit pointer-events: none !important
canvas_code = '''
    <!-- CINEMATIC CANVAS OVERLAYS (STRICTLY NON-BLOCKING) -->
    <canvas id="ember-canvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none !important; z-index: 10;"></canvas>
    <canvas id="confetti-canvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none !important; z-index: 100; display: none;"></canvas>
'''

html = html.replace('<body class="min-h-screen flex flex-col hero-pattern">', 
                    '<body class="min-h-screen flex flex-col hero-pattern">' + canvas_code, 1)

# 2. Update Top Announcement Bar
top_bar_old = '''    <!-- TOP ANNOUNCEMENT BAR -->
    <div class="bg-gradient-to-r from-red-950 via-red-900 to-amber-950 text-amber-200 text-xs py-2 px-4 border-b border-amber-700/40 text-center flex items-center justify-center">
        <div class="flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-500/20 text-amber-300 font-semibold px-2 py-0.5 rounded border border-amber-500/40">HỘI THI DẠY HỌC SỐ - STEM 2026 - 2027</span>
            <span class="hidden md:inline">|</span>
            <span class="font-medium">Chủ đề: "Phong trào Tây Sơn và Thiên tài quân sự Quang Trung" - Lịch sử & Địa lí 8 (Bài 8)</span>
        </div>
    </div>'''

top_bar_new = '''    <!-- TOP ANNOUNCEMENT BAR -->
    <div class="relative z-50 bg-gradient-to-r from-red-950 via-red-900 to-amber-950 text-amber-200 text-xs py-2 px-4 border-b border-amber-700/40 flex flex-wrap items-center justify-between gap-3 shadow-md">
        <div class="flex flex-wrap items-center gap-2">
            <span class="bg-amber-500/20 text-amber-300 font-semibold px-2.5 py-0.5 rounded-full border border-amber-500/40 flex items-center gap-1.5">
                <span class="w-1.5 h-1.5 rounded-full bg-amber-400 animate-ping"></span>
                HỘI THI DẠY HỌC SỐ - STEM 2026 - 2027
            </span>
            <span class="hidden md:inline text-amber-600">|</span>
            <span class="font-medium text-amber-100/90 hidden sm:inline">Chủ đề: "Phong trào Tây Sơn & Thiên tài quân sự Quang Trung" - Lịch sử 8</span>
        </div>
        <div class="flex items-center gap-2">
            <!-- Nút bật/tắt Trống trận Tây Sơn -->
            <button type="button" onclick="toggleBattleDrums()" id="btn-battle-drums" class="cursor-pointer px-2.5 py-1 rounded-lg bg-stone-900/90 hover:bg-red-950 border border-amber-500/40 text-amber-300 font-bold text-[11px] flex items-center gap-1.5 transition shadow" title="Bật/Tắt tiếng trống trận Tây Sơn hào hùng">
                <i class="fa-solid fa-drum text-amber-400"></i>
                <span>Trống Trận:</span>
                <span id="battle-drums-status" class="text-amber-200 font-bold">Bật</span>
            </button>
            <!-- Nút nghe Lời hiểu dụ -->
            <button type="button" onclick="playQuangTrungSpeech()" class="cursor-pointer px-2.5 py-1 rounded-lg bg-stone-900/90 hover:bg-amber-950 border border-amber-500/40 text-amber-300 font-bold text-[11px] flex items-center gap-1.5 transition shadow" title="Nghe diễn đọc hào hùng Lời Hiểu Dụ của Hoàng đế Quang Trung">
                <i class="fa-solid fa-bullhorn text-amber-400"></i>
                <span class="hidden sm:inline">Lời Dụ Quang Trung</span>
            </button>
            <!-- Nút bật/tắt Tàn lửa -->
            <button type="button" onclick="toggleEmberEffect()" id="btn-toggle-ember" class="cursor-pointer px-2 py-1 rounded-lg bg-stone-900/90 hover:bg-stone-800 border border-amber-500/40 text-amber-300 text-[11px] transition" title="Bật/Tắt hiệu ứng tàn lửa chiến trận">
                <i class="fa-solid fa-fire text-amber-400"></i>
                <span class="hidden sm:inline">Tàn Lửa:</span>
                <span id="lbl-ember-state" class="text-amber-300 font-bold">Bật</span>
            </button>
        </div>
    </div>'''

html = html.replace(top_bar_old, top_bar_new, 1)

# 3. Main Navbar Enhancements
nav_end_old = '</nav>'
nav_quick_actions = '''</nav>
            <!-- Quick Feature Actions -->
            <div class="hidden lg:flex items-center gap-2.5">
                <button type="button" onclick="openArenaQuizModal()" class="cursor-pointer px-3.5 py-2 rounded-xl bg-gradient-to-r from-red-800 via-amber-700 to-amber-600 hover:from-red-700 hover:to-amber-500 text-yellow-100 font-bold text-xs flex items-center gap-2 shadow-lg shadow-amber-900/40 border border-yellow-400/50 transition transform hover:scale-105" title="Đấu trường thử tài chiến lược 60 giây">
                    <i class="fa-solid fa-bolt text-yellow-300 animate-pulse"></i> Đấu Trường 60s
                </button>
                <button type="button" onclick="openPresentationSuite(1)" class="cursor-pointer px-3.5 py-2 rounded-xl bg-stone-900/90 hover:bg-stone-800 text-amber-300 font-bold text-xs flex items-center gap-2 border border-amber-500/50 transition hover:shadow-lg hover:shadow-amber-900/30" title="Chế độ Trình chiếu Báo cáo màn hình lớn / Máy chiếu">
                    <i class="fa-solid fa-tv text-amber-400"></i> Trình Chiếu
                </button>
            </div>'''

html = html.replace(nav_end_old, nav_quick_actions, 1)

# Mobile navbar additions
mobile_nav_end = '<button onclick="switchTab(\'qr-hub\')" class="mobile-nav-btn px-3 py-1.5 rounded-lg whitespace-nowrap font-medium text-stone-400">Mã QR</button>'
mobile_nav_extra = '''<button onclick="switchTab('qr-hub')" class="mobile-nav-btn px-3 py-1.5 rounded-lg whitespace-nowrap font-medium text-stone-400">Mã QR</button>
            <button type="button" onclick="openArenaQuizModal()" class="cursor-pointer mobile-nav-btn px-3 py-1.5 rounded-lg whitespace-nowrap font-bold text-yellow-300 bg-red-950/80 border border-amber-500/40"><i class="fa-solid fa-bolt mr-1"></i>Đấu Trường 60s</button>
            <button type="button" onclick="openPresentationSuite(1)" class="cursor-pointer mobile-nav-btn px-3 py-1.5 rounded-lg whitespace-nowrap font-bold text-amber-300 bg-stone-800"><i class="fa-solid fa-tv mr-1"></i>Trình Chiếu</button>'''

html = html.replace(mobile_nav_end, mobile_nav_extra, 1)

# 4. Enhance Hero Banner Quote & CTA Actions
hero_quote_old = '''                        <!-- Lời dụ Quang Trung -->
                        <div class="p-4 sm:p-5 rounded-2xl bg-gradient-to-r from-black/80 to-amber-950/40 border-l-4 border-amber-500 border-t border-b border-r border-amber-500/20 text-amber-200/90 text-sm italic font-serif space-y-1.5 shadow-lg">
                            <p class="font-bold text-amber-300 uppercase not-italic font-sans text-xs flex items-center gap-2 tracking-wider">
                                <i class="fa-solid fa-quote-left text-amber-400"></i> Lời hiểu dụ của Hoàng đế Quang Trung trước ba quân (1788):
                            </p>
                            <p class="leading-relaxed">“Đánh cho để dài tóc / Đánh cho để đen răng / Đánh cho nó chích luân bất phản / Đánh cho nó phiến giáp bất hoàn / Đánh cho sử tri Nam quốc anh hùng chi hữu chủ!”</p>
                        </div>'''

hero_quote_new = '''                        <!-- Lời dụ Quang Trung -->
                        <div id="hero-quote-container" class="p-4 sm:p-5 rounded-2xl bg-gradient-to-r from-black/80 to-amber-950/40 border-l-4 border-amber-500 border-t border-b border-r border-amber-500/20 text-amber-200/90 text-sm italic font-serif space-y-2 shadow-lg transition-all duration-500">
                            <div class="flex items-center justify-between">
                                <p class="font-bold text-amber-300 uppercase not-italic font-sans text-xs flex items-center gap-2 tracking-wider">
                                    <i class="fa-solid fa-quote-left text-amber-400"></i> Lời hiểu dụ của Hoàng đế Quang Trung trước ba quân (1788):
                                </p>
                                <button type="button" onclick="playQuangTrungSpeech()" class="cursor-pointer px-2.5 py-1 rounded-lg bg-amber-500/20 hover:bg-amber-500/40 text-amber-300 text-xs font-bold border border-amber-500/40 transition flex items-center gap-1.5 not-italic font-sans">
                                    <i class="fa-solid fa-volume-high text-amber-400"></i> Nghe Giọng Đọc
                                </button>
                            </div>
                            <p id="hero-quote-text" class="leading-relaxed text-amber-100/95 font-serif text-sm sm:text-base">“Đánh cho để dài tóc / Đánh cho để đen răng / Đánh cho nó chích luân bất phản / Đánh cho nó phiến giáp bất hoàn / Đánh cho sử tri Nam quốc anh hùng chi hữu chủ!”</p>
                        </div>'''

html = html.replace(hero_quote_old, hero_quote_new, 1)

hero_cta_old = '''                        <!-- CTA Actions -->
                        <div class="flex flex-wrap items-center gap-3.5 pt-2">
                            <button onclick="switchTab('workspaces')" class="px-6 py-3 rounded-xl bg-gradient-to-r from-amber-600 via-amber-500 to-yellow-500 text-stone-950 font-black text-sm uppercase tracking-wider flex items-center gap-2 hover:shadow-xl hover:shadow-amber-500/40 transition transform hover:-translate-y-0.5 border border-yellow-300/40">
                                <i class="fa-solid fa-users text-base"></i> Vào Không Gian 4 Nhóm
                            </button>
                            <button onclick="switchTab('qr-hub')" class="px-6 py-3 rounded-xl bg-stone-900/90 hover:bg-stone-800 text-amber-300 border border-amber-500/50 font-bold text-sm flex items-center gap-2 transition hover:shadow-lg hover:shadow-amber-500/20">
                                <i class="fa-solid fa-qrcode text-base"></i> Quét Mã QR Trải Nghiệm
                            </button>
                        </div>'''

hero_cta_new = '''                        <!-- CTA Actions -->
                        <div class="flex flex-wrap items-center gap-3 pt-2">
                            <button type="button" onclick="switchTab('workspaces')" class="cursor-pointer px-5 py-3 rounded-xl bg-gradient-to-r from-amber-600 via-amber-500 to-yellow-500 text-stone-950 font-black text-sm uppercase tracking-wider flex items-center gap-2 hover:shadow-xl hover:shadow-amber-500/40 transition transform hover:-translate-y-0.5 border border-yellow-300/40">
                                <i class="fa-solid fa-users text-base"></i> Vào 4 Nhóm
                            </button>
                            <button type="button" onclick="scrollToWarMap()" class="cursor-pointer px-5 py-3 rounded-xl bg-gradient-to-r from-red-950 to-stone-900 hover:bg-red-900 text-amber-300 border border-amber-500/60 font-bold text-sm flex items-center gap-2 transition hover:shadow-lg hover:shadow-red-900/40">
                                <i class="fa-solid fa-map-location-dot text-amber-400"></i> Sa Bàn Hành Quân
                            </button>
                            <button type="button" onclick="openArenaQuizModal()" class="cursor-pointer px-5 py-3 rounded-xl bg-gradient-to-r from-yellow-600/30 to-amber-900/40 hover:bg-amber-900/60 text-yellow-300 border border-yellow-500/50 font-bold text-sm flex items-center gap-2 transition">
                                <i class="fa-solid fa-bolt text-yellow-400 animate-pulse"></i> Thử Tài 60s
                            </button>
                            <button type="button" onclick="openPresentationSuite(1)" class="cursor-pointer px-4 py-3 rounded-xl bg-stone-900/80 hover:bg-stone-800 text-stone-300 border border-stone-700 font-semibold text-sm flex items-center gap-2 transition">
                                <i class="fa-solid fa-tv text-amber-400"></i> Trình Chiếu
                            </button>
                        </div>'''

html = html.replace(hero_cta_old, hero_cta_new, 1)

# 5. Inject Sa Bàn Chiến Lược right before 4 Mission Cards
war_map_html = '''
            <!-- ========================================== -->
            <!-- SA BÀN CHIẾN LƯỢC: 5 CHẶNG HÀNH QUÂN THẦN TỐC (1788 - 1789) -->
            <!-- ========================================== -->
            <div id="interactive-war-map" class="relative rounded-3xl p-6 sm:p-8 border-2 border-amber-500/70 bg-gradient-to-b from-[#1a0f0d] via-[#120a08] to-[#0a0706] shadow-[0_20px_50px_rgba(0,0,0,0.85)] overflow-hidden">
                <!-- Background Ambient War Motif -->
                <div class="absolute -right-20 -bottom-20 w-96 h-96 bg-red-950/20 rounded-full blur-3xl pointer-events-none"></div>

                <div class="flex flex-wrap items-center justify-between gap-4 pb-6 border-b border-amber-800/40 relative z-10">
                    <div>
                        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-red-950/90 border border-red-500/60 text-red-300 text-xs font-bold uppercase tracking-wider">
                            <span class="w-2 h-2 rounded-full bg-red-500 animate-ping"></span>
                            <i class="fa-solid fa-map-location-dot text-amber-400"></i> Sa Bàn Tác Chiến Động
                        </div>
                        <h3 class="text-xl sm:text-2xl lg:text-3xl font-black font-cinzel text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-yellow-400 to-amber-500 mt-2">
                            5 Chặng Hành Quân Thần Tốc & Đại Thắng Kỷ Dậu (1788 - 1789)
                        </h3>
                        <p class="text-xs sm:text-sm text-stone-300 mt-1">
                            Bấm vào từng chặng để phân tích thiên tài nghệ thuật quân sự của Hoàng đế Quang Trung
                        </p>
                    </div>
                    <div class="flex items-center gap-3">
                        <button type="button" onclick="autoPlayWarJourney()" id="btn-autoplay-journey" class="cursor-pointer px-4 py-2.5 rounded-xl bg-gradient-to-r from-amber-600 to-yellow-500 hover:from-amber-500 hover:to-yellow-400 text-stone-950 font-black text-xs sm:text-sm flex items-center gap-2 shadow-lg shadow-amber-900/50 transition transform hover:scale-105">
                            <i class="fa-solid fa-play" id="icon-autoplay"></i> <span id="lbl-autoplay">Diễn Tập Tự Động</span>
                        </button>
                    </div>
                </div>

                <!-- 5 Steps Horizontal Stepper Tracker -->
                <div class="py-6 relative z-10">
                    <div class="grid grid-cols-2 sm:grid-cols-5 gap-3">
                        <!-- Step 1 -->
                        <button type="button" onclick="selectWarStep(0)" id="war-step-btn-0" class="cursor-pointer war-step-btn p-3 rounded-2xl border-2 border-amber-400 bg-amber-950 text-left transition transform hover:-translate-y-1 shadow-xl">
                            <div class="flex items-center justify-between text-[11px] font-bold text-amber-300 mb-1">
                                <span>CHẶNG 1</span>
                                <span class="w-5 h-5 rounded-full bg-amber-500 text-stone-950 flex items-center justify-center text-[10px] font-black">1</span>
                            </div>
                            <h5 class="text-xs sm:text-sm font-bold text-stone-100">Núi Bân (Phú Xuân)</h5>
                            <p class="text-[11px] text-amber-300/80 font-mono mt-0.5">22/12/1788</p>
                            <span class="inline-block mt-2 text-[10px] px-2 py-0.5 rounded bg-black/60 text-amber-200 border border-amber-500/30">Lên ngôi & Xuất quân</span>
                        </button>

                        <!-- Step 2 -->
                        <button type="button" onclick="selectWarStep(1)" id="war-step-btn-1" class="cursor-pointer war-step-btn p-3 rounded-2xl border border-stone-800 bg-stone-900/60 hover:bg-stone-800 text-left transition transform hover:-translate-y-1">
                            <div class="flex items-center justify-between text-[11px] font-bold text-stone-400 mb-1">
                                <span>CHẶNG 2</span>
                                <span class="w-5 h-5 rounded-full bg-stone-800 text-stone-300 flex items-center justify-center text-[10px] font-black">2</span>
                            </div>
                            <h5 class="text-xs sm:text-sm font-bold text-stone-200">Nghệ An - Tam Điệp</h5>
                            <p class="text-[11px] text-stone-400 font-mono mt-0.5">15 tháng Chạp</p>
                            <span class="inline-block mt-2 text-[10px] px-2 py-0.5 rounded bg-black/60 text-stone-400 border border-stone-700/50">Duyệt binh & Ăn Tết</span>
                        </button>

                        <!-- Step 3 -->
                        <button type="button" onclick="selectWarStep(2)" id="war-step-btn-2" class="cursor-pointer war-step-btn p-3 rounded-2xl border border-stone-800 bg-stone-900/60 hover:bg-stone-800 text-left transition transform hover:-translate-y-1">
                            <div class="flex items-center justify-between text-[11px] font-bold text-stone-400 mb-1">
                                <span>CHẶNG 3</span>
                                <span class="w-5 h-5 rounded-full bg-stone-800 text-stone-300 flex items-center justify-center text-[10px] font-black">3</span>
                            </div>
                            <h5 class="text-xs sm:text-sm font-bold text-stone-200">Tiền đồn Gián Khẩu</h5>
                            <p class="text-[11px] text-stone-400 font-mono mt-0.5">Đêm 30 Tết</p>
                            <span class="inline-block mt-2 text-[10px] px-2 py-0.5 rounded bg-black/60 text-stone-400 border border-stone-700/50">Tuyệt mật chớp nhoáng</span>
                        </button>

                        <!-- Step 4 -->
                        <button type="button" onclick="selectWarStep(3)" id="war-step-btn-3" class="cursor-pointer war-step-btn p-3 rounded-2xl border border-stone-800 bg-stone-900/60 hover:bg-stone-800 text-left transition transform hover:-translate-y-1">
                            <div class="flex items-center justify-between text-[11px] font-bold text-stone-400 mb-1">
                                <span>CHẶNG 4</span>
                                <span class="w-5 h-5 rounded-full bg-stone-800 text-stone-300 flex items-center justify-center text-[10px] font-black">4</span>
                            </div>
                            <h5 class="text-xs sm:text-sm font-bold text-stone-200">Đồn Hà Hồi</h5>
                            <p class="text-[11px] text-stone-400 font-mono mt-0.5">Đêm mùng 3 Tết</p>
                            <span class="inline-block mt-2 text-[10px] px-2 py-0.5 rounded bg-black/60 text-stone-400 border border-stone-700/50">Tâm lý chiến bức hàng</span>
                        </button>

                        <!-- Step 5 -->
                        <button type="button" onclick="selectWarStep(4)" id="war-step-btn-4" class="cursor-pointer war-step-btn p-3 rounded-2xl border border-stone-800 bg-stone-900/60 hover:bg-stone-800 text-left transition transform hover:-translate-y-1 col-span-2 sm:col-span-1">
                            <div class="flex items-center justify-between text-[11px] font-bold text-stone-400 mb-1">
                                <span>CHẶNG 5 (ĐỈNH CAO)</span>
                                <span class="w-5 h-5 rounded-full bg-stone-800 text-stone-300 flex items-center justify-center text-[10px] font-black">5</span>
                            </div>
                            <h5 class="text-xs sm:text-sm font-bold text-stone-200">Ngọc Hồi - Đống Đa</h5>
                            <p class="text-[11px] text-stone-400 font-mono mt-0.5">Mùng 5 Tết Kỷ Dậu</p>
                            <span class="inline-block mt-2 text-[10px] px-2 py-0.5 rounded bg-black/60 text-stone-400 border border-stone-700/50">Giải phóng Thăng Long</span>
                        </button>
                    </div>
                </div>

                <!-- Active Step Detail Card -->
                <div id="war-step-detail-card" class="rounded-2xl bg-black/70 border border-amber-600/50 p-6 sm:p-8 relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                    <!-- Left: Tactical Description & Analysis -->
                    <div class="lg:col-span-7 space-y-4">
                        <div class="flex flex-wrap items-center gap-2.5">
                            <span id="step-badge-phase" class="text-xs px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/40 font-bold uppercase">
                                KHỞI ĐẦU CHIẾN DỊCH
                            </span>
                            <span id="step-date" class="text-xs text-stone-300 font-mono bg-stone-900 px-2.5 py-1 rounded border border-stone-800">
                                22/12/1788 (25 tháng 11 năm Mậu Thân)
                            </span>
                        </div>

                        <h4 id="step-title" class="text-xl sm:text-2xl font-black text-amber-200 font-serif">
                            Lễ Đăng Quang Tại Núi Bân & Phát Lệnh Xuất Quân Thần Tốc
                        </h4>

                        <div id="step-quote" class="p-3.5 rounded-xl bg-gradient-to-r from-red-950/60 to-black/80 border-l-4 border-amber-500 text-xs sm:text-sm italic text-amber-100/90 font-serif">
                            “Trẫm nay ứng mệnh trời, thuận lòng người, lên ngôi Hoàng đế để dẹp yên giặc giã, giữ yên bờ cõi!”
                        </div>

                        <div class="space-y-2 text-xs sm:text-sm text-stone-300 leading-relaxed">
                            <p id="step-desc-1">
                                Nhận được tin cấp báo 29 vạn quân Mãn Thanh do Tôn Sĩ Nghị chỉ huy tràn vào chiếm đóng Thăng Long, Nguyễn Huệ lập đàn tế trời tại núi Bân (Phú Xuân - Huế), chính thức lên ngôi Hoàng đế, lấy niên hiệu Quang Trung.
                            </p>
                            <p id="step-desc-2">
                                <strong class="text-amber-400">Nghệ thuật quân sự:</strong> Việc lên ngôi xưng đế trước khi xuất quân có ý nghĩa lịch sử to lớn: danh chính ngôn thuận quy tụ lòng dân cả nước, chấm dứt tình trạng cát cứ, đồng thời mở đầu cuộc hành quân thần tốc ra Bắc với tốc độ hành tiến vô tiền khoáng hậu.
                            </p>
                        </div>

                        <div class="pt-3 border-t border-stone-800 flex flex-wrap items-center gap-4 text-xs">
                            <div class="flex items-center gap-2 text-stone-300">
                                <i class="fa-solid fa-users text-amber-400"></i>
                                <span>Lực lượng: <strong id="step-troops" class="text-amber-300 font-bold">6 vạn quân ban đầu</strong></span>
                            </div>
                            <div class="flex items-center gap-2 text-stone-300">
                                <i class="fa-solid fa-chess-knight text-amber-400"></i>
                                <span>Kế sách: <strong id="step-strategy" class="text-amber-300 font-bold">Thần tốc, bất ngờ, nhân tâm</strong></span>
                            </div>
                            <button type="button" onclick="playBassDrum(120, 0.6, 1.0); setTimeout(() => playChiengDong(440, 2, 0.4), 100);" class="cursor-pointer ml-auto px-3 py-1.5 rounded-lg bg-red-950/80 hover:bg-red-900 border border-amber-500/50 text-amber-300 font-bold flex items-center gap-1.5">
                                <i class="fa-solid fa-drum text-amber-400"></i> Hiệu lệnh trống
                            </button>
                        </div>
                    </div>

                    <!-- Right: Visual Map / Artwork Representation -->
                    <div class="lg:col-span-5">
                        <div class="relative rounded-2xl overflow-hidden border-2 border-amber-500/60 shadow-xl group bg-stone-950">
                            <img id="step-img" src="images/luoc_do_can_cu_tay_son.jpg" alt="Lược đồ hành quân" class="w-full h-64 sm:h-72 object-cover object-center transform group-hover:scale-105 transition duration-700">
                            <div class="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent"></div>
                            <div class="absolute bottom-3 left-3 right-3 text-center">
                                <span id="step-img-caption" class="text-xs text-amber-200 font-semibold bg-black/80 px-3 py-1.5 rounded-lg border border-amber-500/40 inline-block shadow">
                                    Đại bản doanh Phú Xuân - Phát tích cuộc hành quân thần tốc
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
'''

html = html.replace('<!-- 4 Mission Cards for the 4 Groups -->', war_map_html + '\n\n            <!-- 4 Mission Cards for the 4 Groups -->', 1)

# 6. Inject Modals before </body>
modals_html = '''
    <!-- ========================================== -->
    <!-- MODAL 1: ĐẤU TRƯỜNG TRÍ TUỆ QUANG TRUNG (60s QUIZ) -->
    <!-- ========================================== -->
    <div id="arena-quiz-modal" class="fixed inset-0 z-50 bg-black/90 backdrop-blur-md hidden items-center justify-center p-4 overflow-y-auto animate-fade">
        <div class="max-w-2xl w-full card-tayson rounded-3xl p-6 sm:p-8 border-2 border-yellow-500/80 shadow-[0_0_60px_rgba(245,158,11,0.4)] bg-gradient-to-b from-[#1c100e] via-[#120a08] to-[#0a0706] relative">
            <!-- Close Button -->
            <button type="button" onclick="closeArenaQuizModal()" class="cursor-pointer absolute top-5 right-5 w-10 h-10 rounded-full bg-stone-900 border border-stone-700 hover:border-amber-500 text-stone-400 hover:text-white flex items-center justify-center transition">
                <i class="fa-solid fa-xmark text-lg"></i>
            </button>

            <!-- Quiz Screen 1: Start Screen -->
            <div id="quiz-start-screen" class="space-y-6 text-center py-4">
                <div class="w-20 h-20 mx-auto rounded-3xl bg-gradient-to-br from-red-700 via-amber-600 to-yellow-500 flex items-center justify-center text-white text-3xl shadow-xl shadow-red-900/60 border-2 border-yellow-300">
                    <i class="fa-solid fa-bolt text-yellow-300 animate-bounce"></i>
                </div>
                <div>
                    <span class="text-xs px-3 py-1 rounded-full bg-red-950 text-amber-300 border border-red-500/60 font-bold uppercase tracking-widest">
                        Thử Tài Chiến Lược Gia Tây Sơn
                    </span>
                    <h3 class="text-2xl sm:text-3xl font-black font-cinzel text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-yellow-400 to-amber-500 mt-2">
                        ĐẤU TRƯỜNG THẦN TỐC 60 GIÂY
                    </h3>
                    <p class="text-xs sm:text-sm text-stone-300 mt-2 max-w-md mx-auto leading-relaxed">
                        Vượt qua 5 câu hỏi tình huống chiến thuật lịch sử bài 8. Đạt điểm tối đa để nhận danh hiệu vinh danh <strong class="text-amber-300 font-bold">"Vạn Thắng Tướng Quân"</strong> và pháo hoa ăn mừng!
                    </p>
                </div>

                <div class="grid grid-cols-3 gap-3 max-w-sm mx-auto text-center text-xs">
                    <div class="p-3 rounded-xl bg-black/60 border border-amber-900/40">
                        <i class="fa-solid fa-stopwatch text-amber-400 text-lg block mb-1"></i>
                        <span class="font-bold text-stone-200">60 Giây</span>
                    </div>
                    <div class="p-3 rounded-xl bg-black/60 border border-amber-900/40">
                        <i class="fa-solid fa-question text-amber-400 text-lg block mb-1"></i>
                        <span class="font-bold text-stone-200">5 Câu Hỏi</span>
                    </div>
                    <div class="p-3 rounded-xl bg-black/60 border border-amber-900/40">
                        <i class="fa-solid fa-award text-amber-400 text-lg block mb-1"></i>
                        <span class="font-bold text-stone-200">Huy Hiệu Số</span>
                    </div>
                </div>

                <div class="pt-2">
                    <button type="button" onclick="startArenaQuiz()" class="cursor-pointer px-8 py-3.5 rounded-2xl bg-gradient-to-r from-red-600 via-amber-600 to-yellow-500 hover:from-red-500 hover:to-yellow-400 text-stone-950 font-black text-sm uppercase tracking-wider shadow-xl shadow-red-900/60 border border-yellow-300 transition transform hover:scale-105 flex items-center gap-2 mx-auto">
                        <i class="fa-solid fa-play"></i> Bắt Đầu Thử Thách Ngay
                    </button>
                </div>
            </div>

            <!-- Quiz Screen 2: Active Playing -->
            <div id="quiz-playing-screen" class="space-y-6 hidden">
                <!-- Header Stats: Timer & Score -->
                <div class="flex items-center justify-between pb-4 border-b border-amber-900/40">
                    <div class="flex items-center gap-2">
                        <span class="text-xs text-stone-400 font-medium">Câu hỏi:</span>
                        <span id="quiz-question-idx" class="text-sm font-black text-amber-300 font-mono">1/5</span>
                    </div>
                    <!-- Countdown Bar & Number -->
                    <div class="flex items-center gap-2 bg-black/60 px-3.5 py-1.5 rounded-full border border-amber-500/40">
                        <i class="fa-solid fa-clock text-amber-400 text-xs"></i>
                        <span id="quiz-timer-text" class="text-sm font-black font-mono text-yellow-300">60s</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-xs text-stone-400 font-medium">Điểm:</span>
                        <span id="quiz-current-score" class="text-sm font-black text-emerald-400 font-mono">0</span>
                    </div>
                </div>

                <!-- Timer progress bar -->
                <div class="w-full h-1.5 bg-stone-900 rounded-full overflow-hidden">
                    <div id="quiz-timer-bar" class="h-full bg-gradient-to-r from-amber-500 to-red-500 w-full transition-all duration-1000 ease-linear"></div>
                </div>

                <!-- Question Text -->
                <div class="min-h-[70px]">
                    <h4 id="quiz-question-text" class="text-base sm:text-lg font-bold text-amber-100 leading-snug">
                        Đang tải câu hỏi...
                    </h4>
                </div>

                <!-- 4 Choices Grid -->
                <div id="quiz-choices-container" class="grid grid-cols-1 gap-3">
                    <!-- Dynamic choice buttons inserted here -->
                </div>

                <!-- Feedback hint box -->
                <div id="quiz-feedback-box" class="p-3.5 rounded-xl bg-black/80 border border-stone-800 text-xs text-stone-300 leading-relaxed hidden">
                    <span id="quiz-feedback-text"></span>
                </div>
            </div>

            <!-- Quiz Screen 3: Victory & Certificate Screen -->
            <div id="quiz-finish-screen" class="space-y-6 text-center py-2 hidden">
                <div class="w-24 h-24 mx-auto rounded-full bg-gradient-to-tr from-amber-600 via-yellow-400 to-amber-200 p-1 shadow-2xl shadow-yellow-500/50">
                    <div class="w-full h-full rounded-full bg-stone-950 flex flex-col items-center justify-center">
                        <i class="fa-solid fa-trophy text-3xl text-yellow-400"></i>
                    </div>
                </div>

                <div>
                    <span class="text-xs px-3 py-1 rounded-full bg-emerald-950 text-emerald-300 border border-emerald-500/40 font-bold uppercase">
                        Hoàn Thành Thử Thách
                    </span>
                    <h3 id="badge-rank-title" class="text-2xl sm:text-3xl font-black font-cinzel text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-yellow-400 to-amber-500 mt-2">
                        VẠN THẮNG TƯỚNG QUÂN
                    </h3>
                    <p class="text-xs sm:text-sm text-stone-300 mt-1">
                        Chúc mừng em đã hoàn thành xuất sắc thử thách chiến lược Quang Trung!
                    </p>
                </div>

                <!-- Digital Certificate Card -->
                <div class="p-5 rounded-2xl bg-gradient-to-br from-red-950/70 via-stone-900 to-black border-2 border-yellow-500/70 shadow-xl max-w-md mx-auto text-left space-y-3 relative overflow-hidden">
                    <div class="absolute -right-10 -bottom-10 opacity-10 text-9xl font-cinzel text-amber-300">⚔️</div>
                    <div class="flex items-center justify-between text-xs border-b border-amber-900/60 pb-2">
                        <span class="font-bold text-amber-400 tracking-wider">CHỨNG NHẬN SỬ HỌC SỐ</span>
                        <span class="text-stone-400 font-mono">BÀI 8 - LỊCH SỬ 8</span>
                    </div>
                    <div class="space-y-1">
                        <label class="text-[11px] text-stone-400">Họ và tên học sinh / Đội thi:</label>
                        <input id="student-cert-name" type="text" value="Học Sinh Giỏi Lịch Sử 8" class="w-full px-3 py-1.5 rounded-lg bg-black/70 border border-amber-600/50 text-amber-200 font-bold text-sm focus:outline-none focus:border-yellow-400">
                    </div>
                    <div class="grid grid-cols-2 gap-2 text-xs pt-1">
                        <div class="bg-black/50 p-2 rounded-lg border border-stone-800">
                            <span class="text-stone-400 block text-[10px]">Điểm đạt được:</span>
                            <span id="final-score-val" class="font-black text-amber-300 text-base">100/100</span>
                        </div>
                        <div class="bg-black/50 p-2 rounded-lg border border-stone-800">
                            <span class="text-stone-400 block text-[10px]">Thời gian còn lại:</span>
                            <span id="final-time-val" class="font-black text-emerald-400 text-base">24s</span>
                        </div>
                    </div>
                </div>

                <div class="flex flex-wrap items-center justify-center gap-3 pt-2">
                    <button type="button" onclick="startArenaQuiz()" class="cursor-pointer px-5 py-2.5 rounded-xl bg-stone-900 hover:bg-stone-800 text-amber-300 border border-amber-500/50 font-bold text-xs flex items-center gap-2">
                        <i class="fa-solid fa-rotate-left"></i> Chơi Lại
                    </button>
                    <button type="button" onclick="printCertificate()" class="cursor-pointer px-5 py-2.5 rounded-xl bg-gradient-to-r from-amber-600 to-yellow-500 text-stone-950 font-black text-xs flex items-center gap-2 shadow-lg">
                        <i class="fa-solid fa-print"></i> In / Lưu Thẻ Vinh Danh
                    </button>
                    <button type="button" onclick="closeArenaQuizModal()" class="cursor-pointer px-5 py-2.5 rounded-xl bg-stone-800 hover:bg-stone-700 text-stone-300 text-xs font-semibold">
                        Đóng
                    </button>
                </div>
            </div>
        </div>
    </div>

    <!-- ========================================== -->
    <!-- MODAL 2: PHÒNG TRÌNH CHIẾU BÁO CÁO (CINEMA PRESENTATION SUITE) -->
    <!-- ========================================== -->
    <div id="presentation-suite-modal" class="fixed inset-0 z-50 bg-[#0c0908] hidden flex-col animate-fade">
        <!-- Presentation Top Control Bar -->
        <div class="h-16 bg-[#160f0d] border-b border-amber-800/40 px-6 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-red-900 flex items-center justify-center text-amber-300 border border-amber-500/40">
                    <i class="fa-solid fa-tv"></i>
                </div>
                <div>
                    <h3 class="text-sm sm:text-base font-black text-amber-200 uppercase tracking-wider">
                        Chế Độ Trình Chiếu Báo Cáo Trước Lớp & Ban Giám Khảo
                    </h3>
                    <p class="text-[11px] text-stone-400">Tối ưu máy chiếu lớp học & Màn hình TV lớn</p>
                </div>
            </div>

            <!-- Slide Selector Tabs -->
            <div class="hidden md:flex items-center gap-1.5 bg-black/60 p-1 rounded-xl border border-amber-900/40 text-xs">
                <button type="button" onclick="changePresentationSlide(1)" id="pres-tab-1" class="cursor-pointer px-3 py-1.5 rounded-lg font-bold text-amber-300 bg-amber-950 border border-amber-500/40">Nhóm 1</button>
                <button type="button" onclick="changePresentationSlide(2)" id="pres-tab-2" class="cursor-pointer px-3 py-1.5 rounded-lg font-medium text-stone-400 hover:text-stone-200">Nhóm 2</button>
                <button type="button" onclick="changePresentationSlide(3)" id="pres-tab-3" class="cursor-pointer px-3 py-1.5 rounded-lg font-medium text-stone-400 hover:text-stone-200">Nhóm 3</button>
                <button type="button" onclick="changePresentationSlide(4)" id="pres-tab-4" class="cursor-pointer px-3 py-1.5 rounded-lg font-medium text-stone-400 hover:text-stone-200">Nhóm 4</button>
            </div>

            <div class="flex items-center gap-3">
                <button type="button" onclick="togglePresentFullscreen()" class="cursor-pointer px-3 py-1.5 rounded-lg bg-stone-900 hover:bg-stone-800 border border-stone-700 text-stone-300 text-xs font-semibold flex items-center gap-1.5">
                    <i class="fa-solid fa-expand text-amber-400"></i> <span class="hidden sm:inline">Toàn Màn Hình</span>
                </button>
                <button type="button" onclick="closePresentationSuite()" class="cursor-pointer w-9 h-9 rounded-xl bg-red-950 hover:bg-red-900 border border-red-700/50 text-red-300 flex items-center justify-center transition">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>
            </div>
        </div>

        <!-- Presentation Main Slide Viewport -->
        <div class="flex-1 max-w-6xl w-full mx-auto p-6 sm:p-10 flex flex-col justify-between overflow-y-auto">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                <!-- Left Slide Details -->
                <div class="lg:col-span-7 space-y-5">
                    <div class="flex items-center gap-3">
                        <span id="pres-group-badge" class="px-3 py-1 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/40 text-xs font-black uppercase tracking-wider">
                            CHIẾN DỊCH SỐ 1
                        </span>
                        <span id="pres-group-period" class="text-xs text-stone-400 font-mono bg-stone-900 px-2.5 py-1 rounded border border-stone-800">
                            1771 - 1777
                        </span>
                        <span id="pres-group-status" class="text-xs px-2.5 py-1 rounded bg-emerald-950 text-emerald-300 border border-emerald-600/40 font-semibold">
                            <i class="fa-solid fa-circle-check mr-1"></i> Đã Phê Duyệt Sư Phạm
                        </span>
                    </div>

                    <h2 id="pres-group-title" class="text-2xl sm:text-3xl lg:text-4xl font-black text-amber-100 font-serif leading-tight">
                        Lật Đổ Chính Quyền Chúa Nguyễn Ở Đàng Trong
                    </h2>

                    <!-- Student Written Findings Box -->
                    <div class="p-5 rounded-2xl bg-black/70 border border-amber-600/40 space-y-3">
                        <div class="flex items-center justify-between text-xs text-amber-300 font-bold border-b border-stone-800 pb-2">
                            <span><i class="fa-solid fa-feather mr-1.5"></i> KẾT QUẢ NGHIÊN CỨU CỦA HỌC SINH</span>
                            <span id="pres-members-count" class="text-stone-400 font-normal">8 thành viên</span>
                        </div>
                        <div id="pres-student-summary" class="text-stone-200 text-sm sm:text-base leading-relaxed space-y-2">
                            <!-- Injected student work -->
                        </div>
                    </div>

                    <!-- Embedded Podcast Audio Player with Animated Soundwave -->
                    <div class="p-4 rounded-2xl bg-gradient-to-r from-red-950/70 to-stone-900 border border-amber-500/50 flex flex-wrap items-center justify-between gap-4">
                        <div class="flex items-center gap-3">
                            <button type="button" onclick="togglePresentationAudio()" id="pres-audio-btn" class="cursor-pointer w-12 h-12 rounded-2xl bg-gradient-to-br from-amber-500 to-yellow-500 text-stone-950 text-xl font-bold flex items-center justify-center shadow-lg transition transform hover:scale-105">
                                <i class="fa-solid fa-play" id="pres-audio-icon"></i>
                            </button>
                            <div>
                                <h5 class="text-xs sm:text-sm font-bold text-amber-200">Bản Tin Phát Thanh Podcast Lịch Sử</h5>
                                <p class="text-[11px] text-stone-400">Giọng đọc thuyết minh truyền cảm của học sinh</p>
                            </div>
                        </div>

                        <!-- Animated Soundwave bars -->
                        <div class="flex items-center gap-1 h-8 px-4 py-1 rounded-xl bg-black/60 border border-amber-900/40" id="pres-soundwave-container">
                            <div class="w-1 h-3 bg-amber-500 rounded-full"></div>
                            <div class="w-1 h-6 bg-amber-400 rounded-full"></div>
                            <div class="w-1 h-4 bg-yellow-300 rounded-full"></div>
                            <div class="w-1 h-7 bg-amber-500 rounded-full"></div>
                            <div class="w-1 h-5 bg-amber-400 rounded-full"></div>
                            <div class="w-1 h-2 bg-yellow-200 rounded-full"></div>
                            <div class="w-1 h-6 bg-amber-500 rounded-full"></div>
                            <div class="w-1 h-3 bg-amber-400 rounded-full"></div>
                        </div>
                    </div>
                </div>

                <!-- Right Slide Media & Teacher Stamp -->
                <div class="lg:col-span-5 space-y-4">
                    <div class="relative rounded-2xl overflow-hidden border-2 border-amber-500/70 shadow-2xl bg-stone-950">
                        <img id="pres-img" src="images/luoc_do_can_cu_tay_son.jpg" alt="Lược đồ" class="w-full h-72 sm:h-80 object-cover object-center">
                        <div class="absolute inset-0 bg-gradient-to-t from-black via-transparent to-transparent"></div>
                        
                        <!-- Teacher Approved Seal Badge -->
                        <div class="absolute bottom-4 right-4 bg-emerald-950/95 border-2 border-emerald-400 text-emerald-300 text-xs font-black px-4 py-2 rounded-xl shadow-2xl flex items-center gap-2">
                            <i class="fa-solid fa-stamp text-emerald-400 text-base"></i>
                            <span>ĐÃ KIỂM DUYỆT SƯ PHẠM</span>
                        </div>
                    </div>

                    <!-- Teacher Feedback Box -->
                    <div class="p-4 rounded-xl bg-stone-900/80 border border-stone-800 text-xs text-stone-300">
                        <strong class="text-amber-300 flex items-center gap-1.5 mb-1">
                            <i class="fa-solid fa-user-tie"></i> Đánh giá của Giáo viên:
                        </strong>
                        <p id="pres-teacher-feedback" class="italic text-stone-300">
                            "Nhóm phân tích chính xác các mốc sự kiện lịch sử, giọng đọc truyền cảm, tư duy phản biện sắc sảo."
                        </p>
                    </div>
                </div>
            </div>

            <!-- Slide Bottom Navigation Bar -->
            <div class="pt-6 border-t border-amber-900/40 flex items-center justify-between">
                <button type="button" onclick="prevPresentationSlide()" class="cursor-pointer px-5 py-2.5 rounded-xl bg-stone-900 hover:bg-stone-800 border border-stone-700 text-amber-300 font-bold text-xs flex items-center gap-2">
                    <i class="fa-solid fa-arrow-left"></i> Nhóm Trước
                </button>
                <div class="text-xs text-stone-400 font-mono">
                    Slide <span id="pres-slide-num" class="font-bold text-amber-300">1</span> / 4 (Dùng phím ← → trên bàn phím)
                </div>
                <button type="button" onclick="nextPresentationSlide()" class="cursor-pointer px-5 py-2.5 rounded-xl bg-gradient-to-r from-amber-600 to-yellow-500 text-stone-950 font-black text-xs flex items-center gap-2 shadow-lg">
                    Nhóm Kế Tiếp <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>
    </div>
'''

html = html.replace('</body>', modals_html + '\n</body>', 1)

# 7. Inject JS logic into ONLY the LAST </script> tag
js_code = '''
        // =========================================================================
        // FULL INTERACTIVE SUITE UPGRADE: AUDIO SYNTH, WAR MAP, QUIZ & PRESENTATION
        // =========================================================================

        // --- A. BATTLE DRUMS & AUDIO SYNTHESIS ENGINE ---
        let audioCtxInstance = null;
        let battleDrumsInterval = null;
        let isBattleDrumsActive = false;
        let isEmberParticlesActive = true;

        function getAudioContext() {
            if (!audioCtxInstance) {
                const AudioContextClass = window.AudioContext || window.webkitAudioContext;
                audioCtxInstance = new AudioContextClass();
            }
            if (audioCtxInstance.state === 'suspended') {
                audioCtxInstance.resume();
            }
            return audioCtxInstance;
        }

        // Bass Drum Synthesis (Tiếng trống trận Tây Sơn trầm vang)
        function playBassDrum(pitch = 95, duration = 0.55, volume = 0.85) {
            try {
                const ctx = getAudioContext();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                const filter = ctx.createBiquadFilter();

                osc.type = 'sine';
                osc.frequency.setValueAtTime(pitch, ctx.currentTime);
                osc.frequency.exponentialRampToValueAtTime(24, ctx.currentTime + duration);

                filter.type = 'lowpass';
                filter.frequency.setValueAtTime(320, ctx.currentTime);

                gain.gain.setValueAtTime(volume, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);

                osc.connect(filter);
                filter.connect(gain);
                gain.connect(ctx.destination);

                osc.start();
                osc.stop(ctx.currentTime + duration);
            } catch(e) {}
        }

        // Chiêng Đồng / Chuông ngân vang dội
        function playChiengDong(freq = 420, duration = 2.0, volume = 0.35) {
            try {
                const ctx = getAudioContext();
                [freq, freq * 1.5, freq * 2.08].forEach((f, idx) => {
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(f, ctx.currentTime);
                    gain.gain.setValueAtTime(volume / (idx + 1), ctx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + duration);
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.start();
                    osc.stop(ctx.currentTime + duration);
                });
            } catch(e) {}
        }

        // Kèn khải hoàn / Fanfare thắng lợi
        function playTriumphFanfare() {
            try {
                const ctx = getAudioContext();
                const notes = [261.63, 329.63, 392.00, 523.25, 659.25, 783.99];
                notes.forEach((freq, i) => {
                    setTimeout(() => {
                        const osc = ctx.createOscillator();
                        const gain = ctx.createGain();
                        osc.type = 'triangle';
                        osc.frequency.setValueAtTime(freq, ctx.currentTime);
                        gain.gain.setValueAtTime(0.2, ctx.currentTime);
                        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.35);
                        osc.connect(gain);
                        gain.connect(ctx.destination);
                        osc.start();
                        osc.stop(ctx.currentTime + 0.35);
                    }, i * 80);
                });
                setTimeout(() => playChiengDong(330, 2.5, 0.45), 550);
            } catch(e) {}
        }

        // Bật / Tắt Tiếng Trống Trận Tây Sơn
        function toggleBattleDrums() {
            const btn = document.getElementById('btn-battle-drums');
            const statusLabel = document.getElementById('battle-drums-status');

            if (isBattleDrumsActive) {
                clearInterval(battleDrumsInterval);
                isBattleDrumsActive = false;
                if (btn) btn.classList.remove('animate-pulse', 'border-red-500', 'bg-red-950/90', 'text-yellow-300');
                if (statusLabel) {
                    statusLabel.textContent = 'Bật';
                    statusLabel.className = 'text-amber-200 font-bold';
                }
            } else {
                getAudioContext();
                isBattleDrumsActive = true;
                if (btn) btn.classList.add('animate-pulse', 'border-red-500', 'bg-red-950/90', 'text-yellow-300');
                if (statusLabel) {
                    statusLabel.textContent = 'Đang phát';
                    statusLabel.className = 'text-yellow-400 font-bold';
                }

                // Tiết tấu trống trận: Tùng... Tùng... Tùng-Tùng-Tùng-Tùng Tùng! [Chiêng]
                const rhythm = [
                    { type: 'drum', pitch: 100, vol: 0.9, delay: 0 },
                    { type: 'drum', pitch: 88, vol: 0.7, delay: 350 },
                    { type: 'drum', pitch: 84, vol: 0.6, delay: 700 },
                    { type: 'drum', pitch: 110, vol: 0.95, delay: 1000 },
                    { type: 'drum', pitch: 105, vol: 0.9, delay: 1180 },
                    { type: 'drum', pitch: 100, vol: 0.85, delay: 1360 },
                    { type: 'drum', pitch: 125, vol: 1.0, delay: 1540 },
                    { type: 'gong', freq: 440, delay: 1600 }
                ];

                function playRhythmCycle() {
                    if (!isBattleDrumsActive) return;
                    rhythm.forEach(item => {
                        setTimeout(() => {
                            if (!isBattleDrumsActive) return;
                            if (item.type === 'drum') playBassDrum(item.pitch, 0.45, item.vol);
                            if (item.type === 'gong') playChiengDong(item.freq, 1.8, 0.35);
                        }, item.delay);
                    });
                }
                playRhythmCycle();
                battleDrumsInterval = setInterval(playRhythmCycle, 2000);
            }
        }

        // Nghe Diễn Đọc Lời Hiểu Dụ Quang Trung
        function playQuangTrungSpeech() {
            const speechText = "Đánh cho để dài tóc! Đánh cho để đen răng! Đánh cho nó chích luân bất phản! Đánh cho nó phiến giáp bất hoàn! Đánh cho sử tri Nam quốc anh hùng chi hữu chủ!";
            
            // Trống lệnh mở màn
            playBassDrum(120, 0.8, 1.0);
            setTimeout(() => playChiengDong(440, 2.5, 0.5), 150);

            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const utterance = new SpeechSynthesisUtterance(speechText);
                utterance.lang = 'vi-VN';
                utterance.rate = 0.92;
                utterance.pitch = 0.88;

                const voices = window.speechSynthesis.getVoices();
                const viVoice = voices.find(v => v.lang.includes('vi'));
                if (viVoice) utterance.voice = viVoice;

                const quoteBox = document.getElementById('hero-quote-container');
                utterance.onstart = () => {
                    if (quoteBox) quoteBox.classList.add('ring-4', 'ring-amber-400', 'shadow-[0_0_35px_rgba(245,158,11,0.7)]');
                };
                utterance.onend = () => {
                    if (quoteBox) quoteBox.classList.remove('ring-4', 'ring-amber-400', 'shadow-[0_0_35px_rgba(245,158,11,0.7)]');
                    playChiengDong(380, 2.0, 0.4);
                };
                window.speechSynthesis.speak(utterance);
            } else {
                alert("Lời hiểu dụ Quang Trung: \\n" + speechText);
            }
        }

        // --- B. EMBER PARTICLE CANVAS SYSTEM ---
        function initEmberCanvas() {
            const canvas = document.getElementById('ember-canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            let w = canvas.width = window.innerWidth;
            let h = canvas.height = window.innerHeight;

            window.addEventListener('resize', () => {
                w = canvas.width = window.innerWidth;
                h = canvas.height = window.innerHeight;
            });

            const embers = [];
            const count = 40;
            const colors = ['#F59E0B', '#EF4444', '#D97706', '#FBBF24', '#DC2626'];

            for (let i = 0; i < count; i++) {
                embers.push({
                    x: Math.random() * w,
                    y: Math.random() * h,
                    r: Math.random() * 2.5 + 0.8,
                    speedY: Math.random() * 0.8 + 0.35,
                    speedX: (Math.random() - 0.5) * 0.5,
                    opacity: Math.random() * 0.6 + 0.2,
                    color: colors[Math.floor(Math.random() * colors.length)]
                });
            }

            function animate() {
                if (!isEmberParticlesActive) {
                    ctx.clearRect(0, 0, w, h);
                    requestAnimationFrame(animate);
                    return;
                }
                ctx.clearRect(0, 0, w, h);
                embers.forEach(p => {
                    p.y -= p.speedY;
                    p.x += Math.sin(p.y * 0.02) * 0.4 + p.speedX;
                    p.opacity += (Math.random() - 0.5) * 0.015;
                    if (p.opacity < 0.1) p.opacity = 0.1;
                    if (p.opacity > 0.8) p.opacity = 0.8;

                    if (p.y < -10) {
                        p.y = h + 10;
                        p.x = Math.random() * w;
                    }
                    if (p.x < -10) p.x = w + 10;
                    if (p.x > w + 10) p.x = -10;

                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                    ctx.fillStyle = p.color;
                    ctx.globalAlpha = p.opacity;
                    ctx.shadowBlur = 8;
                    ctx.shadowColor = p.color;
                    ctx.fill();
                });
                ctx.shadowBlur = 0;
                ctx.globalAlpha = 1;
                requestAnimationFrame(animate);
            }
            animate();
        }

        function toggleEmberEffect() {
            isEmberParticlesActive = !isEmberParticlesActive;
            const lbl = document.getElementById('lbl-ember-state');
            if (lbl) {
                lbl.textContent = isEmberParticlesActive ? 'Bật' : 'Tắt';
                lbl.className = isEmberParticlesActive ? 'text-amber-300 font-bold' : 'text-stone-400 font-semibold';
            }
        }

        // --- C. SA BÀN CHIẾN LƯỢC: 5 CHẶNG HÀNH QUÂN THẦN TỐC ---
        const WAR_STEPS_DATA = [
            {
                phase: "CHẶNG 1: KHỞI ĐẦU CHIẾN DỊCH",
                date: "22/12/1788 (25 tháng 11 năm Mậu Thân)",
                location: "Núi Bân (Phú Xuân - Huế)",
                title: "Lễ Đăng Quang Tại Núi Bân & Lệnh Xuất Quân Thần Tốc",
                quote: "“Trẫm nay ứng mệnh trời, thuận lòng người, lên ngôi Hoàng đế để dẹp yên giặc giã, giữ yên bờ cõi!”",
                desc1: "Nhận được tin cấp báo 29 vạn quân Mãn Thanh do Tôn Sĩ Nghị chỉ huy tràn vào chiếm đóng Thăng Long, Nguyễn Huệ lập đàn tế trời tại núi Bân (Phú Xuân - Huế), chính thức lên ngôi Hoàng đế, lấy niên hiệu Quang Trung.",
                desc2: "Nghệ thuật quân sự: Danh chính ngôn thuận xưng đế để tập hợp nhân tâm cả nước, chấm dứt tình trạng cát cứ, đồng thời mở đầu cuộc hành quân thần tốc ra Bắc với tốc độ hành tiến vô tiền khoáng hậu.",
                troops: "6 vạn quân tinh nhuệ ban đầu",
                strategy: "Xưng đế quy tụ nhân tâm, hành quân chớp nhoáng",
                img: "images/luoc_do_can_cu_tay_son.jpg",
                caption: "Đại bản doanh Phú Xuân - Phát tích cuộc hành quân thần tốc"
            },
            {
                phase: "CHẶNG 2: DUYỆT BINH & CHIẾN LƯỢC",
                date: "15 tháng Chạp năm Mậu Thân (1788)",
                location: "Nghệ An - Phòng tuyến Tam Điệp / Biện Sơn",
                title: "Đại Duyệt Binh Nghệ An, Đọc Hiểu Dụ & Quyết Định Ăn Tết Sớm",
                quote: "“Đánh cho để dài tóc / Đánh cho để đen răng / Đánh cho nó chích luân bất phản / Đánh cho nó phiến giáp bất hoàn!”",
                desc1: "Đến Nghệ An chỉ sau vài ngày, vua Quang Trung tuyển thêm hơn 4 vạn tân binh, tổ chức duyệt binh lớn và đọc bài Hiểu dụ bất hủ, khơi dậy tinh thần yêu nước quật cường của tướng sĩ.",
                desc2: "Hội quân tại Tam Điệp cùng Ngô Thì Nhậm, Ngô Văn Sở; khen ngợi kế sách bảo toàn lực lượng. Vua tuyên bố mở tiệc khao quân ăn Tết sớm vào đêm 30, hẹn mùng 7 Tết vào Thăng Long ăn Tết khải hoàn!",
                troops: "Hơn 10 vạn quân, hàng trăm thớt voi chiến",
                strategy: "Bảo toàn lực lượng (kế Ngô Thì Nhậm), ăn Tết sớm khích lệ sĩ khí",
                img: "images/quang_trung_oai_phong_1789.jpg",
                caption: "Đại duyệt binh tại Nghệ An & Khí thế hào hùng của đoàn quân áo vải"
            },
            {
                phase: "CHẶNG 3: BẢO MẬT TUYỆT ĐỐI",
                date: "Đêm 30 Tết Kỷ Dậu (1789)",
                location: "Tiền đồn Gián Khẩu (Ninh Bình)",
                title: "Vượt Sông Gián Khẩu, Tiêu Diệt Tiền Tiêu & Giữ Kín Tung Tích",
                quote: "“Bắt gọn toàn bộ toán thám tử giặc, giữ bí mật tuyệt đối cuộc hành quân thần tốc!”",
                desc1: "Đêm 30 Tết, quân Tây Sơn vượt sông Gián Khẩu (sông Đáy), bất ngờ đánh úp đồn tiền tiêu của quân Thanh và quân tay sai bán nước Lê Chiêu Thống.",
                desc2: "Nghệ thuật quân sự: Toàn bộ quân do thám của giặc bị bắt sống, không một tên nào chạy thoát. Quân Thanh ở Thăng Long hoàn toàn không hay biết đại quân Tây Sơn đã áp sát cửa ngõ kinh thành.",
                troops: "Đạo quân tiên phong cảm tử",
                strategy: "Bất ngờ tuyệt đối, phong tỏa tin tức chiến trường",
                img: "images/luoc_do_rach_gam_xoai_mut.jpg",
                caption: "Nghệ thuật tập kích bí mật ban đêm của bộ binh Tây Sơn"
            },
            {
                phase: "CHẶNG 4: TÂM LÝ CHIẾN BẬC THẦY",
                date: "Nửa đêm Mùng 3 Tết Kỷ Dậu (1789)",
                location: "Đồn Hà Hồi (Thường Tín, Hà Nội)",
                title: "Bao Vây Đồn Hà Hồi, Bức Hàng Không Tốn Một Mũi Tên",
                quote: "“Tiếng loa truyền gọi, đuốc sáng rực trời, quân giặc run sợ vỡ mật xin hàng!”",
                desc1: "Nửa đêm mùng 3 Tết, quân Tây Sơn bí mật tiếp cận và lặng lẽ bao vây chặt đồn Hà Hồi (cách Thăng Long khoảng 20km).",
                desc2: "Đến canh tư, quân ta đốt đuốc sáng rực, bắc loa gọi hàng kết hợp tiếng hò reo vang dậy như có vạn binh. Quân Thanh rụng rời kinh hãi, mở cửa đồn xin hàng toàn bộ; thu trọn kho lương thảo khí giới.",
                troops: "Đạo quân chủ lực vây hãm",
                strategy: "Tâm lý chiến, đánh vào tinh thần hoang mang của giặc",
                img: "images/quang_trung_epic_victory_1789.jpg",
                caption: "Trận Hà Hồi - Bức hàng thần tốc đồn lũy kiên cố của địch"
            },
            {
                phase: "CHẶNG 5: ĐẠI THẮNG LỊCH SỬ",
                date: "Mùng 5 Tết Kỷ Dậu (1789)",
                location: "Ngọc Hồi - Đống Đa - Thăng Long",
                title: "Đại Phá 29 Vạn Quân Thanh - Tiến Vào Thăng Long Trưa Mùng 5 Tết",
                quote: "“Hoàng đế Quang Trung áo bào sém đen khói súng, dẫn đầu đoàn quân khải hoàn Thăng Long!”",
                desc1: "Sáng mùng 5 Tết, Quang Trung trực tiếp chỉ huy đánh đồn Ngọc Hồi: dùng 60 chiến tượng cùng các tổ cảm tử khiên gỗ bện rơm ướt phá hủy hỏa công súng đạn của địch. Cùng lúc, Đô đốc Đặng Tiến Đông bất ngờ đánh úp đồn Khương Thượng (Đống Đa).",
                desc2: "Tướng giặc Sầm Nghi Đống thắt cổ tự tử; Tôn Sĩ Nghị vứt bỏ ấn tín tháo chạy, chen nhau qua cầu phao sông Hồng làm cầu đứt, xác giặc nghẽn dòng nước. Đúng trưa mùng 5 Tết (sớm 2 ngày so với dự kiến), quân Tây Sơn giải phóng hoàn toàn Thăng Long!",
                troops: "Toàn bộ 5 đạo quân phối hợp hiệp đồng",
                strategy: "Hiệp đồng binh chủng, phá hỏa công bằng khiên rơm ướt, đánh tập hậu",
                img: "images/luoc_do_ngoc_hoi_dong_da.jpg",
                caption: "Lược đồ trận Ngọc Hồi - Đống Đa đại phá 29 vạn quân Thanh"
            }
        ];

        let currentWarStep = 0;
        let autoPlayTimer = null;
        let isAutoPlaying = false;

        function selectWarStep(idx) {
            currentWarStep = idx;
            const data = WAR_STEPS_DATA[idx];
            if (!data) return;

            document.getElementById('step-badge-phase').textContent = data.phase;
            document.getElementById('step-date').textContent = data.date;
            document.getElementById('step-title').textContent = data.title;
            document.getElementById('step-quote').textContent = data.quote;
            document.getElementById('step-desc-1').textContent = data.desc1;
            document.getElementById('step-desc-2').innerHTML = `<strong class="text-amber-400">Nghệ thuật quân sự:</strong> ${data.desc2}`;
            document.getElementById('step-troops').textContent = data.troops;
            document.getElementById('step-strategy').textContent = data.strategy;
            document.getElementById('step-img').src = data.img;
            document.getElementById('step-img-caption').textContent = data.caption;

            for (let i = 0; i < 5; i++) {
                const btn = document.getElementById(`war-step-btn-${i}`);
                if (btn) {
                    if (i === idx) {
                        btn.className = "cursor-pointer war-step-btn p-3 rounded-2xl border-2 border-amber-400 bg-amber-950 text-left transition transform -translate-y-1 shadow-xl shadow-amber-900/50";
                    } else {
                        btn.className = "cursor-pointer war-step-btn p-3 rounded-2xl border border-stone-800 bg-stone-900/60 hover:bg-stone-800 text-left transition transform hover:-translate-y-0.5";
                    }
                }
            }

            playBassDrum(100 + idx * 10, 0.4, 0.7);
        }

        function autoPlayWarJourney() {
            const btn = document.getElementById('btn-autoplay-journey');
            const lbl = document.getElementById('lbl-autoplay');
            const icon = document.getElementById('icon-autoplay');

            if (isAutoPlaying) {
                clearInterval(autoPlayTimer);
                isAutoPlaying = false;
                if (lbl) lbl.textContent = "Diễn Tập Tự Động";
                if (icon) icon.className = "fa-solid fa-play";
            } else {
                isAutoPlaying = true;
                if (lbl) lbl.textContent = "Dừng Diễn Tập";
                if (icon) icon.className = "fa-solid fa-pause";

                let step = 0;
                selectWarStep(step);
                autoPlayTimer = setInterval(() => {
                    step++;
                    if (step >= WAR_STEPS_DATA.length) {
                        clearInterval(autoPlayTimer);
                        isAutoPlaying = false;
                        if (lbl) lbl.textContent = "Diễn Tập Lại";
                        if (icon) icon.className = "fa-solid fa-rotate-left";
                        playTriumphFanfare();
                    } else {
                        selectWarStep(step);
                    }
                }, 3500);
            }
        }

        function scrollToWarMap() {
            switchTab('portal');
            const el = document.getElementById('interactive-war-map');
            if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }

        // --- D. ĐẤU TRƯỜNG TRÍ TUỆ QUANG TRUNG (60s QUIZ) & CONFETTI ---
        const QUIZ_QUESTIONS = [
            {
                q: "Ngày 22/12/1788, Nguyễn Huệ chọn địa điểm nào để lập đàn tế trời, lên ngôi Hoàng đế trước khi xuất quân ra Bắc?",
                choices: [
                    "Kinh thành Thăng Long (Hà Nội)",
                    "Núi Bân (Phú Xuân - Huế)",
                    "Tây Sơn thượng đạo (Bình Định)",
                    "Phòng tuyến Tam Điệp (Ninh Bình)"
                ],
                correct: 1,
                hint: "Chính xác! Nguyễn Huệ lên ngôi tại núi Bân (Huế), lấy niên hiệu Quang Trung để quy tụ lòng dân cả nước."
            },
            {
                q: "Vua Quang Trung đã mở tiệc khao quân ăn Tết sớm vào đêm 30 và hẹn tướng sĩ ngày nào vào Thăng Long ăn Tết khải hoàn?",
                choices: [
                    "Mùng 3 Tết Kỷ Dậu",
                    "Mùng 5 Tết Kỷ Dậu",
                    "Mùng 7 Tết Kỷ Dậu",
                    "Rằm tháng Giêng"
                ],
                correct: 2,
                hint: "Chính xác! Vua hẹn mùng 7, nhưng nhờ hành quân thần tốc và đánh dũng mãnh, trưa mùng 5 quân Tây Sơn đã giải phóng Thăng Long (sớm 2 ngày)!"
            },
            {
                q: "Tại trận hạ đồn Ngọc Hồi kiên cố, nghĩa quân Tây Sơn đã áp dụng sáng kiến độc đáo nào để vô hiệu hóa súng đạn hỏa công của địch?",
                choices: [
                    "Đào địa đạo ngầm xuyên lòng đất áp sát chân thành",
                    "Dùng ván gỗ lớn bện rơm ướt làm lá chắn cho tổ cảm tử",
                    "Dùng bè lửa thả trôi xuôi dòng sông",
                    "Đợi trời đổ mưa dông lớn mới tấn công"
                ],
                correct: 1,
                hint: "Chính xác! Cứ 20 người khiêng một tấm ván bện rơm ướt, đạn súng và hỏa công quân Thanh bắn vào đều bị tắt ngấm."
            },
            {
                q: "Trong trận quyết chiến đánh tan 5 vạn quân Xiêm (1785), danh tướng Tây Sơn chọn khúc sông nào làm trận địa mai phục tiêu diệt giặc?",
                choices: [
                    "Sông Bạch Đằng",
                    "Sông Như Nguyệt",
                    "Rạch Gầm - Xoài Mút (Tiền Giang)",
                    "Sông Gianh (Quảng Bình)"
                ],
                correct: 2,
                hint: "Chính xác! Khúc sông Tiền đoạn Rạch Gầm - Xoài Mút với cù lao cồn bãi hiểm yếu đã chôn vùi toàn bộ chiến thuyền giặc Xiêm."
            },
            {
                q: "Ý nghĩa lịch sử to lớn nhất của phong trào Tây Sơn và sự nghiệp của người anh hùng áo vải Quang Trung là gì?",
                choices: [
                    "Lật đổ các tập đoàn phong kiến thống trị, xóa bỏ ranh giới chia cắt Đàng Trong - Đàng Ngoài",
                    "Đánh tan hai cuộc xâm lăng của quân Xiêm và Mãn Thanh, giữ vững nền độc lập",
                    "Đặt nền tảng vững chắc cho công cuộc thống nhất toàn vẹn lãnh thổ quốc gia",
                    "Tất cả các ý kiến trên đều đúng"
                ],
                correct: 3,
                hint: "Chính xác! Phong trào Tây Sơn đã hoàn thành xuất sắc cả hai sứ mệnh thiêng liêng: Thống nhất non sông và Bảo vệ độc lập dân tộc!"
            }
        ];

        let quizIndex = 0;
        let quizScore = 0;
        let quizTimerSeconds = 60;
        let quizTimerInterval = null;

        function openArenaQuizModal() {
            document.getElementById('arena-quiz-modal').classList.remove('hidden');
            document.getElementById('arena-quiz-modal').classList.add('flex');
            document.getElementById('quiz-start-screen').classList.remove('hidden');
            document.getElementById('quiz-playing-screen').classList.add('hidden');
            document.getElementById('quiz-finish-screen').classList.add('hidden');
        }

        function closeArenaQuizModal() {
            clearInterval(quizTimerInterval);
            document.getElementById('arena-quiz-modal').classList.add('hidden');
            document.getElementById('arena-quiz-modal').classList.remove('flex');
        }

        function startArenaQuiz() {
            quizIndex = 0;
            quizScore = 0;
            quizTimerSeconds = 60;

            document.getElementById('quiz-start-screen').classList.add('hidden');
            document.getElementById('quiz-finish-screen').classList.add('hidden');
            document.getElementById('quiz-playing-screen').classList.remove('hidden');

            renderCurrentQuestion();

            clearInterval(quizTimerInterval);
            updateTimerDisplay();
            quizTimerInterval = setInterval(() => {
                quizTimerSeconds--;
                updateTimerDisplay();
                if (quizTimerSeconds <= 0) {
                    clearInterval(quizTimerInterval);
                    finishArenaQuiz();
                }
            }, 1000);

            playBassDrum(120, 0.4, 0.8);
        }

        function updateTimerDisplay() {
            const timerText = document.getElementById('quiz-timer-text');
            const timerBar = document.getElementById('quiz-timer-bar');
            if (timerText) timerText.textContent = `${quizTimerSeconds}s`;
            if (timerBar) {
                const percent = (quizTimerSeconds / 60) * 100;
                timerBar.style.width = `${percent}%`;
                if (quizTimerSeconds <= 15) {
                    timerBar.className = "h-full bg-red-600 transition-all duration-1000 ease-linear animate-pulse";
                } else {
                    timerBar.className = "h-full bg-gradient-to-r from-amber-500 to-red-500 transition-all duration-1000 ease-linear";
                }
            }
        }

        function renderCurrentQuestion() {
            const q = QUIZ_QUESTIONS[quizIndex];
            document.getElementById('quiz-question-idx').textContent = `${quizIndex + 1}/${QUIZ_QUESTIONS.length}`;
            document.getElementById('quiz-current-score').textContent = quizScore;
            document.getElementById('quiz-question-text').textContent = q.q;

            const feedbackBox = document.getElementById('quiz-feedback-box');
            feedbackBox.classList.add('hidden');

            const container = document.getElementById('quiz-choices-container');
            container.innerHTML = '';

            const alphabet = ['A', 'B', 'C', 'D'];
            q.choices.forEach((choice, idx) => {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = "cursor-pointer quiz-choice-btn p-3.5 rounded-xl bg-stone-900/90 hover:bg-stone-800 border border-stone-700 hover:border-amber-500 text-left text-xs sm:text-sm text-stone-200 font-medium transition flex items-center gap-3";
                btn.innerHTML = `
                    <span class="w-6 h-6 rounded-lg bg-black/60 border border-amber-600/40 text-amber-300 flex items-center justify-center text-xs font-bold">${alphabet[idx]}</span>
                    <span>${choice}</span>
                `;
                btn.onclick = () => handleChoiceSelect(idx, btn);
                container.appendChild(btn);
            });
        }

        function handleChoiceSelect(choiceIdx, btnElement) {
            const q = QUIZ_QUESTIONS[quizIndex];
            const isCorrect = (choiceIdx === q.correct);

            document.querySelectorAll('.quiz-choice-btn').forEach(btn => btn.disabled = true);

            const feedbackBox = document.getElementById('quiz-feedback-box');
            feedbackBox.classList.remove('hidden');

            if (isCorrect) {
                quizScore += 20;
                btnElement.className = "quiz-choice-btn p-3.5 rounded-xl bg-emerald-950 border-2 border-emerald-400 text-left text-xs sm:text-sm text-emerald-200 font-bold transition flex items-center gap-3 shadow-lg shadow-emerald-950/60";
                feedbackBox.className = "p-3.5 rounded-xl bg-emerald-950/80 border border-emerald-500/50 text-xs text-emerald-200 leading-relaxed";
                feedbackBox.innerHTML = `<strong class="text-emerald-300 block mb-1">🎉 Xuất sắc! Đáp án chính xác!</strong> ${q.hint}`;
                playBassDrum(140, 0.3, 0.9);
                setTimeout(() => playChiengDong(520, 0.8, 0.3), 80);
            } else {
                btnElement.className = "quiz-choice-btn p-3.5 rounded-xl bg-red-950 border-2 border-red-500 text-left text-xs sm:text-sm text-red-200 font-bold transition flex items-center gap-3";
                feedbackBox.className = "p-3.5 rounded-xl bg-red-950/80 border border-red-500/50 text-xs text-red-200 leading-relaxed";
                feedbackBox.innerHTML = `<strong class="text-red-300 block mb-1">❌ Chưa chính xác!</strong> ${q.hint}`;
                playBassDrum(65, 0.5, 0.7);
            }

            document.getElementById('quiz-current-score').textContent = quizScore;

            setTimeout(() => {
                quizIndex++;
                if (quizIndex < QUIZ_QUESTIONS.length && quizTimerSeconds > 0) {
                    renderCurrentQuestion();
                } else {
                    clearInterval(quizTimerInterval);
                    finishArenaQuiz();
                }
            }, 1800);
        }

        function finishArenaQuiz() {
            document.getElementById('quiz-playing-screen').classList.add('hidden');
            document.getElementById('quiz-finish-screen').classList.remove('hidden');

            const scoreDisplay = document.getElementById('final-score-val');
            const timeDisplay = document.getElementById('final-time-val');
            const rankTitle = document.getElementById('badge-rank-title');

            if (scoreDisplay) scoreDisplay.textContent = `${quizScore}/100`;
            if (timeDisplay) timeDisplay.textContent = `${quizTimerSeconds}s`;

            if (quizScore >= 80) {
                rankTitle.textContent = "VẠN THẮNG TƯỚNG QUÂN";
                rankTitle.className = "text-2xl sm:text-3xl font-black font-cinzel text-transparent bg-clip-text bg-gradient-to-r from-amber-200 via-yellow-400 to-amber-500 mt-2";
                triggerFireworksConfetti();
                playTriumphFanfare();
            } else if (quizScore >= 60) {
                rankTitle.textContent = "ĐÔ ĐỐC TIÊN PHONG TÂY SƠN";
                rankTitle.className = "text-2xl sm:text-3xl font-black font-cinzel text-amber-300 mt-2";
                triggerFireworksConfetti();
                playChiengDong(440, 2, 0.4);
            } else {
                rankTitle.textContent = "CHIẾN LƯỢC GIA TRIỂN VỌNG";
                rankTitle.className = "text-2xl sm:text-3xl font-black font-cinzel text-stone-300 mt-2";
            }
        }

        function triggerFireworksConfetti() {
            const canvas = document.getElementById('confetti-canvas');
            if (!canvas) return;
            canvas.style.display = 'block';
            const ctx = canvas.getContext('2d');
            let w = canvas.width = window.innerWidth;
            let h = canvas.height = window.innerHeight;

            const particles = [];
            const colors = ['#F59E0B', '#EF4444', '#10B981', '#3B82F6', '#FBBF24', '#EC4899', '#8B5CF6'];

            for (let i = 0; i < 160; i++) {
                particles.push({
                    x: w / 2,
                    y: h * 0.45,
                    vx: (Math.random() - 0.5) * 16,
                    vy: (Math.random() - 0.7) * 18,
                    size: Math.random() * 6 + 3,
                    color: colors[Math.floor(Math.random() * colors.length)],
                    alpha: 1,
                    rotation: Math.random() * 360,
                    rotationSpeed: (Math.random() - 0.5) * 12
                });
            }

            let frames = 0;
            function renderConfetti() {
                ctx.clearRect(0, 0, w, h);
                frames++;
                let active = false;

                particles.forEach(p => {
                    p.x += p.vx;
                    p.y += p.vy;
                    p.vy += 0.35;
                    p.vx *= 0.98;
                    p.alpha -= 0.008;
                    p.rotation += p.rotationSpeed;

                    if (p.alpha > 0) {
                        active = true;
                        ctx.save();
                        ctx.translate(p.x, p.y);
                        ctx.rotate((p.rotation * Math.PI) / 180);
                        ctx.fillStyle = p.color;
                        ctx.globalAlpha = p.alpha;
                        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 1.5);
                        ctx.restore();
                    }
                });

                if (active && frames < 200) {
                    requestAnimationFrame(renderConfetti);
                } else {
                    ctx.clearRect(0, 0, w, h);
                    canvas.style.display = 'none';
                }
            }
            renderConfetti();
        }

        function printCertificate() {
            const studentName = document.getElementById('student-cert-name').value || 'Học Sinh Lịch Sử 8';
            alert(`🎉 Chứng Nhận Danh Dự: "${studentName}" đã hoàn thành xuất sắc thử thách với số điểm ${quizScore}/100! Đang mở cửa sổ in...`);
            window.print();
        }

        // --- E. PHÒNG TRÌNH CHIẾU BÁO CÁO (CINEMA PRESENTATION SUITE) ---
        let currentPresentationSlide = 1;
        let isPresAudioPlaying = false;
        let presAudioElement = null;

        function openPresentationSuite(groupId = 1) {
            currentPresentationSlide = groupId;
            document.getElementById('presentation-suite-modal').classList.remove('hidden');
            document.getElementById('presentation-suite-modal').classList.add('flex');
            renderPresentationSlide(groupId);
            playBassDrum(120, 0.4, 0.8);
        }

        function closePresentationSuite() {
            if (isPresAudioPlaying && presAudioElement) {
                presAudioElement.pause();
                isPresAudioPlaying = false;
            }
            document.getElementById('presentation-suite-modal').classList.add('hidden');
            document.getElementById('presentation-suite-modal').classList.remove('flex');
            if (document.fullscreenElement) {
                document.exitFullscreen().catch(() => {});
            }
        }

        function renderPresentationSlide(groupId) {
            currentPresentationSlide = groupId;
            const g = GROUPS_DATA[groupId];
            if (!g) return;

            for (let i = 1; i <= 4; i++) {
                const tab = document.getElementById(`pres-tab-${i}`);
                if (tab) {
                    if (i === groupId) {
                        tab.className = "cursor-pointer px-3 py-1.5 rounded-lg font-bold text-amber-300 bg-amber-950 border border-amber-500/40";
                    } else {
                        tab.className = "cursor-pointer px-3 py-1.5 rounded-lg font-medium text-stone-400 hover:text-stone-200";
                    }
                }
            }

            document.getElementById('pres-group-badge').textContent = `CHIẾN DỊCH SỐ ${groupId}`;
            document.getElementById('pres-group-period').textContent = g.period;
            document.getElementById('pres-group-title').textContent = g.topic;
            document.getElementById('pres-slide-num').textContent = groupId;
            document.getElementById('pres-img').src = g.mapImg;
            document.getElementById('pres-teacher-feedback').textContent = `"${g.teacherFeedback || 'Đạt yêu cầu sư phạm chuẩn mực, phân tích sâu sắc.'}"`;

            const summaryContainer = document.getElementById('pres-student-summary');
            summaryContainer.innerHTML = `
                <div class="space-y-2">
                    <p><strong class="text-amber-400">1. Bối cảnh & Nguyên nhân:</strong> ${g.causes || g.desc}</p>
                    <p><strong class="text-amber-400">2. Diễn biến chủ chốt:</strong> ${g.events || 'Nghĩa quân bí mật hành quân, chia các mũi giáp công mãnh liệt.'}</p>
                    <p><strong class="text-amber-400">3. Ý nghĩa & Nghệ thuật quân sự:</strong> ${g.meaning || g.historicalSignificance}</p>
                </div>
            `;

            if (isPresAudioPlaying && presAudioElement) {
                presAudioElement.pause();
                isPresAudioPlaying = false;
                document.getElementById('pres-audio-icon').className = "fa-solid fa-play";
            }
        }

        function nextPresentationSlide() {
            let next = currentPresentationSlide + 1;
            if (next > 4) next = 1;
            renderPresentationSlide(next);
        }

        function prevPresentationSlide() {
            let prev = currentPresentationSlide - 1;
            if (prev < 1) prev = 4;
            renderPresentationSlide(prev);
        }

        function togglePresentFullscreen() {
            const modal = document.getElementById('presentation-suite-modal');
            if (!document.fullscreenElement) {
                if (modal.requestFullscreen) modal.requestFullscreen();
            } else {
                if (document.exitFullscreen) document.exitFullscreen();
            }
        }

        function togglePresentationAudio() {
            const g = GROUPS_DATA[currentPresentationSlide];
            const icon = document.getElementById('pres-audio-icon');

            if (isPresAudioPlaying && presAudioElement) {
                presAudioElement.pause();
                isPresAudioPlaying = false;
                if (icon) icon.className = "fa-solid fa-play";
            } else {
                if (g.audioSrc) {
                    if (!presAudioElement) {
                        presAudioElement = new Audio();
                    }
                    presAudioElement.src = g.audioSrc;
                    presAudioElement.play().catch(e => console.log(e));
                    isPresAudioPlaying = true;
                    if (icon) icon.className = "fa-solid fa-pause";

                    presAudioElement.onended = () => {
                        isPresAudioPlaying = false;
                        if (icon) icon.className = "fa-solid fa-play";
                    };
                } else {
                    playQuangTrungSpeech();
                }
            }
        }

        window.addEventListener('keydown', (e) => {
            const presModal = document.getElementById('presentation-suite-modal');
            if (presModal && !presModal.classList.contains('hidden')) {
                if (e.key === 'ArrowRight' || e.key === 'PageDown') {
                    nextPresentationSlide();
                } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
                    prevPresentationSlide();
                } else if (e.key === ' ' || e.key === 'Spacebar') {
                    e.preventDefault();
                    togglePresentationAudio();
                } else if (e.key === 'Escape') {
                    closePresentationSuite();
                }
            }
        });

        window.addEventListener('DOMContentLoaded', () => {
            initEmberCanvas();
        });
'''

# Find ONLY the last </script> tag
last_script_pos = html.rfind('</script>')
if last_script_pos != -1:
    html = html[:last_script_pos] + js_code + '\n    ' + html[last_script_pos:]

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: index.html cleanly updated with single JS block!")
