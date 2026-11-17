import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import os

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def generate_user_aligned_docx():
    doc = Document()
    
    # Page setup - Margins 1 inch (2.54 cm)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
    style_normal = doc.styles['Normal']
    font = style_normal.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0x11, 0x11, 0x11)
    
    # ------------------ COVER PAGE ------------------
    cover_p1 = doc.add_paragraph()
    cover_p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover_p1.paragraph_format.space_before = Pt(30)
    cover_p1.paragraph_format.space_after = Pt(10)
    r = cover_p1.add_run("LAPORAN DATA PROCESSING DAN DATA ANALYSIS\nDATASET CRAIGSLIST CARS & TRUCKS")
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
    
    cover_p2 = doc.add_paragraph()
    cover_p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover_p2.paragraph_format.space_before = Pt(10)
    cover_p2.paragraph_format.space_after = Pt(30)
    r = cover_p2.add_run("TUGAS BESAR 1 / UJIAN TENGAH SEMESTER (UTS)\nMATA KULIAH: DATA SAINS")
    r.font.size = Pt(13)
    r.font.bold = True
    r.font.color.rgb = RGBColor(0x2B, 0x6C, 0xB0)
    
    cover_p_line = doc.add_paragraph()
    cover_p_line.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover_p_line.paragraph_format.space_after = Pt(60)
    r = cover_p_line.add_run("—" * 35)
    r.font.color.rgb = RGBColor(0x71, 0x80, 0x96)
    
    cover_meta = doc.add_paragraph()
    cover_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover_meta.paragraph_format.space_after = Pt(60)
    r = cover_meta.add_run("Disusun Oleh:\n")
    r.font.bold = True
    r.font.size = Pt(12)
    
    r_name = cover_meta.add_run(
        "Nama Mahasiswa : Alief Reefandi / Praktikan Data Sains\n"
        "NIM : [Silakan Diisi NIM]\n"
        "Program Studi : Data Sains / Ilmu Komputer\n"
        "Repository GitHub : https://github.com/AliefReefandi/Data_sains\n"
        "Dataset : Kaggle Craigslist Cars & Trucks Data (Austin Reese)\n"
    )
    r_name.font.size = Pt(11)
    
    cover_date = doc.add_paragraph()
    cover_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cover_date.paragraph_format.space_before = Pt(40)
    r = cover_date.add_run("Format Pengumpulan: Hard Copy\nTenggat Waktu: 19 November 2026\nTAHUN AKADEMIK 2026/2027")
    r.font.bold = True
    r.font.size = Pt(11)
    r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
    
    doc.add_page_break()
    
    # ------------------ HELPER FUNCTIONS ------------------
    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.size = Pt(14)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x1A, 0x36, 0x5D)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.size = Pt(12.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x2B, 0x6C, 0xB0)
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        r.font.size = Pt(12)
        r.font.bold = True
        r.font.color.rgb = RGBColor(0x2D, 0x37, 0x48)
        return p

    def add_p(text, bold_prefix=None, space_after=6):
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.bold = True
        p.add_run(text)
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.bold = True
        p.add_run(text)
        return p

    def add_img(img_path, caption, width=Inches(5.8)):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(10)
            p_img.paragraph_format.space_after = Pt(4)
            p_img.paragraph_format.keep_with_next = True
            run = p_img.add_run()
            run.add_picture(img_path, width=width)
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(12)
            r_cap = p_cap.add_run(caption)
            r_cap.font.size = Pt(10)
            r_cap.font.bold = True
            r_cap.font.color.rgb = RGBColor(0x4A, 0x55, 0x68)

    # ------------------ BAB I. PENDAHULUAN ------------------
    add_h1("BAB I. PENDAHULUAN")
    
    add_h2("1.1 Latar Belakang")
    add_p("Kendaraan bekas memiliki harga yang berbeda-beda. Perbedaan harga tersebut dapat dipengaruhi oleh beberapa hal, seperti merek kendaraan, tahun produksi, jarak tempuh, jenis bahan bakar, dan jenis transmisi.")
    add_p("Pada tugas ini, digunakan dataset Craigslist Cars & Trucks yang berisi informasi mengenai berbagai kendaraan yang dijual melalui platform Craigslist.")
    add_p("Sebelum data dianalisis, perlu dilakukan pemeriksaan dan pembersihan data terlebih dahulu. Hal ini karena dataset masih memiliki beberapa masalah, seperti data kosong, nilai yang tidak wajar, dan format data yang belum sesuai.")
    add_p("Setelah proses pembersihan selesai, dilakukan analisis untuk mengetahui pola harga kendaraan dan hubungan harga dengan beberapa karakteristik kendaraan.")

    add_h2("1.2 Tujuan")
    add_p("Tujuan dari pengerjaan ini adalah:")
    add_bullet("Memahami isi dan struktur dataset kendaraan.")
    add_bullet("Menemukan masalah pada data, seperti data kosong, data tidak wajar, dan data duplikat.")
    add_bullet("Membersihkan data agar lebih siap digunakan untuk analisis.")
    add_bullet("Mengetahui bagaimana penyebaran harga kendaraan.")
    add_bullet("Mengetahui hubungan antara tahun produksi, jarak tempuh, dan harga kendaraan.")
    add_bullet("Membandingkan harga kendaraan berdasarkan merek, jenis bahan bakar, dan jenis transmisi.")

    add_h2("1.3 Dataset yang Digunakan")
    add_p("Dataset yang digunakan adalah Craigslist Cars & Trucks yang diperoleh dari Kaggle dalam format CSV dengan nama file vehicles.csv.")
    add_p("Pada awalnya, dataset memiliki:")
    add_bullet("295.451", "Jumlah baris: ")
    add_bullet("41", "Jumlah kolom: ")
    add_bullet("sekitar 92,4 MB", "Ukuran memori: ")
    add_p("Beberapa informasi yang terdapat dalam dataset antara lain:")
    
    t1 = doc.add_table(rows=1, cols=2)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    h1 = t1.rows[0].cells
    h1[0].text = "Kolom"
    h1[1].text = "Keterangan"
    for cell in h1:
        set_cell_background(cell, "1A365D")
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)
        set_cell_margins(cell, 60, 60, 100, 100)
        
    t1_data = [
        ("price", "Harga kendaraan"),
        ("year", "Tahun produksi kendaraan"),
        ("manufacturer", "Merek kendaraan"),
        ("model", "Model kendaraan"),
        ("odometer", "Jarak tempuh kendaraan"),
        ("fuel", "Jenis bahan bakar"),
        ("transmission", "Jenis transmisi"),
        ("condition", "Kondisi kendaraan"),
        ("type", "Jenis kendaraan"),
        ("title_status", "Status dokumen kendaraan"),
    ]
    for r_idx, (col_name, col_desc) in enumerate(t1_data):
        row_c = t1.add_row().cells
        bg_col = "F7FAFC" if r_idx % 2 == 1 else "FFFFFF"
        row_c[0].text = col_name
        row_c[1].text = col_desc
        for c_idx, cell in enumerate(row_c):
            set_cell_background(cell, bg_col)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.size = Pt(9.5)
            set_cell_margins(cell, 40, 40, 80, 80)
            
    add_p("Tabel 1.1: Beberapa Kolom Utama Dataset Craigslist Cars & Trucks", bold_prefix="Catatan: ", space_after=12)

    doc.add_page_break()

    # ------------------ BAB II. DATA PROCESSING ------------------
    add_h1("BAB II. DATA PROCESSING")
    
    add_h2("2.1 Pemeriksaan Awal Dataset")
    add_p("Tahap pertama adalah memeriksa isi dan struktur dataset menggunakan fungsi info(), shape, dan describe().")
    add_p("Dari hasil pemeriksaan, diketahui bahwa dataset memiliki 295.451 baris dan 41 kolom. Data terdiri dari beberapa jenis, seperti angka, teks, dan tanggal.")
    add_p("Pada tahap ini juga ditemukan beberapa kolom yang memiliki banyak data kosong. Bahkan, terdapat kolom yang seluruh isinya kosong.")
    add_p("Karena itu, perlu dilakukan pemeriksaan lebih lanjut sebelum data digunakan untuk analisis.")

    add_h2("2.2 Pemeriksaan Data Kosong (Missing Value)")
    add_p("Pemeriksaan dilakukan untuk mengetahui jumlah data kosong pada setiap kolom.")
    add_p("Beberapa kolom yang memiliki data kosong dalam jumlah besar adalah:")
    
    t2 = doc.add_table(rows=1, cols=3)
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    h2 = t2.rows[0].cells
    h2[0].text = "Kolom"
    h2[1].text = "Jumlah Data Kosong"
    h2[2].text = "Persentase"
    for cell in h2:
        set_cell_background(cell, "1A365D")
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)
        set_cell_margins(cell, 60, 60, 100, 100)
        
    t2_data = [
        ("other_attributes", "291.688", "98,73%"),
        ("monthly_payment", "289.398", "97,95%"),
        ("updated_date", "179.711", "60,83%"),
        ("address_street", "138.758", "46,96%"),
        ("condition", "135.490", "45,86%"),
        ("VIN", "121.119", "40,99%"),
        ("cylinders", "80.167", "27,13%"),
        ("paint_color", "74.718", "25,29%"),
        ("drive", "70.375", "23,82%"),
    ]
    for r_idx, (col_name, col_missing, col_pct) in enumerate(t2_data):
        row_c = t2.add_row().cells
        bg_col = "F7FAFC" if r_idx % 2 == 1 else "FFFFFF"
        row_c[0].text = col_name
        row_c[1].text = col_missing
        row_c[2].text = col_pct
        for c_idx, cell in enumerate(row_c):
            set_cell_background(cell, bg_col)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                if c_idx in [1, 2]:
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                for r in p.runs:
                    r.font.size = Pt(9.5)
            set_cell_margins(cell, 40, 40, 80, 80)
            
    add_p("Tabel 2.1: Kolom dengan Jumlah Data Kosong Terbanyak", bold_prefix="Catatan: ", space_after=12)
    add_p("Hasil tersebut menunjukkan bahwa beberapa informasi kendaraan tidak diisi oleh penjual. Oleh karena itu, setiap kolom perlu ditangani sesuai dengan kondisi dan kegunaannya.")

    add_h2("2.3 Pemeriksaan Data Duplikat")
    add_p("Selanjutnya dilakukan pemeriksaan untuk mengetahui apakah terdapat data yang tercatat lebih dari satu kali.")
    add_p("Pemeriksaan dilakukan terhadap seluruh baris dan kolom id.")
    add_p("Hasilnya:")
    add_bullet("0.", "Data duplikat seluruh baris: ")
    add_bullet("0.", "Data dengan ID duplikat: ")
    add_p("Dengan demikian, tidak ditemukan data duplikat pada dataset.")

    add_h2("2.4 Penghapusan Kolom")
    add_p("Beberapa kolom dihapus karena memiliki terlalu banyak data kosong atau tidak terlalu dibutuhkan dalam analisis.")
    add_p("Kolom yang dihapus adalah:")
    add_bullet("size")
    add_bullet("county")
    add_bullet("other_attributes")
    add_bullet("monthly_payment")
    add_bullet("updated_date")
    add_bullet("address_street")
    add_p("Penghapusan dilakukan agar dataset lebih sederhana dan hanya menyimpan kolom yang masih berguna untuk kebutuhan analisis.")

    add_h2("2.5 Perubahan Format Data")
    add_p("Beberapa kolom memiliki format yang perlu disesuaikan agar dapat digunakan dengan benar.")
    add_p("Perubahan yang dilakukan adalah:")
    add_bullet("Kolom price diubah menjadi format angka.")
    add_bullet("Kolom posting_date diubah menjadi format tanggal.")
    add_bullet("Kolom updated_date sempat diubah menjadi format tanggal sebelum akhirnya dihapus karena memiliki banyak data kosong.")
    add_p("Dengan perubahan ini, data menjadi lebih mudah diolah dan dianalisis.")

    add_h2("2.6 Pembersihan Data Tidak Wajar")
    add_p("Pada tahap ini dilakukan pemeriksaan terhadap tiga kolom utama, yaitu harga kendaraan, tahun produksi, dan jarak tempuh.")
    
    add_h3("A. Harga Kendaraan (price)")
    add_p("Ditemukan beberapa nilai harga yang tidak wajar, yaitu:")
    add_bullet("Harga $0 sebanyak 10.288 data.")
    add_bullet("Harga di atas $1.000.000 sebanyak 71 data.")
    add_bullet("Tidak ditemukan harga negatif.")
    add_p("Harga nol dan harga di atas $1.000.000 dianggap tidak sesuai untuk analisis harga kendaraan. Oleh karena itu, kedua jenis nilai tersebut diubah menjadi data kosong (NaN).")
    add_p("Total data harga yang diubah menjadi kosong adalah 10.359 data.")

    add_h3("B. Tahun Kendaraan (year)")
    add_p("Ditemukan 14 kendaraan dengan tahun produksi 1900.")
    add_p("Setelah diperiksa, beberapa data tersebut memiliki informasi yang tidak sesuai dengan tahun produksinya. Oleh karena itu, nilai tahun 1900 diubah menjadi data kosong.")
    add_p("Selain itu, ditemukan enam kendaraan dengan tahun produksi 1901. Satu di antaranya memiliki informasi Oldsmobile Curved Dash yang mendukung tahun tersebut. Lima data lainnya tidak memiliki informasi yang cukup untuk memastikan kebenarannya.")

    add_h3("C. Jarak Tempuh (odometer)")
    add_p("Ditemukan 287 kendaraan dengan jarak tempuh lebih dari 1.000.000 miles.")
    add_p("Nilai tersebut dianggap tidak wajar untuk kebutuhan analisis ini sehingga diubah menjadi data kosong (NaN).")
    add_p("Pada tahap ini, baris data tidak dihapus. Hanya nilai yang dianggap tidak wajar yang diubah menjadi kosong agar informasi kendaraan lainnya tetap dapat digunakan.")

    add_h2("2.7 Penanganan Data Kosong pada Kategori")
    add_p("Data kosong pada beberapa kolom kategori diisi dengan kata Unknown.")
    add_p("Kolom yang ditangani adalah:")
    add_bullet("condition")
    add_bullet("cylinders")
    add_bullet("paint_color")
    add_bullet("drive")
    add_bullet("type")
    add_bullet("manufacturer")
    add_bullet("transmission")
    add_bullet("fuel")
    add_bullet("title_status")
    add_p("Pengisian ini dilakukan agar data kendaraan tetap dapat digunakan meskipun informasi pada kolom tersebut tidak tersedia.")

    add_h2("2.8 Hasil Akhir Data Processing")
    add_p("Setelah seluruh proses pembersihan selesai, dilakukan pemeriksaan kembali untuk memastikan hasilnya.")
    add_p("Berikut hasil akhir dataset:")
    
    t3 = doc.add_table(rows=1, cols=2)
    t3.alignment = WD_TABLE_ALIGNMENT.CENTER
    h3 = t3.rows[0].cells
    h3[0].text = "Keterangan"
    h3[1].text = "Hasil"
    for cell in h3:
        set_cell_background(cell, "1A365D")
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)
        set_cell_margins(cell, 60, 60, 100, 100)
        
    t3_data = [
        ("Jumlah baris", "295.451"),
        ("Jumlah kolom", "35"),
        ("Data duplikat", "0"),
        ("ID duplikat", "0"),
        ("Data kosong pada price", "10.359"),
        ("Data kosong pada odometer", "4.323"),
        ("Data kosong pada year", "40"),
    ]
    for r_idx, (keterangan, hasil) in enumerate(t3_data):
        row_c = t3.add_row().cells
        bg_col = "F7FAFC" if r_idx % 2 == 1 else "FFFFFF"
        row_c[0].text = keterangan
        row_c[1].text = hasil
        for c_idx, cell in enumerate(row_c):
            set_cell_background(cell, bg_col)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                if c_idx == 1:
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                for r in p.runs:
                    r.font.size = Pt(9.5)
            set_cell_margins(cell, 40, 40, 80, 80)
            
    add_p("Tabel 2.2: Ringkasan Hasil Akhir Dataset Setelah Data Processing", bold_prefix="Catatan: ", space_after=12)
    add_p("Dataset yang sudah dibersihkan kemudian disimpan dengan nama vehicles_cleaned.csv.")
    add_p("Dengan demikian, dataset sudah siap digunakan untuk tahap Data Analysis.")

    doc.add_page_break()

    # ------------------ BAB III. DATA ANALYSIS ------------------
    add_h1("BAB III. DATA ANALYSIS")
    
    add_h2("3.1 Q1 – Analisis Penyebaran Harga Kendaraan")
    add_p("Analisis pertama dilakukan untuk mengetahui bagaimana penyebaran harga kendaraan dalam dataset.")
    add_p("Analisis ini menggunakan nilai rata-rata, median, kuartil, persentil, histogram, dan boxplot.")
    add_p("Untuk membuat grafik lebih mudah dibaca, digunakan data harga yang tidak melebihi persentil ke-99, yaitu $89.900. Pembatasan ini hanya digunakan untuk visualisasi, bukan untuk menghapus data dari dataset final.")
    
    add_p("Hasil Statistik Harga:")
    t4 = doc.add_table(rows=1, cols=2)
    t4.alignment = WD_TABLE_ALIGNMENT.CENTER
    h4 = t4.rows[0].cells
    h4[0].text = "Statistik"
    h4[1].text = "Nilai"
    for cell in h4:
        set_cell_background(cell, "1A365D")
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)
        set_cell_margins(cell, 60, 60, 100, 100)
        
    t4_data = [
        ("Jumlah data harga valid", "285.092"),
        ("Rata-rata", "$18.313,38"),
        ("Median", "$12.995"),
        ("Harga terendah", "$1"),
        ("Q1 (25%)", "$6.950"),
        ("Q3 (75%)", "$22.995"),
        ("Harga tertinggi", "$1.000.000"),
    ]
    for r_idx, (stat, val) in enumerate(t4_data):
        row_c = t4.add_row().cells
        bg_col = "F7FAFC" if r_idx % 2 == 1 else "FFFFFF"
        row_c[0].text = stat
        row_c[1].text = val
        for c_idx, cell in enumerate(row_c):
            set_cell_background(cell, bg_col)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                if c_idx == 1:
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                for r in p.runs:
                    r.font.size = Pt(9.5)
            set_cell_margins(cell, 40, 40, 80, 80)
            
    add_p("Tabel 3.1: Hasil Statistik Deskriptif Harga Kendaraan", bold_prefix="Catatan: ", space_after=10)

    add_p("Hasil persentil harga:")
    t5 = doc.add_table(rows=1, cols=2)
    t5.alignment = WD_TABLE_ALIGNMENT.CENTER
    h5 = t5.rows[0].cells
    h5[0].text = "Persentil"
    h5[1].text = "Harga"
    for cell in h5:
        set_cell_background(cell, "1A365D")
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)
        set_cell_margins(cell, 60, 60, 100, 100)
        
    t5_data = [
        ("25%", "$6.950"),
        ("50%", "$12.995"),
        ("75%", "$22.995"),
        ("90%", "$37.985"),
        ("95%", "$49.997"),
        ("99%", "$89.900"),
        ("99,5%", "$110.000"),
        ("99,9%", "$219.995"),
    ]
    for r_idx, (pct, prc) in enumerate(t5_data):
        row_c = t5.add_row().cells
        bg_col = "F7FAFC" if r_idx % 2 == 1 else "FFFFFF"
        row_c[0].text = pct
        row_c[1].text = prc
        for c_idx, cell in enumerate(row_c):
            set_cell_background(cell, bg_col)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                if c_idx == 1:
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                for r in p.runs:
                    r.font.size = Pt(9.5)
            set_cell_margins(cell, 40, 40, 80, 80)
            
    add_p("Tabel 3.2: Persentil Harga Kendaraan", bold_prefix="Catatan: ", space_after=10)

    add_h3("Hasil Analisis")
    add_p("Berdasarkan hasil tersebut, diketahui bahwa rata-rata harga kendaraan adalah $18.313,38, sedangkan nilai tengahnya adalah $12.995.")
    add_p("Nilai rata-rata yang lebih tinggi daripada median menunjukkan bahwa terdapat beberapa kendaraan dengan harga tinggi yang membuat rata-rata harga meningkat.")
    add_p("Sebanyak 50% kendaraan memiliki harga antara $6.950 hingga $22.995.")

    add_img("images/cell_100_out_1.png", "Gambar 3.1 Distribusi Harga Kendaraan", width=Inches(5.8))

    add_p("Dari histogram, terlihat bahwa sebagian besar kendaraan memiliki harga di bawah $20.000. Semakin tinggi harga kendaraan, jumlah listing yang ditemukan semakin sedikit.")
    add_p("Dengan demikian, penyebaran harga kendaraan lebih banyak terkumpul pada harga yang relatif rendah, sedangkan kendaraan dengan harga tinggi jumlahnya lebih sedikit.")

    add_h3("Kesimpulan Q1")
    add_p("Sebagian besar kendaraan dalam dataset memiliki harga pada rentang menengah ke bawah. Hanya sebagian kecil kendaraan yang memiliki harga jauh lebih tinggi dibandingkan kendaraan lainnya.")

    doc.add_page_break()

    # ------------------ 3.2 Q2 ------------------
    add_h2("3.2 Q2 – Analisis Hubungan Tahun Produksi, Jarak Tempuh, dan Harga")
    add_p("Analisis kedua bertujuan untuk mengetahui hubungan antara tahun produksi kendaraan, jarak tempuh, dan harga kendaraan.")
    add_p("Data yang digunakan berjumlah 275.254 baris. Data dipilih dengan ketentuan:")
    add_bullet("Harga kendaraan lebih dari nol.")
    add_bullet("Harga tidak melebihi $89.900.")
    add_bullet("Jarak tempuh lebih dari nol dan tidak melebihi persentil ke-99.")
    add_bullet("Tahun kendaraan tidak lebih dari 2026.")
    add_bullet("Data kosong pada ketiga kolom tidak digunakan dalam perhitungan.")

    add_p("Statistik Data Q2:")
    t6 = doc.add_table(rows=1, cols=4)
    t6.alignment = WD_TABLE_ALIGNMENT.CENTER
    h6 = t6.rows[0].cells
    h6[0].text = "Statistik"
    h6[1].text = "Year"
    h6[2].text = "Odometer"
    h6[3].text = "Price"
    for cell in h6:
        set_cell_background(cell, "1A365D")
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)
        set_cell_margins(cell, 60, 60, 100, 100)
        
    t6_data = [
        ("Jumlah data", "275.254", "275.254", "275.254"),
        ("Rata-rata", "2012,68", "110.070,74", "$16.991,01"),
        ("Median", "2015", "108.534,50", "$12.950"),
        ("Minimum", "1901", "1", "$1"),
        ("Maksimum", "2026", "290.000", "$89.900"),
    ]
    for r_idx, (st, yr, od, pr) in enumerate(t6_data):
        row_c = t6.add_row().cells
        bg_col = "F7FAFC" if r_idx % 2 == 1 else "FFFFFF"
        row_c[0].text = st
        row_c[1].text = yr
        row_c[2].text = od
        row_c[3].text = pr
        for c_idx, cell in enumerate(row_c):
            set_cell_background(cell, bg_col)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                if c_idx > 0:
                    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                for r in p.runs:
                    r.font.size = Pt(9.5)
            set_cell_margins(cell, 40, 40, 80, 80)
            
    add_p("Tabel 3.3: Statistik Data Q2 (Year, Odometer, Price)", bold_prefix="Catatan: ", space_after=10)

    add_h3("A. Korelasi Pearson")
    add_p("Korelasi Pearson digunakan untuk mengetahui arah dan kekuatan hubungan antara dua variabel secara linear.")
    add_p("Hasil perhitungannya:")
    
    t7 = doc.add_table(rows=1, cols=2)
    t7.alignment = WD_TABLE_ALIGNMENT.CENTER
    h7 = t7.rows[0].cells
    h7[0].text = "Hubungan"
    h7[1].text = "Nilai Pearson"
    for cell in h7:
        set_cell_background(cell, "1A365D")
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)
        set_cell_margins(cell, 60, 60, 100, 100)
        
    t7_data = [
        ("Year – Odometer", "-0,138"),
        ("Year – Price", "+0,209"),
        ("Odometer – Price", "-0,496"),
    ]
    for r_idx, (rel, val) in enumerate(t7_data):
        row_c = t7.add_row().cells
        bg_col = "F7FAFC" if r_idx % 2 == 1 else "FFFFFF"
        row_c[0].text = rel
        row_c[1].text = val
        for c_idx, cell in enumerate(row_c):
            set_cell_background(cell, bg_col)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                if c_idx == 1:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.size = Pt(9.5)
            set_cell_margins(cell, 40, 40, 80, 80)
            
    add_p("Tabel 3.4: Hasil Korelasi Pearson", bold_prefix="Catatan: ", space_after=8)
    add_p("Penjelasan:")
    add_bullet("Memiliki hubungan negatif yang sangat lemah. Kendaraan yang lebih baru cenderung memiliki jarak tempuh lebih rendah.", "Year dan Odometer: ")
    add_bullet("Memiliki hubungan positif yang lemah. Kendaraan yang lebih baru cenderung memiliki harga lebih tinggi.", "Year dan Price: ")
    add_bullet("Memiliki hubungan negatif sedang. Kendaraan dengan jarak tempuh lebih tinggi cenderung memiliki harga lebih rendah.", "Odometer dan Price: ")

    add_h3("B. Korelasi Spearman")
    add_p("Korelasi Spearman digunakan untuk melihat hubungan antara dua variabel berdasarkan urutan atau peringkat nilainya.")
    add_p("Hasil perhitungannya:")
    
    t8 = doc.add_table(rows=1, cols=2)
    t8.alignment = WD_TABLE_ALIGNMENT.CENTER
    h8 = t8.rows[0].cells
    h8[0].text = "Hubungan"
    h8[1].text = "Nilai Spearman"
    for cell in h8:
        set_cell_background(cell, "1A365D")
        for p in cell.paragraphs:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
                r.font.size = Pt(10)
        set_cell_margins(cell, 60, 60, 100, 100)
        
    t8_data = [
        ("Year – Odometer", "-0,424"),
        ("Year – Price", "+0,523"),
        ("Odometer – Price", "-0,538"),
    ]
    for r_idx, (rel, val) in enumerate(t8_data):
        row_c = t8.add_row().cells
        bg_col = "F7FAFC" if r_idx % 2 == 1 else "FFFFFF"
        row_c[0].text = rel
        row_c[1].text = val
        for c_idx, cell in enumerate(row_c):
            set_cell_background(cell, bg_col)
            for p in cell.paragraphs:
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                if c_idx == 1:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.size = Pt(9.5)
            set_cell_margins(cell, 40, 40, 80, 80)
            
    add_p("Tabel 3.5: Hasil Korelasi Spearman", bold_prefix="Catatan: ", space_after=8)
    add_p("Penjelasan:")
    add_bullet("Kendaraan yang lebih baru cenderung memiliki jarak tempuh lebih rendah.", "Year dan Odometer: ")
    add_bullet("Kendaraan yang lebih baru cenderung memiliki harga lebih tinggi.", "Year dan Price: ")
    add_bullet("Kendaraan dengan jarak tempuh lebih tinggi cenderung memiliki harga lebih rendah.", "Odometer dan Price: ")

    add_h3("C. Analisis Scatter Plot")
    add_img("images/cell_105_out_0.png", "Gambar 3.2 Hubungan Tahun Kendaraan dan Odometer terhadap Harga", width=Inches(6.0))
    add_p("Berdasarkan grafik hubungan tahun kendaraan dengan harga, terlihat bahwa kendaraan yang lebih baru cenderung memiliki harga lebih tinggi. Namun, harga kendaraan pada tahun yang sama masih memiliki perbedaan yang cukup besar.")
    add_p("Pada grafik hubungan jarak tempuh dengan harga, terlihat bahwa kendaraan dengan jarak tempuh rendah memiliki harga yang lebih bervariasi. Sementara itu, kendaraan dengan jarak tempuh tinggi lebih banyak ditemukan pada rentang harga yang lebih rendah.")

    add_h3("Kesimpulan Q2")
    add_p("Hasil analisis menunjukkan bahwa tahun produksi dan jarak tempuh memiliki hubungan dengan harga kendaraan.")
    add_p("Kendaraan yang lebih baru cenderung memiliki harga lebih tinggi, sedangkan kendaraan dengan jarak tempuh lebih tinggi cenderung memiliki harga lebih rendah.")
    add_p("Namun, hubungan tersebut tidak berarti bahwa tahun produksi dan jarak tempuh merupakan satu-satunya hal yang menentukan harga kendaraan. Masih terdapat faktor lain yang dapat memengaruhi harga.")

    doc.add_page_break()

    # ------------------ 3.3 Q3 ------------------
    add_h2("3.3 Q3 – Analisis Harga Berdasarkan Merek, Bahan Bakar, dan Transmisi")
    add_p("Analisis ketiga dilakukan untuk membandingkan harga kendaraan berdasarkan tiga kategori, yaitu merek kendaraan (manufacturer), jenis bahan bakar (fuel), dan jenis transmisi (transmission).")
    add_p("Jumlah data yang digunakan adalah 282.257 baris. Data harga yang digunakan lebih dari nol dan tidak melebihi persentil ke-99, yaitu $89.900.")
    add_p("Perbandingan dilakukan menggunakan boxplot untuk melihat nilai tengah harga dan perbedaan penyebaran harga pada setiap kategori.")

    add_h3("A. Harga Berdasarkan Manufacturer")
    add_p("Analisis manufacturer menampilkan sepuluh kategori manufacturer dengan jumlah listing terbanyak, termasuk kategori Unknown untuk kendaraan yang tidak memiliki informasi merek. Berdasarkan boxplot, ditemukan bahwa:")
    add_bullet("RAM memiliki nilai tengah harga paling tinggi di antara sepuluh merek yang ditampilkan.")
    add_bullet("GMC juga memiliki nilai tengah harga yang cukup tinggi.")
    add_bullet("Nissan memiliki nilai tengah harga paling rendah.")
    add_bullet("Ford, Toyota, Chevrolet, dan Jeep memiliki penyebaran harga yang cukup luas.")
    add_bullet("Terdapat beberapa kendaraan dengan harga jauh lebih tinggi dibandingkan sebagian besar kendaraan dalam kategori yang sama.")
    add_p("Hasil ini menunjukkan bahwa setiap merek kendaraan memiliki penyebaran harga yang berbeda.")

    add_h3("B. Harga Berdasarkan Fuel")
    add_p("Berdasarkan boxplot jenis bahan bakar, ditemukan bahwa:")
    add_bullet("Diesel memiliki nilai tengah harga paling tinggi.")
    add_bullet("Electric berada di urutan kedua.")
    add_bullet("Other dan Hybrid memiliki nilai tengah harga pada kelompok menengah.")
    add_bullet("Gas memiliki nilai tengah harga paling rendah.")
    add_p("Hal ini menunjukkan bahwa harga kendaraan dalam dataset memiliki perbedaan berdasarkan jenis bahan bakarnya.")

    add_h3("C. Harga Berdasarkan Transmission")
    add_p("Berdasarkan boxplot jenis transmisi, ditemukan bahwa:")
    add_bullet("Other memiliki nilai tengah harga paling tinggi.")
    add_bullet("Unknown memiliki nilai tengah harga yang relatif tinggi.")
    add_bullet("Automatic dan Manual memiliki nilai tengah harga yang cukup berdekatan.")
    add_p("Setiap kategori memiliki penyebaran harga yang berbeda.")
    add_p("Kategori Other dan Unknown perlu diperhatikan karena keduanya tidak menunjukkan jenis transmisi yang spesifik.")

    add_img("images/cell_111_out_0.png", "Gambar 3.3 Distribusi Harga Kendaraan Berdasarkan Manufacturer, Fuel, dan Transmission", width=Inches(5.8))

    add_h3("Kesimpulan Q3")
    add_p("Hasil analisis menunjukkan bahwa harga kendaraan memiliki perbedaan berdasarkan merek, jenis bahan bakar, dan jenis transmisi.")
    add_p("RAM memiliki nilai tengah harga tertinggi di antara sepuluh merek yang dianalisis. Berdasarkan jenis bahan bakar, diesel memiliki nilai tengah harga tertinggi. Sementara itu, berdasarkan transmisi, kategori Other memiliki nilai tengah harga tertinggi.")
    add_p("Perbedaan ini menunjukkan bahwa karakteristik kendaraan berkaitan dengan variasi harga yang ditemukan dalam dataset. Namun, hasil ini tidak membuktikan bahwa karakteristik tersebut secara langsung menyebabkan harga menjadi lebih tinggi atau lebih rendah.")

    doc.add_page_break()

    # ------------------ BAB IV. KESIMPULAN ------------------
    add_h1("BAB IV. KESIMPULAN")
    
    add_h2("4.1 Kesimpulan Umum")
    add_p("Berdasarkan seluruh proses yang telah dilakukan, dapat disimpulkan bahwa:")
    add_bullet("Dataset awal memiliki 295.451 baris dan 41 kolom. Setelah dibersihkan, dataset memiliki 295.451 baris dan 35 kolom.")
    add_bullet("Proses Data Processing berhasil menangani data kosong, nilai yang tidak wajar, dan beberapa kolom yang tidak diperlukan.")
    add_bullet("Hasil analisis Q1 menunjukkan bahwa sebagian besar kendaraan memiliki harga yang relatif rendah, sedangkan kendaraan dengan harga tinggi jumlahnya lebih sedikit.")
    add_bullet("Hasil analisis Q2 menunjukkan bahwa kendaraan dengan tahun produksi lebih baru cenderung memiliki harga lebih tinggi. Sebaliknya, kendaraan dengan jarak tempuh lebih tinggi cenderung memiliki harga lebih rendah.")
    add_bullet("Hasil analisis Q3 menunjukkan bahwa harga kendaraan memiliki perbedaan berdasarkan merek, jenis bahan bakar, dan jenis transmisi.")
    add_p("Secara keseluruhan, Data Processing membuat data lebih siap digunakan, sedangkan Data Analysis membantu memberikan gambaran mengenai harga dan karakteristik kendaraan.")

    add_h2("4.2 Keterbatasan Analisis")
    add_p("Dalam pengerjaan ini terdapat beberapa keterbatasan, yaitu:")
    add_bullet("Harga yang tercatat merupakan harga pada listing kendaraan dan belum tentu merupakan harga akhir saat transaksi.")
    add_bullet("Beberapa informasi kendaraan masih kosong, seperti VIN dan informasi lokasi.")
    add_bullet("Batas nilai yang digunakan untuk menangani anomali merupakan aturan yang ditentukan dalam proses analisis.")
    add_bullet("Analisis Q2 dan Q3 menggunakan sebagian data yang telah disaring sesuai kebutuhan masing-masing analisis.")
    add_bullet("Hasil korelasi hanya menunjukkan hubungan antarvariabel dan tidak membuktikan bahwa satu variabel menyebabkan perubahan pada variabel lainnya.")

    add_h1("PENUTUP")
    add_p("Melalui tugas ini, dilakukan pemeriksaan, pembersihan, dan analisis terhadap dataset Craigslist Cars & Trucks. Proses tersebut membantu memahami kondisi data sekaligus menemukan beberapa pola harga kendaraan berdasarkan informasi yang tersedia.")

    add_h1("DAFTAR PUSTAKA")
    add_p("Austin Reese. (n.d.). Used cars dataset. Kaggle. https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data")

    out_file = "Laporan_Tubes1_Data_Sains.docx"
    doc.save(out_file)
    print(f"File '{out_file}' successfully regenerated with exact user content!")

if __name__ == '__main__':
    generate_user_aligned_docx()
