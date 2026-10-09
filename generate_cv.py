import os
from fpdf import FPDF

class CV_PDF(FPDF):
    def __init__(self, lang="EN"):
        super().__init__()
        self.lang = lang
        self.set_auto_page_break(auto=True, margin=15)
        # Fonts
        self.add_font("Arial_B", "", "/System/Library/Fonts/Supplemental/Arial Bold.ttf", uni=True)
        self.add_font("Arial", "", "/System/Library/Fonts/Supplemental/Arial.ttf", uni=True)
        self.add_font("Arial_I", "", "/System/Library/Fonts/Supplemental/Arial Italic.ttf", uni=True)
        self.add_font("Arial", "B", "/System/Library/Fonts/Supplemental/Arial Bold.ttf", uni=True)
        self.add_font("Arial", "I", "/System/Library/Fonts/Supplemental/Arial Italic.ttf", uni=True)
        self.add_font("FAS", "", "assets/fonts/fa-solid-900.ttf", uni=True)
        self.add_font("FAB", "", "assets/fonts/fa-brands-400.ttf", uni=True)

    def write_icon_text(self, icon_font, icon_char, text_font, text_str, font_sz=10):
        self.set_font(icon_font, '', font_sz)
        self.cell(5, 5, icon_char, 0, 0, 'L')
        self.set_font(text_font, '', font_sz)
        self.cell(0, 5, text_str, 0, 1, 'L')

    def header(self):
        if self.page_no() > 1:
            return
            
        # Insert Profile Picture on top right
        self.image("images/profil_yudha_3.jpg", 165, 12, 28)
        
        self.set_font('Arial_B', '', 24)
        self.set_text_color(44, 62, 80)
        self.cell(140, 10, 'YUDHA STYAWAN', 0, 1, 'L')
        self.ln(2)

        self.set_font('Arial', '', 12)
        self.set_text_color(127, 140, 141)
        sub = "Lecturer, Geophysicist & Computational Seismology Enthusiast" if self.lang == "EN" else "Dosen, Ahli Geofisika & Penggiat Komputasi Seismologi"
        self.multi_cell(140, 5, sub)
        self.ln(3)

        self.set_text_color(52, 152, 219)
        # Email
        self.write_icon_text('FAS', '\uf0e0', 'Arial', "yudha.styawan@tg.itera.ac.id | yudhastyawan26@gmail.com")
        # Web
        self.write_icon_text('FAS', '\uf0ac', 'Arial', "yudhastyawan.github.io")
        
        self.set_text_color(127, 140, 141)
        self.ln(1)
        # Scholar
        self.write_icon_text('FAS', '\uf19d', 'Arial', "Google Scholar: s.itera.id/yudhascholar")
        # ORCID
        self.write_icon_text('FAS', '\uf2c1', 'Arial', "ORCID: 0000-0002-0891-5745")
        # GitHub
        self.write_icon_text('FAB', '\uf09b', 'Arial', "GitHub: github.com/yudhastyawan")
        
        self.ln(3)
        self.set_draw_color(189, 195, 199)
        self.line(10, self.get_y(), 155, self.get_y())
        self.ln(3)

    def section_title(self, icon, title):
        self.ln(2)
        self.set_font('FAS', '', 14)
        self.set_text_color(44, 62, 80)
        self.cell(8, 10, icon, 0, 0, 'L')
        
        self.set_font('Arial_B', '', 14)
        self.cell(0, 10, title.upper(), 0, 1, 'L')
        
        self.set_draw_color(52, 152, 219)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def add_entry(self, title, date, org, description=None, sub_details=None):
        self.set_font('Arial_B', '', 11)
        self.set_text_color(44, 62, 80)
        self.cell(140, 6, title, 0, 0, 'L')
        
        self.set_font('Arial_I', '', 11)
        self.set_text_color(127, 140, 141)
        self.cell(0, 6, date, 0, 1, 'R')

        if org:
            self.set_font('Arial', '', 11)
            self.set_text_color(52, 73, 94)
            self.cell(0, 6, org, 0, 1, 'L')

        if description:
            self.set_font('Arial', '', 10)
            self.set_text_color(85, 85, 85)
            self.multi_cell(0, 5, description)
            self.ln(1)

        if sub_details:
            self.set_text_color(85, 85, 85)
            for key, val in sub_details.items():
                self.set_font('Arial_B', '', 10)
                self.write(5, f"{key}: ")
                self.set_font('Arial', '', 10)
                self.multi_cell(0, 5, val)
            self.ln(1)
        self.ln(3)

    def add_list_item(self, text):
        self.set_font('Arial', '', 10)
        self.set_text_color(85, 85, 85)
        self.set_x(12)
        self.cell(5, 5, "-", 0, 0)
        self.multi_cell(0, 5, text, markdown=True)
        self.ln(1)

