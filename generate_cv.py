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
        self.add_font("FAS", "", "assets/fonts/fa-solid-900.ttf", uni=True)
        self.add_font("FAB", "", "assets/fonts/fa-brands-400.ttf", uni=True)

    def write_icon_text(self, icon_font, icon_char, text_font, text_str, font_sz=10):
        self.set_font(icon_font, '', font_sz)
        self.cell(5, 5, icon_char, 0, 0, 'L')
        self.set_font(text_font, '', font_sz)
        self.cell(0, 5, text_str, 0, 1, 'L')

    def header(self):
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
        self.write_icon_text('FAS', '\uf19d', 'Arial', "Google Scholar: s.id/yudhascholar")
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
        self.multi_cell(0, 5, text)
        self.ln(1)

def generate_en_cv():
    pdf = CV_PDF(lang="EN")
    pdf.add_page()

    # PROFESSIONAL EXPERIENCE (\uf0b1 briefcase)
    pdf.section_title('\uf0b1', "Professional Experience")
    pdf.add_entry(
        title="Secretary at Earthquake and Tsunami Disaster Mitigation Center",
        date="2025 - Present",
        org="Institut Teknologi Sumatera, Indonesia"
    )
    pdf.add_entry(
        title="Lecturer - Geophysical Engineering",
        date="2022 - Present",
        org="Institut Teknologi Sumatera, Indonesia",
        description="Teaching undergraduate courses in geophysics. Mentoring students in practical applications and research projects. Research focus areas: seismic data analysis, engineering seismology, and computational modeling."
    )
    pdf.add_entry(
        title="Laboratory Staff - Geophysical Engineering",
        date="2018 - 2021",
        org="Institut Teknologi Sumatera, Indonesia"
    )

    # GRANTS (\uf4c0 money check)
    pdf.section_title('\uf4c0', "Grants & Research Funding")
    pdf.add_entry(title="ITERA Expertise-Based Research Grant", date="2025", org="", description="Application of Brownian Passage Time Method as Recurrence Interval Calculation on Fault Earthquakes in the Western Part of Sunda-Java Strait to Support the Update of Seismic Hazard Assessment Model in Lampung Region")
    pdf.add_entry(title="ITERA Assignment Research Grant", date="2025", org="", description="Policy Brief Response of Lampung Province City and Regency Towards Megathrust")
    pdf.add_entry(title="ITERA Scientific Group Strengthening Research Grant", date="2025", org="", description="Azimuth Variation Analysis on Single Station HVSR Measurement in Umbul Niti Geothermal Manifestation, Jatimulyo Village, South Lampung Regency")
    pdf.add_entry(title="ITERA Community Service Funding", date="2025", org="", description="Early Preparedness: Forming a Tsunami Responsive Generation in Coastal Schools")
    pdf.add_entry(title="ITERA Beginner Lecturer Research Grant", date="2024", org="", description="Updating Seismic Activity Modeling and Vs30 on Ground Motion Prediction Equations for Long-term Seismic Hazard Assessment in Sumatra, Indonesia: A Probabilistic Approach")

    # PUBLICATIONS (\uf02d book)
    pdf.section_title('\uf02d', "Recent Publications")
    pubs = [
        "Wulandari, R., & Styawan, Y. (2025). Enhancing seismic hazard preparation in Lampung, Sumatra: Improved magnitude conversion, seismicity smoothing, and area source modeling. Indonesian Journal on Geoscience. (Accepted for publication)",
        "Styawan, Y. (2025). Optimizing seismic b-values in the java region through voronoi-based ok1993 modelling. JGE (Jurnal Geofisika Eksplorasi), 11(2), 109-121. https://doi.org/10.23960/jge.v11i2.489",
        "Styawan, Y. (2024). Quakesee: Aplikasi cross-platform python berbasis web untuk otomasi dan aksesibilitas dalam pengunduhan data gempa terbuka. GeoScienceEd Journal, 6(3), 1292-1301. https://doi.org/10.29303/goescienceed.v6i3.968",
        "Farduwin, A., Nugraha, P. N., Styawan, Y., Lestari, E. Y. P., & Tr, D. P. J. (2025). Site effects identification using hvsr method in cisarua hot spring area, natar, south lampung. JGE (Jurnal Geofisika Eksplorasi), 11(2), 151-162. https://doi.org/10.23960/jge.v11i2.494",
        "Hamidah, I. F., Farduwin, A., Styawan, Y., Nurfitriani, I., Prasetyo, N., Junian, W. E., & Wulandari, R. (2025). Analisis ancaman gempa lombok menggunakan metode spasial temporal a-value dan b-value periode 1964- 2022. Wahana Fisika, 10(1), 12-26. https://doi.org/10.17509/wafi.v10i1.76470"
    ]
    for p in pubs:
        pdf.add_list_item(p)

    # OPEN SOURCE SOFTWARE (\uf121 code)
    pdf.section_title('\uf121', "Open Source Software")
    pdf.add_list_item("SeisWave: https://github.com/yudhastyawan/seiswave")
    pdf.add_list_item("QuakeSee: https://github.com/yudhastyawan/quakesee")
    pdf.add_list_item("Lindu Software: https://github.com/Computation-Geophysics-TG-Itera/lindu-software")

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
            "Skripsi": "Lindu Software: Aplikasi Pengolahan Data Seismologi Berbasis Python untuk Tomografi Waktu Tempuh",
            "Advisors": "Dr. Tedi Yudistira, S.Si., M.Si., Ruhul Firdaus, S.T., M.T."
        }
    )

    # SKILLS (\uf0ad wrench)
    pdf.section_title('\uf0ad', "Technical Skills")
    pdf.set_font('Arial_B', '', 10)
    pdf.set_text_color(44, 62, 80)
    
    skills = [
        ("Programming & Dev", "Julia, Python, PyQt, Fortran, C++, Git, GMT, Bash / CLI"),
        ("Geophysical Tools", "Seismic, Gravity, Magnetic, and Electrical instruments"),
        ("Software & OS", "Linux, LaTeX"),
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
        org="Institut Teknologi Sumatera, Indonesia"
    )
    pdf.add_entry(
        title="Dosen Program Studi Teknik Geofisika",
        date="2022 - Sekarang",
        org="Institut Teknologi Sumatera, Indonesia",
        description="Mengajar program sarjana di bidang geofisika. Membimbing mahasiswa dalam penelitian dan aplikasi lapangan. Fokus penelitian: analisis data seismik, seismologi teknik, dan pemodelan komputasi."
    )
    pdf.add_entry(
        title="Staf Laboratorium Teknik Geofisika",
        date="2018 - 2021",
        org="Institut Teknologi Sumatera, Indonesia"
    )

    # GRANTS
    pdf.section_title('\uf4c0', "Pendanaan Penelitian dan Pengabdian")
    pdf.add_entry(title="Penelitian Berbasis Kepakaran ITERA", date="2025", org="", description="Penerapan Metode Brownian Passage Time Sebagai Perhitungan Recurrence Interval Pada Gempa Bumi Patahan di Selat Sunda-Jawa Bagian Barat Untuk Mendukung Pembaharuan Model Penilaian Bahaya Seismik Di Wilayah Lampung")
    pdf.add_entry(title="Penelitian Penugasan ITERA", date="2025", org="", description="Policy Brief Response Kota dan Kabupaten Prov Lampung Terhadap Megathrust")
    pdf.add_entry(title="Penelitan Penguatan Kelompok Keilmuan ITERA", date="2025", org="", description="Analisis Variasi Azimuth Pada Pengukuran HVSR Single Station Di Manifestasi Geotermal Umbul Niti, Desa Jatimulyo, Kabupaten Lampung Selatan")
    pdf.add_entry(title="Pendanaan Pengabdian Kepada Masyarakat ITERA (PKK)", date="2025", org="", description="Siaga Sejak Dini: Membentuk Generasi Tanggap Tsunami Di Sekolah Pesisir")
    pdf.add_entry(title="Penelitian Dosen Pemula ITERA", date="2024", org="", description="Pemutakhiran Pemodelan Aktivitas Seismik dan Vs30 pada Ground Motion Prediction Equations untuk Penilaian Jangka Panjang Bahaya Gempa Bumi di Sumatera, Indonesia: Pendekatan Probabilistik")

    # PUBLICATIONS
    pdf.section_title('\uf02d', "Penelitian Terkini")
    pubs = [
        "Wulandari, R., & Styawan, Y. (2025). Enhancing seismic hazard preparation in Lampung, Sumatra: Improved magnitude conversion, seismicity smoothing, and area source modeling. Indonesian Journal on Geoscience. (Accepted for publication)",
        "Styawan, Y. (2025). Optimizing seismic b-values in the java region through voronoi-based ok1993 modelling. JGE (Jurnal Geofisika Eksplorasi), 11(2), 109-121. https://doi.org/10.23960/jge.v11i2.489",
        "Styawan, Y. (2024). Quakesee: Aplikasi cross-platform python berbasis web untuk otomasi dan aksesibilitas dalam pengunduhan data gempa terbuka. GeoScienceEd Journal, 6(3), 1292-1301. https://doi.org/10.29303/goescienceed.v6i3.968",
        "Farduwin, A., Nugraha, P. N., Styawan, Y., Lestari, E. Y. P., & Tr, D. P. J. (2025). Site effects identification using hvsr method in cisarua hot spring area, natar, south lampung. JGE (Jurnal Geofisika Eksplorasi), 11(2), 151-162. https://doi.org/10.23960/jge.v11i2.494",
        "Hamidah, I. F., Farduwin, A., Styawan, Y., Nurfitriani, I., Prasetyo, N., Junian, W. E., & Wulandari, R. (2025). Analisis ancaman gempa lombok menggunakan metode spasial temporal a-value dan b-value periode 1964- 2022. Wahana Fisika, 10(1), 12-26. https://doi.org/10.17509/wafi.v10i1.76470"
    ]
    for p in pubs:
        pdf.add_list_item(p)

    # OPEN SOURCE SOFTWARE
    pdf.section_title('\uf121', "Software yang Sudah Dibuat")
    pdf.add_list_item("SeisWave: https://github.com/yudhastyawan/seiswave")
    pdf.add_list_item("QuakeSee: https://github.com/yudhastyawan/quakesee")
    pdf.add_list_item("Lindu Software: https://github.com/Computation-Geophysics-TG-Itera/lindu-software")

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

    # SKILLS
    pdf.section_title('\uf0ad', "Keahlian Teknis")
    pdf.set_font('Arial_B', '', 10)
    pdf.set_text_color(44, 62, 80)
    
    skills = [
        ("Pemrograman & Dev", "Julia, Python, PyQt, Fortran, C++, Git, GMT, Bash / CLI"),
        ("Alat Geofisika", "Seismik, Gravitasi, Magnetik, dan Geolistrik"),
        ("Perangkat Lunak & OS", "Linux, LaTeX"),
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
