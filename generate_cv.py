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

    def header(self):
        # Insert Profile Picture on top right
        self.image("images/profil_yudha_3.jpg", 165, 12, 28)
        
        self.set_font('Arial_B', '', 24)
        self.set_text_color(44, 62, 80)
        self.cell(140, 10, 'Yudha Styawan', 0, 1, 'L')

        self.set_font('Arial', '', 12)
        self.set_text_color(127, 140, 141)
        sub = "Lecturer, Geophysicist & Computational Seismology Enthusiast" if self.lang == "EN" else "Dosen, Ahli Geofisika & Penggiat Komputasi Seismologi"
        self.cell(140, 7, sub, 0, 1, 'L')

        self.set_font('Arial', '', 10)
        self.set_text_color(52, 152, 219)
        contact = "yudha.styawan@tg.itera.ac.id  |  yudhastyawan26@gmail.com  |  yudhastyawan.github.io"
        self.cell(140, 6, contact, 0, 1, 'L')
        
        self.ln(5)
        self.set_draw_color(189, 195, 199)
        self.line(10, self.get_y(), 155, self.get_y())
        self.ln(5)

    def section_title(self, title):
        self.set_font('Arial_B', '', 14)
        self.set_text_color(44, 62, 80)
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

def generate_en_cv():
    pdf = CV_PDF(lang="EN")
    pdf.add_page()

    # PROFESSIONAL EXPERIENCE
    pdf.section_title("Professional Experience")
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
        org="Institut Teknologi Sumatera, Indonesia",
        description="Managed geophysical instrumentation. Supervised fieldwork activities. Conducted technical training on seismic refraction, Scintrex 6 gravity meter, geomagnetic tools, geoelectrical instruments, and seismometers."
    )

    # EDUCATION
    pdf.section_title("Education")
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

    # SKILLS
    pdf.section_title("Technical Skills")
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
    pdf.section_title("Pengalaman Profesional")
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
        org="Institut Teknologi Sumatera, Indonesia",
        description="Mengelola instrumen geofisika dan membimbing praktikum lapangan mahasiswa. Melaksanakan pelatihan teknis meliputi refraksi seismik, gravity meter Scintrex 6, alat geomagnetik, instrumen geolistrik, dan seismometer."
    )

    # EDUCATION
    pdf.section_title("Pendidikan")
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
    pdf.section_title("Keahlian Teknis")
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