def generate_en_cv():
    pdf = CV_PDF(lang="EN")
    pdf.add_page()

    # PROFESSIONAL EXPERIENCE (\uf0b1 briefcase)
    pdf.section_title('\uf0b1', "Professional Experience")
    pdf.add_entry(
        title="Secretary at Earthquake and Tsunami Disaster Mitigation Center",
        date="2025 - Present",
        org="Institut Teknologi Sumatera, Indonesia",
        description="Assisting in the management and coordination of center activities, including research programs, public outreach, and administrative duties related to disaster mitigation."
    )
    pdf.add_entry(
        title="Lecturer - Geophysical Engineering",
        date="2022 - Present",
        org="Institut Teknologi Sumatera, Indonesia",
        description="Teaching undergraduate (B.Sc.) courses in geophysics. Mentoring students in practical applications and research projects. Teaching focus areas: seismology, geodynamics, seismic data analysis, engineering seismology, and computational modeling."
    )
    pdf.add_entry(
        title="Laboratory Staff - Geophysical Engineering",
        date="2018 - 2021",
        org="Institut Teknologi Sumatera, Indonesia",
        description="Managing laboratory equipment, assisting students during practical sessions, and maintaining geophysical instruments for field measurements."
    )

    # EDUCATION (\uf19d graduation cap)
    pdf.section_title('\uf19d', "Education")
    pdf.add_entry(
        title="Master of Science (M.Sc.) in Geophysics",
        date="2021",
        org="National Central University, Taiwan",
        sub_details={
            "Thesis": "Characteristics of Seismic Attenuation in Sumatra Subduction Zone, Indonesia",
            "Advisors": "Asst. Prof. Chun-Hsiang Kuo, Prof. Bor-Shouh Huang"
        }
    )
    pdf.add_entry(
        title="Bachelor of Engineering (S.T.) in Geophysical Engineering",
        date="2018",
        org="Institut Teknologi Sumatera, Indonesia",
        sub_details={
            "Thesis": "Lindu Software: Aplikasi Pengolahan Data Seismologi Berbasis Python untuk Tomografi Waktu Tempuh [Lindu Software: Python-Based Seismological Data Processing Application for Travel Time Tomography]",
            "Advisors": "Dr. Tedi Yudistira, S.Si., M.Si., Ruhul Firdaus, S.T., M.T."
        }
    )

    # GRANTS (\uf4c0 money check)
    pdf.section_title('\uf4c0', "Grants & Research Funding")
    pdf.add_entry(title="ITERA Expertise-Based Research Grant", date="2025", org="Institut Teknologi Sumatera (ITERA)", description="Application of Brownian Passage Time Method as Recurrence Interval Calculation on Fault Earthquakes in the Western Part of Sunda-Java Strait to Support the Update of Seismic Hazard Assessment Model in Lampung Region")
    pdf.add_entry(title="ITERA Assignment Research Grant", date="2025", org="Institut Teknologi Sumatera (ITERA)", description="Policy Brief Response of Lampung Province City and Regency Towards Megathrust")
    pdf.add_entry(title="ITERA Scientific Group Strengthening Research Grant", date="2025", org="Institut Teknologi Sumatera (ITERA)", description="Azimuth Variation Analysis on Single Station HVSR Measurement in Umbul Niti Geothermal Manifestation, Jatimulyo Village, South Lampung Regency")
    pdf.add_entry(title="ITERA Community Service Funding", date="2025", org="Institut Teknologi Sumatera (ITERA)", description="Early Preparedness: Forming a Tsunami Responsive Generation in Coastal Schools")
    pdf.add_entry(title="ITERA Beginner Lecturer Research Grant", date="2024", org="Institut Teknologi Sumatera (ITERA)", description="Updating Seismic Activity Modeling and Vs30 on Ground Motion Prediction Equations for Long-term Seismic Hazard Assessment in Sumatra, Indonesia: A Probabilistic Approach")

    # PUBLICATIONS (\uf02d book)
    pdf.section_title('\uf02d', "Recent Publications")
    pubs = [
        "Alif, S. M., Anggara, O., Perdana, R. S., Wulandari, R., & **Styawan, Y.** (2026). Earthquake potential and seismic hazard in Southern Sumatra, Indonesia: Insights from different GNSS velocity sets. __Journal of Asian Earth Sciences__, __311__, 107217. [https://doi.org/10.1016/j.jseaes.2026.107217](https://doi.org/10.1016/j.jseaes.2026.107217)",
        "Antosia, R. M., Endryanti, W. M., Farduwin, A., Rizki, R., & **Styawan, Y.** (2026). Soil characterization for seismic vulnerability and preliminary subsidence assessment based on microtremor analysis in Sukarame District, Bandar Lampung. __Journal of Degraded and Mining Lands Management__, __13__(3), 10439-10450. [https://doi.org/10.15243/jdmlm.2026.133.10439](https://doi.org/10.15243/jdmlm.2026.133.10439)",
        "Junian, W. E., **Styawan, Y.**, Prasetyo, N., & Paembonan, A. Y. (2026). Applying the one-to-one-based optimizer (OOBO) algorithm for one-dimensional inversion modeling of magnetotellurics data. __Pure and Applied Geophysics__, __183__(6), 2873-2890. [https://doi.org/10.1007/s00024-026-03998-x](https://doi.org/10.1007/s00024-026-03998-x)",
        "Wulandari, R., Suhendi, C., & **Styawan, Y.** (2026). Receiver-fault variability and depth-dependent Coulomb stress changes in the 2019 Mw 7.2 Halmahera earthquake sequence. __Jurnal Geocelebes__, 145-159. [https://doi.org/10.70561/geocelebes.v10i2.47046](https://doi.org/10.70561/geocelebes.v10i2.47046)",
        "Wulandari, R., **Styawan, Y.**, & Chan, C.-H. (2026). Enhancing seismic hazard preparation in Lampung, Sumatra: Improved magnitude conversion, seismicity smoothing, and area source modeling. __Indonesian Journal on Geoscience__, __13__(2), 221-241. [https://doi.org/10.17014/ijog.13.2.221-241](https://doi.org/10.17014/ijog.13.2.221-241)",
        "**Styawan, Y.** (2025). Optimizing seismic b-values in the Java region through Voronoi-based OK1993 modelling. __JGE (Jurnal Geofisika Eksplorasi)__, __11__(2), 109-121. [https://doi.org/10.23960/jge.v11i2.489](https://doi.org/10.23960/jge.v11i2.489)",
        "**Styawan, Y.** (2025). QuakeSee: Aplikasi cross-platform Python berbasis web untuk otomasi dan aksesibilitas dalam pengunduhan data gempa terbuka [QuakeSee: A cross-platform web-based Python application for automation and accessibility in downloading open earthquake data]. __GeoScienceEd Journal__, __6__(3), 1292-1301. [https://doi.org/10.29303/goescienceed.v6i3.968](https://doi.org/10.29303/goescienceed.v6i3.968)",
        "Farduwin, A., Nugraha, P. N., **Styawan, Y.**, Lestari, E. Y. P., & Tr, D. P. J. (2025). Site effects identification using HVSR method in Cisarua hot spring area, Natar, South Lampung. __JGE (Jurnal Geofisika Eksplorasi)__, __11__(2), 151-162. [https://doi.org/10.23960/jge.v11i2.494](https://doi.org/10.23960/jge.v11i2.494)",
        "Hamidah, I. F., Farduwin, A., **Styawan, Y.**, Nurfitriani, I., Prasetyo, N., Junian, W. E., & Wulandari, R. (2025). Analisis ancaman gempa Lombok menggunakan metode spasial temporal a-value dan b-value periode 1964-2022 [Lombok earthquake hazard analysis using spatio-temporal a-value and b-value method for the period of 1964-2022]. __Wahana Fisika__, __10__(1), 12-26. [https://doi.org/10.17509/wafi.v10i1.76470](https://doi.org/10.17509/wafi.v10i1.76470)"
    ]
    for p in pubs:
        pdf.add_list_item(p)

    # OPEN SOURCE SOFTWARE (\uf121 code)
    pdf.section_title('\uf121', "Open Source Software")
    pdf.add_list_item("**SeisBox** ([https://github.com/yudhastyawan/SeisBox](https://github.com/yudhastyawan/SeisBox)): A Rust-based native desktop app for downloading open-source catalog and seismogram data, visualizing waveforms, picking seismic wave phases, computing Coulomb stress changes, analyzing HVSR, and performing 1D Vs inversions.")
    pdf.add_list_item("**QuakeSee** ([https://github.com/yudhastyawan/quakesee](https://github.com/yudhastyawan/quakesee)): A Python GUI program for downloading and interactively visualizing open-source seismic data to aid undergraduate seismology practicums.")
    pdf.add_list_item("**SeisWave** ([https://github.com/yudhastyawan/seiswave](https://github.com/yudhastyawan/seiswave)): A robust Python and Fortran framework for surface wave modeling and Full f-c Spectrum Inversion, utilizing dispersion image code from Computer Programs in Seismology.")
    pdf.add_list_item("**Lindu Software** ([https://github.com/Computation-Geophysics-TG-Itera/lindu-software](https://github.com/Computation-Geophysics-TG-Itera/lindu-software)): An open-source Python GUI tool for earthquake location, HypoDD relocation, and traveltime tomography, though its development is currently paused.")

    # SKILLS (\uf0ad wrench)
    pdf.section_title('\uf0ad', "Technical Skills")
    pdf.set_font('Arial_B', '', 10)
    pdf.set_text_color(44, 62, 80)
    
    skills = [
        ("Programming & Dev", "Python, Rust, Julia, Fortran, C++ | PyQt, Git, GMT, Bash / CLI, Linux, LaTeX"),
        ("Geophysical Tools", "Seismometers (Primary); Gravity, Magnetic, and Electrical instruments"),
        ("Professional Interests", "Computational Seismology, Engineering Seismology, Geophysics Software Development")
    ]
    for cat, items in skills:
        pdf.set_font('Arial_B', '', 10)
        pdf.cell(45, 6, cat, 0, 0, 'L')
        pdf.set_font('Arial', '', 10)
        pdf.cell(0, 6, items, 0, 1, 'L')

    os.makedirs('assets/pdf', exist_ok=True)
    pdf.output('assets/pdf/Yudha_Styawan_CV_EN.pdf')

def generate_id_cv():
    pdf = CV_PDF(lang="ID")
    pdf.add_page()

    # PROFESSIONAL EXPERIENCE
    pdf.section_title('\uf0b1', "Pengalaman Profesional")
    pdf.add_entry(
        title="Sekretaris pada Pusat Mitigasi Bencana Gempa dan Tsunami",
        date="2025 - Sekarang",
        org="Institut Teknologi Sumatera, Indonesia",
        description="Membantu manajemen dan koordinasi kegiatan pusat studi, termasuk program penelitian, pengabdian masyarakat, dan tugas administratif terkait mitigasi bencana."
    )
    pdf.add_entry(
        title="Dosen Program Studi Teknik Geofisika",
        date="2022 - Sekarang",
        org="Institut Teknologi Sumatera, Indonesia",
        description="Mengajar mahasiswa program sarjana (S1) di bidang geofisika. Membimbing mahasiswa dalam penelitian dan aplikasi lapangan. Fokus pengajaran: seismologi, geodinamika, analisis data seismik, seismologi teknik, dan pemodelan komputasi."
    )
    pdf.add_entry(
        title="Staf Laboratorium Teknik Geofisika",
        date="2018 - 2021",
        org="Institut Teknologi Sumatera, Indonesia",
        description="Mengelola peralatan laboratorium, mendampingi mahasiswa selama kegiatan praktikum, serta melakukan pemeliharaan instrumen geofisika untuk pengukuran lapangan."
    )

    # EDUCATION
    pdf.section_title('\uf19d', "Pendidikan")
    pdf.add_entry(
        title="Master of Science (M.Sc.) Program Geofisika",
        date="2021",
        org="Departemen Ilmu Bumi, National Central University, Taiwan",
        sub_details={
            "Tesis": "Characteristics of Seismic Attenuation in Sumatra Subduction Zone, Indonesia",
            "Pembimbing": "Asst. Prof. Chun-Hsiang Kuo, Prof. Bor-Shouh Huang"
        }
    )
    pdf.add_entry(
        title="Sarjana Teknik (S.T.) Program Studi Teknik Geofisika",
        date="2018",
        org="Institut Teknologi Sumatera, Indonesia",
        sub_details={
            "Skripsi": "Lindu Software: Aplikasi Pengolahan Data Seismologi Berbasis Python untuk Tomografi Waktu Tempuh",
            "Pembimbing": "Dr. Tedi Yudistira, S.Si., M.Si., Ruhul Firdaus, S.T., M.T."
        }
    )

    # GRANTS
    pdf.section_title('\uf4c0', "Pendanaan Penelitian dan Pengabdian")
    pdf.add_entry(title="Penelitian Berbasis Kepakaran ITERA", date="2025", org="Institut Teknologi Sumatera (ITERA)", description="Penerapan Metode Brownian Passage Time Sebagai Perhitungan Recurrence Interval Pada Gempa Bumi Patahan di Selat Sunda-Jawa Bagian Barat Untuk Mendukung Pembaharuan Model Penilaian Bahaya Seismik Di Wilayah Lampung")
    pdf.add_entry(title="Penelitian Penugasan ITERA", date="2025", org="Institut Teknologi Sumatera (ITERA)", description="Policy Brief Response Kota dan Kabupaten Prov Lampung Terhadap Megathrust")
    pdf.add_entry(title="Penelitan Penguatan Kelompok Keilmuan ITERA", date="2025", org="Institut Teknologi Sumatera (ITERA)", description="Analisis Variasi Azimuth Pada Pengukuran HVSR Single Station Di Manifestasi Geotermal Umbul Niti, Desa Jatimulyo, Kabupaten Lampung Selatan")
    pdf.add_entry(title="Pendanaan Pengabdian Kepada Masyarakat ITERA (PKK)", date="2025", org="Institut Teknologi Sumatera (ITERA)", description="Siaga Sejak Dini: Membentuk Generasi Tanggap Tsunami Di Sekolah Pesisir")
    pdf.add_entry(title="Penelitian Dosen Pemula ITERA", date="2024", org="Institut Teknologi Sumatera (ITERA)", description="Pemutakhiran Pemodelan Aktivitas Seismik dan Vs30 pada Ground Motion Prediction Equations untuk Penilaian Jangka Panjang Bahaya Gempa Bumi di Sumatera, Indonesia: Pendekatan Probabilistik")

    # PUBLICATIONS
    pdf.section_title('\uf02d', "Publikasi Terkini")
    pubs = [
        "Alif, S. M., Anggara, O., Perdana, R. S., Wulandari, R., & **Styawan, Y.** (2026). Earthquake potential and seismic hazard in Southern Sumatra, Indonesia: Insights from different GNSS velocity sets. __Journal of Asian Earth Sciences__, __311__, 107217. [https://doi.org/10.1016/j.jseaes.2026.107217](https://doi.org/10.1016/j.jseaes.2026.107217)",
        "Antosia, R. M., Endryanti, W. M., Farduwin, A., Rizki, R., & **Styawan, Y.** (2026). Soil characterization for seismic vulnerability and preliminary subsidence assessment based on microtremor analysis in Sukarame District, Bandar Lampung. __Journal of Degraded and Mining Lands Management__, __13__(3), 10439-10450. [https://doi.org/10.15243/jdmlm.2026.133.10439](https://doi.org/10.15243/jdmlm.2026.133.10439)",
        "Junian, W. E., **Styawan, Y.**, Prasetyo, N., & Paembonan, A. Y. (2026). Applying the one-to-one-based optimizer (OOBO) algorithm for one-dimensional inversion modeling of magnetotellurics data. __Pure and Applied Geophysics__, __183__(6), 2873-2890. [https://doi.org/10.1007/s00024-026-03998-x](https://doi.org/10.1007/s00024-026-03998-x)",
        "Wulandari, R., Suhendi, C., & **Styawan, Y.** (2026). Receiver-fault variability and depth-dependent Coulomb stress changes in the 2019 Mw 7.2 Halmahera earthquake sequence. __Jurnal Geocelebes__, 145-159. [https://doi.org/10.70561/geocelebes.v10i2.47046](https://doi.org/10.70561/geocelebes.v10i2.47046)",
        "Wulandari, R., **Styawan, Y.**, & Chan, C.-H. (2026). Enhancing seismic hazard preparation in Lampung, Sumatra: Improved magnitude conversion, seismicity smoothing, and area source modeling. __Indonesian Journal on Geoscience__, __13__(2), 221-241. [https://doi.org/10.17014/ijog.13.2.221-241](https://doi.org/10.17014/ijog.13.2.221-241)",
        "**Styawan, Y.** (2025). Optimizing seismic b-values in the Java region through Voronoi-based OK1993 modelling. __JGE (Jurnal Geofisika Eksplorasi)__, __11__(2), 109-121. [https://doi.org/10.23960/jge.v11i2.489](https://doi.org/10.23960/jge.v11i2.489)",
        "**Styawan, Y.** (2025). QuakeSee: Aplikasi cross-platform Python berbasis web untuk otomasi dan aksesibilitas dalam pengunduhan data gempa terbuka. __GeoScienceEd Journal__, __6__(3), 1292-1301. [https://doi.org/10.29303/goescienceed.v6i3.968](https://doi.org/10.29303/goescienceed.v6i3.968)",
        "Farduwin, A., Nugraha, P. N., **Styawan, Y.**, Lestari, E. Y. P., & Tr, D. P. J. (2025). Site effects identification using HVSR method in Cisarua hot spring area, Natar, South Lampung. __JGE (Jurnal Geofisika Eksplorasi)__, __11__(2), 151-162. [https://doi.org/10.23960/jge.v11i2.494](https://doi.org/10.23960/jge.v11i2.494)",
        "Hamidah, I. F., Farduwin, A., **Styawan, Y.**, Nurfitriani, I., Prasetyo, N., Junian, W. E., & Wulandari, R. (2025). Analisis ancaman gempa Lombok menggunakan metode spasial temporal a-value dan b-value periode 1964-2022. __Wahana Fisika__, __10__(1), 12-26. [https://doi.org/10.17509/wafi.v10i1.76470](https://doi.org/10.17509/wafi.v10i1.76470)"
    ]
    for p in pubs:
        pdf.add_list_item(p)

    # OPEN SOURCE SOFTWARE
    pdf.section_title('\uf121', "Pengembangan Software")
    pdf.add_list_item("**SeisBox** ([https://github.com/yudhastyawan/SeisBox](https://github.com/yudhastyawan/SeisBox)): Aplikasi desktop native berbasis Rust untuk mengunduh data katalog dan seismogram terbuka, memvisualisasikan bentuk gelombang, melakukan picking fase gelombang seismik, menghitung perubahan tegangan Coulomb, menganalisis HVSR, serta melakukan inversi Vs 1D.")
    pdf.add_list_item("**QuakeSee** ([https://github.com/yudhastyawan/quakesee](https://github.com/yudhastyawan/quakesee)): Program GUI berbasis Python untuk mengunduh dan memvisualisasikan data seismik terbuka secara interaktif guna mendukung praktikum seismologi mahasiswa tingkat sarjana.")
    pdf.add_list_item("**SeisWave** ([https://github.com/yudhastyawan/seiswave](https://github.com/yudhastyawan/seiswave)): Framework Python dan Fortran yang kuat untuk pemodelan gelombang permukaan dan Inversi Spektrum f-c Penuh, memanfaatkan kode citra dispersi dari Computer Programs in Seismology.")
    pdf.add_list_item("**Lindu Software** ([https://github.com/Computation-Geophysics-TG-Itera/lindu-software](https://github.com/Computation-Geophysics-TG-Itera/lindu-software)): Perangkat lunak GUI Python bersumber terbuka untuk penentuan lokasi gempa, relokasi HypoDD, dan tomografi waktu tempuh (pengembangan saat ini dihentikan sementara).")

    # SKILLS
    pdf.section_title('\uf0ad', "Keahlian Teknis")
    pdf.set_font('Arial_B', '', 10)
    pdf.set_text_color(44, 62, 80)
    
    skills = [
        ("Pemrograman & Dev", "Python, Rust, Julia, Fortran, C++ | PyQt, Git, GMT, Bash / CLI, Linux, LaTeX"),
        ("Alat Geofisika", "Seismometer (Utama); Instrumen Gravitasi, Magnetik, dan Geolistrik"),
        ("Minat Profesional", "Seismologi Komputasi, Seismologi Teknik, Pengembangan Software Geofisika")
    ]
    for cat, items in skills:
        pdf.set_font('Arial_B', '', 10)
        pdf.cell(45, 6, cat, 0, 0, 'L')
        pdf.set_font('Arial', '', 10)
        pdf.cell(0, 6, items, 0, 1, 'L')

    os.makedirs('assets/pdf', exist_ok=True)
    pdf.output('assets/pdf/Yudha_Styawan_CV_ID.pdf')

if __name__ == "__main__":
    generate_en_cv()
    generate_id_cv()
    print("CV PDFs generated successfully in assets/pdf/")
