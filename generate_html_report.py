import base64
import os

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded}"
    return ""

img_3_1 = get_base64_image("images/cell_100_out_1.png")
img_3_2 = get_base64_image("images/cell_105_out_0.png")
img_3_3 = get_base64_image("images/cell_111_out_0.png")

html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>LAPORAN DATA PROCESSING DAN DATA ANALYSIS - Dataset Craigslist Cars & Trucks</title>
<style>
  @page {{
    size: A4 portrait;
    margin: 20mm 20mm 20mm 20mm;
    @bottom-right {{
      content: counter(page);
    }}
  }}
  @media print {{
    body {{
      font-size: 11pt;
      color: #111111;
      background: #ffffff;
      line-height: 1.5;
    }}
    .page-break {{
      page-break-after: always;
      break-after: page;
    }}
    .no-print {{
      display: none !important;
    }}
    .print-btn-bar {{
      display: none !important;
    }}
  }}
  * {{
    box-sizing: border-box;
  }}
  body {{
    font-family: 'Times New Roman', Times, serif;
    line-height: 1.6;
    color: #222222;
    background-color: #f7fafc;
    margin: 0;
    padding: 0;
  }}
  .container {{
    max-width: 850px;
    margin: 0 auto;
    background: #ffffff;
    padding: 40px 60px;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
  }}
  .print-btn-bar {{
    position: sticky;
    top: 0;
    background: #1a365d;
    color: white;
    padding: 12px 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 1000;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }}
  .btn-print {{
    background: #3182ce;
    color: white;
    border: none;
    padding: 8px 18px;
    font-size: 14px;
    font-weight: 600;
    border-radius: 6px;
    cursor: pointer;
    transition: background 0.2s;
  }}
  .btn-print:hover {{
    background: #2b6cb0;
  }}
  .cover {{
    text-align: center;
    padding: 50px 0 30px 0;
  }}
  .cover h1 {{
    font-size: 20pt;
    color: #1a365d;
    margin-bottom: 8px;
    font-weight: bold;
    line-height: 1.3;
  }}
  .cover h2 {{
    font-size: 14pt;
    color: #2b6cb0;
    font-weight: bold;
    margin-top: 15px;
    margin-bottom: 25px;
    line-height: 1.4;
  }}
  .cover-divider {{
    width: 140px;
    height: 3px;
    background: #718096;
    margin: 25px auto;
  }}
  .cover-info {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 20px 28px;
    display: inline-block;
    text-align: left;
    margin-bottom: 35px;
    font-size: 11pt;
  }}
  .cover-info table td {{
    padding: 4px 8px;
  }}
  .cover-deadline {{
    font-size: 11pt;
    font-weight: bold;
    color: #c53030;
    margin-top: 15px;
  }}
  h1.section-title {{
    color: #1a365d;
    font-size: 16pt;
    border-bottom: 1.5px solid #1a365d;
    padding-bottom: 6px;
    margin-top: 36px;
    margin-bottom: 16px;
  }}
  h2.sub-title {{
    color: #2b6cb0;
    font-size: 13pt;
    margin-top: 22px;
    margin-bottom: 10px;
  }}
  h3.sub-sub-title {{
    color: #2d3748;
    font-size: 12pt;
    margin-top: 16px;
    margin-bottom: 8px;
  }}
  p {{
    text-align: justify;
    margin-bottom: 10px;
    font-size: 11.5pt;
  }}
  ul, ol {{
    margin-bottom: 12px;
    padding-left: 24px;
  }}
  li {{
    margin-bottom: 4px;
    text-align: justify;
    font-size: 11.5pt;
  }}
  .figure {{
    text-align: center;
    margin: 20px 0;
    page-break-inside: avoid;
  }}
  .figure img {{
    max-width: 100%;
    height: auto;
    border: 1px solid #cbd5e0;
  }}
  .figure-caption {{
    font-size: 10.5pt;
    color: #4a5568;
    font-weight: bold;
    margin-top: 6px;
  }}
  table.data-table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 10.5pt;
    page-break-inside: avoid;
  }}
  table.data-table th, table.data-table td {{
    border: 1px solid #a0aec0;
    padding: 6px 10px;
  }}
  table.data-table th {{
    background-color: #1a365d;
    color: #ffffff;
    font-weight: bold;
    text-align: center;
  }}
  table.data-table tr:nth-child(even) {{
    background-color: #f7fafc;
  }}
</style>
</head>
<body>

<div class="print-btn-bar no-print">
  <div>
    <strong>Laporan Tubes 1 (UTS) Data Processing & Data Analysis</strong> &mdash; Hard Copy Ready
  </div>
  <button class="btn-print" onclick="window.print()">🖨️ Cetak Hard Copy / Simpan PDF</button>
</div>

<div class="container">

  <!-- COVER PAGE -->
  <div class="cover">
    <h1>LAPORAN DATA PROCESSING DAN DATA ANALYSIS<br>DATASET CRAIGSLIST CARS & TRUCKS</h1>
    <div class="cover-divider"></div>
    <h2>TUGAS BESAR 1 / UJIAN TENGAH SEMESTER (UTS)<br>MATA KULIAH: DATA SAINS</h2>
    
    <div class="cover-info">
      <table>
        <tr>
          <td><strong>Nama Mahasiswa</strong></td>
          <td>:</td>
          <td>Alief Reefandi / Praktikan Data Sains</td>
        </tr>
        <tr>
          <td><strong>NIM</strong></td>
          <td>:</td>
          <td>[Silakan Diisi NIM]</td>
        </tr>
        <tr>
          <td><strong>Program Studi</strong></td>
          <td>:</td>
          <td>Data Sains / Ilmu Komputer</td>
        </tr>
        <tr>
          <td><strong>Repository GitHub</strong></td>
          <td>:</td>
          <td><a href="https://github.com/AliefReefandi/Data_sains" target="_blank">github.com/AliefReefandi/Data_sains</a></td>
        </tr>
        <tr>
          <td><strong>Dataset</strong></td>
          <td>:</td>
          <td>Kaggle: Craigslist Cars & Trucks Data (Austin Reese)</td>
        </tr>
      </table>
    </div>
    
    <div class="cover-deadline">
      Format Pengumpulan: Hard Copy &mdash; Tenggat Waktu: 19 November 2026<br>
      TAHUN AKADEMIK 2026/2027
    </div>
  </div>

  <div class="page-break"></div>

  <!-- BAB I -->
  <h1 class="section-title">BAB I. PENDAHULUAN</h1>
  
  <h2 class="sub-title">1.1 Latar Belakang</h2>
  <p>Kendaraan bekas memiliki harga yang berbeda-beda. Perbedaan harga tersebut dapat dipengaruhi oleh beberapa hal, seperti merek kendaraan, tahun produksi, jarak tempuh, jenis bahan bakar, dan jenis transmisi.</p>
  <p>Pada tugas ini, digunakan dataset Craigslist Cars & Trucks yang berisi informasi mengenai berbagai kendaraan yang dijual melalui platform Craigslist.</p>
  <p>Sebelum data dianalisis, perlu dilakukan pemeriksaan dan pembersihan data terlebih dahulu. Hal ini karena dataset masih memiliki beberapa masalah, seperti data kosong, nilai yang tidak wajar, dan format data yang belum sesuai.</p>
  <p>Setelah proses pembersihan selesai, dilakukan analisis untuk mengetahui pola harga kendaraan dan hubungan harga dengan beberapa karakteristik kendaraan.</p>

  <h2 class="sub-title">1.2 Tujuan</h2>
  <p>Tujuan dari pengerjaan ini adalah:</p>
  <ul>
    <li>Memahami isi dan struktur dataset kendaraan.</li>
    <li>Menemukan masalah pada data, seperti data kosong, data tidak wajar, dan data duplikat.</li>
    <li>Membersihkan data agar lebih siap digunakan untuk analisis.</li>
    <li>Mengetahui bagaimana penyebaran harga kendaraan.</li>
    <li>Mengetahui hubungan antara tahun produksi, jarak tempuh, dan harga kendaraan.</li>
    <li>Membandingkan harga kendaraan berdasarkan merek, jenis bahan bakar, dan jenis transmisi.</li>
  </ul>

  <h2 class="sub-title">1.3 Dataset yang Digunakan</h2>
  <p>Dataset yang digunakan adalah Craigslist Cars & Trucks yang diperoleh dari Kaggle dalam format CSV dengan nama file vehicles.csv.</p>
  <p>Pada awalnya, dataset memiliki:</p>
  <ul>
    <li>Jumlah baris: 295.451</li>
    <li>Jumlah kolom: 41</li>
    <li>Ukuran memori: sekitar 92,4 MB</li>
  </ul>
  <p>Beberapa informasi yang terdapat dalam dataset antara lain:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th style="width: 35%;">Kolom</th>
        <th>Keterangan</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><code>price</code></td><td>Harga kendaraan</td></tr>
      <tr><td><code>year</code></td><td>Tahun produksi kendaraan</td></tr>
      <tr><td><code>manufacturer</code></td><td>Merek kendaraan</td></tr>
      <tr><td><code>model</code></td><td>Model kendaraan</td></tr>
      <tr><td><code>odometer</code></td><td>Jarak tempuh kendaraan</td></tr>
      <tr><td><code>fuel</code></td><td>Jenis bahan bakar</td></tr>
      <tr><td><code>transmission</code></td><td>Jenis transmisi</td></tr>
      <tr><td><code>condition</code></td><td>Kondisi kendaraan</td></tr>
      <tr><td><code>type</code></td><td>Jenis kendaraan</td></tr>
      <tr><td><code>title_status</code></td><td>Status dokumen kendaraan</td></tr>
    </tbody>
  </table>

  <!-- BAB II -->
  <h1 class="section-title">BAB II. DATA PROCESSING</h1>

  <h2 class="sub-title">2.1 Pemeriksaan Awal Dataset</h2>
  <p>Tahap pertama adalah memeriksa isi dan struktur dataset menggunakan fungsi info(), shape, dan describe().</p>
  <p>Dari hasil pemeriksaan, diketahui bahwa dataset memiliki 295.451 baris dan 41 kolom. Data terdiri dari beberapa jenis, seperti angka, teks, dan tanggal.</p>
  <p>Pada tahap ini juga ditemukan beberapa kolom yang memiliki banyak data kosong. Bahkan, terdapat kolom yang seluruh isinya kosong.</p>
  <p>Karena itu, perlu dilakukan pemeriksaan lebih lanjut sebelum data digunakan untuk analisis.</p>

  <h2 class="sub-title">2.2 Pemeriksaan Data Kosong (Missing Value)</h2>
  <p>Pemeriksaan dilakukan untuk mengetahui jumlah data kosong pada setiap kolom.</p>
  <p>Beberapa kolom yang memiliki data kosong dalam jumlah besar adalah:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th>Kolom</th>
        <th style="text-align: right;">Jumlah Data Kosong</th>
        <th style="text-align: right;">Persentase</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><code>other_attributes</code></td><td style="text-align: right;">291.688</td><td style="text-align: right;">98,73%</td></tr>
      <tr><td><code>monthly_payment</code></td><td style="text-align: right;">289.398</td><td style="text-align: right;">97,95%</td></tr>
      <tr><td><code>updated_date</code></td><td style="text-align: right;">179.711</td><td style="text-align: right;">60,83%</td></tr>
      <tr><td><code>address_street</code></td><td style="text-align: right;">138.758</td><td style="text-align: right;">46,96%</td></tr>
      <tr><td><code>condition</code></td><td style="text-align: right;">135.490</td><td style="text-align: right;">45,86%</td></tr>
      <tr><td><code>VIN</code></td><td style="text-align: right;">121.119</td><td style="text-align: right;">40,99%</td></tr>
      <tr><td><code>cylinders</code></td><td style="text-align: right;">80.167</td><td style="text-align: right;">27,13%</td></tr>
      <tr><td><code>paint_color</code></td><td style="text-align: right;">74.718</td><td style="text-align: right;">25,29%</td></tr>
      <tr><td><code>drive</code></td><td style="text-align: right;">70.375</td><td style="text-align: right;">23,82%</td></tr>
    </tbody>
  </table>

  <p>Hasil tersebut menunjukkan bahwa beberapa informasi kendaraan tidak diisi oleh penjual. Oleh karena itu, setiap kolom perlu ditangani sesuai dengan kondisi dan kegunaannya.</p>

  <h2 class="sub-title">2.3 Pemeriksaan Data Duplikat</h2>
  <p>Selanjutnya dilakukan pemeriksaan untuk mengetahui apakah terdapat data yang tercatat lebih dari satu kali.</p>
  <p>Pemeriksaan dilakukan terhadap seluruh baris dan kolom id.</p>
  <p>Hasilnya:</p>
  <ul>
    <li>Data duplikat seluruh baris: 0.</li>
    <li>Data dengan ID duplikat: 0.</li>
  </ul>
  <p>Dengan demikian, tidak ditemukan data duplikat pada dataset.</p>

  <h2 class="sub-title">2.4 Penghapusan Kolom</h2>
  <p>Beberapa kolom dihapus karena memiliki terlalu banyak data kosong atau tidak terlalu dibutuhkan dalam analisis.</p>
  <p>Kolom yang dihapus adalah:</p>
  <ul>
    <li><code>size</code></li>
    <li><code>county</code></li>
    <li><code>other_attributes</code></li>
    <li><code>monthly_payment</code></li>
    <li><code>updated_date</code></li>
    <li><code>address_street</code></li>
  </ul>
  <p>Penghapusan dilakukan agar dataset lebih sederhana dan hanya menyimpan kolom yang masih berguna untuk kebutuhan analisis.</p>

  <h2 class="sub-title">2.5 Perubahan Format Data</h2>
  <p>Beberapa kolom memiliki format yang perlu disesuaikan agar dapat digunakan dengan benar.</p>
  <p>Perubahan yang dilakukan adalah:</p>
  <ul>
    <li>Kolom <code>price</code> diubah menjadi format angka.</li>
    <li>Kolom <code>posting_date</code> diubah menjadi format tanggal.</li>
    <li>Kolom <code>updated_date</code> sempat diubah menjadi format tanggal sebelum akhirnya dihapus karena memiliki banyak data kosong.</li>
  </ul>
  <p>Dengan perubahan ini, data menjadi lebih mudah diolah dan dianalisis.</p>

  <h2 class="sub-title">2.6 Pembersihan Data Tidak Wajar</h2>
  <p>Pada tahap ini dilakukan pemeriksaan terhadap tiga kolom utama, yaitu harga kendaraan, tahun produksi, dan jarak tempuh.</p>

  <h3 class="sub-sub-title">A. Harga Kendaraan (price)</h3>
  <p>Ditemukan beberapa nilai harga yang tidak wajar, yaitu:</p>
  <ul>
    <li>Harga $0 sebanyak 10.288 data.</li>
    <li>Harga di atas $1.000.000 sebanyak 71 data.</li>
    <li>Tidak ditemukan harga negatif.</li>
  </ul>
  <p>Harga nol dan harga di atas $1.000.000 dianggap tidak sesuai untuk analisis harga kendaraan. Oleh karena itu, kedua jenis nilai tersebut diubah menjadi data kosong (NaN).</p>
  <p>Total data harga yang diubah menjadi kosong adalah 10.359 data.</p>

  <h3 class="sub-sub-title">B. Tahun Kendaraan (year)</h3>
  <p>Ditemukan 14 kendaraan dengan tahun produksi 1900.</p>
  <p>Setelah diperiksa, beberapa data tersebut memiliki informasi yang tidak sesuai dengan tahun produksinya. Oleh karena itu, nilai tahun 1900 diubah menjadi data kosong.</p>
  <p>Selain itu, ditemukan enam kendaraan dengan tahun produksi 1901. Satu di antaranya memiliki informasi Oldsmobile Curved Dash yang mendukung tahun tersebut. Lima data lainnya tidak memiliki informasi yang cukup untuk memastikan kebenarannya.</p>

  <h3 class="sub-sub-title">C. Jarak Tempuh (odometer)</h3>
  <p>Ditemukan 287 kendaraan dengan jarak tempuh lebih dari 1.000.000 miles.</p>
  <p>Nilai tersebut dianggap tidak wajar untuk kebutuhan analisis ini sehingga diubah menjadi data kosong (NaN).</p>
  <p>Pada tahap ini, baris data tidak dihapus. Hanya nilai yang dianggap tidak wajar yang diubah menjadi kosong agar informasi kendaraan lainnya tetap dapat digunakan.</p>

  <h2 class="sub-title">2.7 Penanganan Data Kosong pada Kategori</h2>
  <p>Data kosong pada beberapa kolom kategori diisi dengan kata Unknown.</p>
  <p>Kolom yang ditangani adalah:</p>
  <ul>
    <li><code>condition</code></li>
    <li><code>cylinders</code></li>
    <li><code>paint_color</code></li>
    <li><code>drive</code></li>
    <li><code>type</code></li>
    <li><code>manufacturer</code></li>
    <li><code>transmission</code></li>
    <li><code>fuel</code></li>
    <li><code>title_status</code></li>
  </ul>
  <p>Pengisian ini dilakukan agar data kendaraan tetap dapat digunakan meskipun informasi pada kolom tersebut tidak tersedia.</p>

  <h2 class="sub-title">2.8 Hasil Akhir Data Processing</h2>
  <p>Setelah seluruh proses pembersihan selesai, dilakukan pemeriksaan kembali untuk memastikan hasilnya.</p>
  <p>Berikut hasil akhir dataset:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th>Keterangan</th>
        <th style="text-align: right;">Hasil</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Jumlah baris</td><td style="text-align: right;">295.451</td></tr>
      <tr><td>Jumlah kolom</td><td style="text-align: right;">35</td></tr>
      <tr><td>Data duplikat</td><td style="text-align: right;">0</td></tr>
      <tr><td>ID duplikat</td><td style="text-align: right;">0</td></tr>
      <tr><td>Data kosong pada price</td><td style="text-align: right;">10.359</td></tr>
      <tr><td>Data kosong pada odometer</td><td style="text-align: right;">4.323</td></tr>
      <tr><td>Data kosong pada year</td><td style="text-align: right;">40</td></tr>
    </tbody>
  </table>

  <p>Dataset yang sudah dibersihkan kemudian disimpan dengan nama <code>vehicles_cleaned.csv</code>.</p>
  <p>Dengan demikian, dataset sudah siap digunakan untuk tahap Data Analysis.</p>

  <div class="page-break"></div>

  <!-- BAB III -->
  <h1 class="section-title">BAB III. DATA ANALYSIS</h1>

  <h2 class="sub-title">3.1 Q1 – Analisis Penyebaran Harga Kendaraan</h2>
  <p>Analisis pertama dilakukan untuk mengetahui bagaimana penyebaran harga kendaraan dalam dataset.</p>
  <p>Analisis ini menggunakan nilai rata-rata, median, kuartil, persentil, histogram, dan boxplot.</p>
  <p>Untuk membuat grafik lebih mudah dibaca, digunakan data harga yang tidak melebihi persentil ke-99, yaitu $89.900. Pembatasan ini hanya digunakan untuk visualisasi, bukan untuk menghapus data dari dataset final.</p>

  <h3 class="sub-sub-title">Hasil Statistik Harga</h3>
  <table class="data-table">
    <thead>
      <tr>
        <th>Statistik</th>
        <th style="text-align: right;">Nilai</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Jumlah data harga valid</td><td style="text-align: right;">285.092</td></tr>
      <tr><td>Rata-rata</td><td style="text-align: right;">$18.313,38</td></tr>
      <tr><td>Median</td><td style="text-align: right;">$12.995</td></tr>
      <tr><td>Harga terendah</td><td style="text-align: right;">$1</td></tr>
      <tr><td>Q1 (25%)</td><td style="text-align: right;">$6.950</td></tr>
      <tr><td>Q3 (75%)</td><td style="text-align: right;">$22.995</td></tr>
      <tr><td>Harga tertinggi</td><td style="text-align: right;">$1.000.000</td></tr>
    </tbody>
  </table>

  <h3 class="sub-sub-title">Hasil persentil harga:</h3>
  <table class="data-table">
    <thead>
      <tr>
        <th>Persentil</th>
        <th style="text-align: right;">Harga</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>25%</td><td style="text-align: right;">$6.950</td></tr>
      <tr><td>50%</td><td style="text-align: right;">$12.995</td></tr>
      <tr><td>75%</td><td style="text-align: right;">$22.995</td></tr>
      <tr><td>90%</td><td style="text-align: right;">$37.985</td></tr>
      <tr><td>95%</td><td style="text-align: right;">$49.997</td></tr>
      <tr><td>99%</td><td style="text-align: right;">$89.900</td></tr>
      <tr><td>99,5%</td><td style="text-align: right;">$110.000</td></tr>
      <tr><td>99,9%</td><td style="text-align: right;">$219.995</td></tr>
    </tbody>
  </table>

  <h3 class="sub-sub-title">Hasil Analisis</h3>
  <p>Berdasarkan hasil tersebut, diketahui bahwa rata-rata harga kendaraan adalah $18.313,38, sedangkan nilai tengahnya adalah $12.995.</p>
  <p>Nilai rata-rata yang lebih tinggi daripada median menunjukkan bahwa terdapat beberapa kendaraan dengan harga tinggi yang membuat rata-rata harga meningkat.</p>
  <p>Sebanyak 50% kendaraan memiliki harga antara $6.950 hingga $22.995.</p>

  <div class="figure">
    <img src="{img_3_1}" alt="Distribusi Harga Kendaraan">
    <div class="figure-caption">Gambar 3.1 Distribusi Harga Kendaraan</div>
  </div>

  <p>Dari histogram, terlihat bahwa sebagian besar kendaraan memiliki harga di bawah $20.000. Semakin tinggi harga kendaraan, jumlah listing yang ditemukan semakin sedikit.</p>
  <p>Dengan demikian, penyebaran harga kendaraan lebih banyak terkumpul pada harga yang relatif rendah, sedangkan kendaraan dengan harga tinggi jumlahnya lebih sedikit.</p>

  <h3 class="sub-sub-title">Kesimpulan Q1</h3>
  <p>Sebagian besar kendaraan dalam dataset memiliki harga pada rentang menengah ke bawah. Hanya sebagian kecil kendaraan yang memiliki harga jauh lebih tinggi dibandingkan kendaraan lainnya.</p>

  <div class="page-break"></div>

  <h2 class="sub-title">3.2 Q2 – Analisis Hubungan Tahun Produksi, Jarak Tempuh, dan Harga</h2>
  <p>Analisis kedua bertujuan untuk mengetahui hubungan antara tahun produksi kendaraan, jarak tempuh, dan harga kendaraan.</p>
  <p>Data yang digunakan berjumlah 275.254 baris. Data dipilih dengan ketentuan:</p>
  <ul>
    <li>Harga kendaraan lebih dari nol.</li>
    <li>Harga tidak melebihi $89.900.</li>
    <li>Jarak tempuh lebih dari nol dan tidak melebihi persentil ke-99.</li>
    <li>Tahun kendaraan tidak lebih dari 2026.</li>
    <li>Data kosong pada ketiga kolom tidak digunakan dalam perhitungan.</li>
  </ul>

  <h3 class="sub-sub-title">Statistik Data Q2</h3>
  <table class="data-table">
    <thead>
      <tr>
        <th>Statistik</th>
        <th style="text-align: right;">Year</th>
        <th style="text-align: right;">Odometer</th>
        <th style="text-align: right;">Price</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Jumlah data</td><td style="text-align: right;">275.254</td><td style="text-align: right;">275.254</td><td style="text-align: right;">275.254</td></tr>
      <tr><td>Rata-rata</td><td style="text-align: right;">2012,68</td><td style="text-align: right;">110.070,74</td><td style="text-align: right;">$16.991,01</td></tr>
      <tr><td>Median</td><td style="text-align: right;">2015</td><td style="text-align: right;">108.534,50</td><td style="text-align: right;">$12.950</td></tr>
      <tr><td>Minimum</td><td style="text-align: right;">1901</td><td style="text-align: right;">1</td><td style="text-align: right;">$1</td></tr>
      <tr><td>Maksimum</td><td style="text-align: right;">2026</td><td style="text-align: right;">290.000</td><td style="text-align: right;">$89.900</td></tr>
    </tbody>
  </table>

  <h3 class="sub-sub-title">A. Korelasi Pearson</h3>
  <p>Korelasi Pearson digunakan untuk mengetahui arah dan kekuatan hubungan antara dua variabel secara linear.</p>
  <p>Hasil perhitungannya:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th>Hubungan</th>
        <th style="text-align: center;">Nilai Pearson</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Year – Odometer</td><td style="text-align: center;">-0,138</td></tr>
      <tr><td>Year – Price</td><td style="text-align: center;">+0,209</td></tr>
      <tr><td>Odometer – Price</td><td style="text-align: center;">-0,496</td></tr>
    </tbody>
  </table>

  <p>Penjelasan:</p>
  <ul>
    <li><strong>Year dan Odometer:</strong> Memiliki hubungan negatif yang sangat lemah. Kendaraan yang lebih baru cenderung memiliki jarak tempuh lebih rendah.</li>
    <li><strong>Year dan Price:</strong> Memiliki hubungan positif yang lemah. Kendaraan yang lebih baru cenderung memiliki harga lebih tinggi.</li>
    <li><strong>Odometer dan Price:</strong> Memiliki hubungan negatif sedang. Kendaraan dengan jarak tempuh lebih tinggi cenderung memiliki harga lebih rendah.</li>
  </ul>

  <h3 class="sub-sub-title">B. Korelasi Spearman</h3>
  <p>Korelasi Spearman digunakan untuk melihat hubungan antara dua variabel berdasarkan urutan atau peringkat nilainya.</p>
  <p>Hasil perhitungannya:</p>

  <table class="data-table">
    <thead>
      <tr>
        <th>Hubungan</th>
        <th style="text-align: center;">Nilai Spearman</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Year – Odometer</td><td style="text-align: center;">-0,424</td></tr>
      <tr><td>Year – Price</td><td style="text-align: center;">+0,523</td></tr>
      <tr><td>Odometer – Price</td><td style="text-align: center;">-0,538</td></tr>
    </tbody>
  </table>

  <p>Penjelasan:</p>
  <ul>
    <li><strong>Year dan Odometer:</strong> Kendaraan yang lebih baru cenderung memiliki jarak tempuh lebih rendah.</li>
    <li><strong>Year dan Price:</strong> Kendaraan yang lebih baru cenderung memiliki harga lebih tinggi.</li>
    <li><strong>Odometer dan Price:</strong> Kendaraan dengan jarak tempuh lebih tinggi cenderung memiliki harga lebih rendah.</li>
  </ul>

  <h3 class="sub-sub-title">C. Analisis Scatter Plot</h3>
  <div class="figure">
    <img src="{img_3_2}" alt="Hubungan Tahun Kendaraan dan Odometer terhadap Harga">
    <div class="figure-caption">Gambar 3.2 Hubungan Tahun Kendaraan dan Odometer terhadap Harga</div>
  </div>

  <p>Berdasarkan grafik hubungan tahun kendaraan dengan harga, terlihat bahwa kendaraan yang lebih baru cenderung memiliki harga lebih tinggi. Namun, harga kendaraan pada tahun yang sama masih memiliki perbedaan yang cukup besar.</p>
  <p>Pada grafik hubungan jarak tempuh dengan harga, terlihat bahwa kendaraan dengan jarak tempuh rendah memiliki harga yang lebih bervariasi. Sementara itu, kendaraan dengan jarak tempuh tinggi lebih banyak ditemukan pada rentang harga yang lebih rendah.</p>

  <h3 class="sub-sub-title">Kesimpulan Q2</h3>
  <p>Hasil analisis menunjukkan bahwa tahun produksi dan jarak tempuh memiliki hubungan dengan harga kendaraan.</p>
  <p>Kendaraan yang lebih baru cenderung memiliki harga lebih tinggi, sedangkan kendaraan dengan jarak tempuh lebih tinggi cenderung memiliki harga lebih rendah.</p>
  <p>Namun, hubungan tersebut tidak berarti bahwa tahun produksi dan jarak tempuh merupakan satu-satunya hal yang menentukan harga kendaraan. Masih terdapat faktor lain yang dapat memengaruhi harga.</p>

  <div class="page-break"></div>

  <h2 class="sub-title">3.3 Q3 – Analisis Harga Berdasarkan Merek, Bahan Bakar, dan Transmisi</h2>
  <p>Analisis ketiga dilakukan untuk membandingkan harga kendaraan berdasarkan tiga kategori, yaitu merek kendaraan (manufacturer), jenis bahan bakar (fuel), dan jenis transmisi (transmission).</p>
  <p>Jumlah data yang digunakan adalah 282.257 baris. Data harga yang digunakan lebih dari nol dan tidak melebihi persentil ke-99, yaitu $89.900.</p>
  <p>Perbandingan dilakukan menggunakan boxplot untuk melihat nilai tengah harga dan perbedaan penyebaran harga pada setiap kategori.</p>

  <h3 class="sub-sub-title">A. Harga Berdasarkan Manufacturer</h3>
  <p>Analisis manufacturer menampilkan sepuluh kategori manufacturer dengan jumlah listing terbanyak, termasuk kategori Unknown untuk kendaraan yang tidak memiliki informasi merek. Berdasarkan boxplot, ditemukan bahwa:</p>
  <ul>
    <li>RAM memiliki nilai tengah harga paling tinggi di antara sepuluh merek yang ditampilkan.</li>
    <li>GMC juga memiliki nilai tengah harga yang cukup tinggi.</li>
    <li>Nissan memiliki nilai tengah harga paling rendah.</li>
    <li>Ford, Toyota, Chevrolet, dan Jeep memiliki penyebaran harga yang cukup luas.</li>
    <li>Terdapat beberapa kendaraan dengan harga jauh lebih tinggi dibandingkan sebagian besar kendaraan dalam kategori yang sama.</li>
  </ul>
  <p>Hasil ini menunjukkan bahwa setiap merek kendaraan memiliki penyebaran harga yang berbeda.</p>

  <h3 class="sub-sub-title">B. Harga Berdasarkan Fuel</h3>
  <p>Berdasarkan boxplot jenis bahan bakar, ditemukan bahwa:</p>
  <ul>
    <li>Diesel memiliki nilai tengah harga paling tinggi.</li>
    <li>Electric berada di urutan kedua.</li>
    <li>Other dan Hybrid memiliki nilai tengah harga pada kelompok menengah.</li>
    <li>Gas memiliki nilai tengah harga paling rendah.</li>
  </ul>
  <p>Hal ini menunjukkan bahwa harga kendaraan dalam dataset memiliki perbedaan berdasarkan jenis bahan bakarnya.</p>

  <h3 class="sub-sub-title">C. Harga Berdasarkan Transmission</h3>
  <p>Berdasarkan boxplot jenis transmisi, ditemukan bahwa:</p>
  <ul>
    <li>Other memiliki nilai tengah harga paling tinggi.</li>
    <li>Unknown memiliki nilai tengah harga yang relatif tinggi.</li>
    <li>Automatic dan Manual memiliki nilai tengah harga yang cukup berdekatan.</li>
    <li>Setiap kategori memiliki penyebaran harga yang berbeda.</li>
    <li>Kategori Other dan Unknown perlu diperhatikan karena keduanya tidak menunjukkan jenis transmisi yang spesifik.</li>
  </ul>

  <div class="figure">
    <img src="{img_3_3}" alt="Distribusi Harga Kendaraan Berdasarkan Manufacturer, Fuel, dan Transmission">
    <div class="figure-caption">Gambar 3.3 Distribusi Harga Kendaraan Berdasarkan Manufacturer, Fuel, dan Transmission</div>
  </div>

  <h3 class="sub-sub-title">Kesimpulan Q3</h3>
  <p>Hasil analisis menunjukkan bahwa harga kendaraan memiliki perbedaan berdasarkan merek, jenis bahan bakar, dan jenis transmisi.</p>
  <p>RAM memiliki nilai tengah harga tertinggi di antara sepuluh merek yang dianalisis. Berdasarkan jenis bahan bakar, diesel memiliki nilai tengah harga tertinggi. Sementara itu, berdasarkan transmisi, kategori Other memiliki nilai tengah harga tertinggi.</p>
  <p>Perbedaan ini menunjukkan bahwa karakteristik kendaraan berkaitan dengan variasi harga yang ditemukan dalam dataset. Namun, hasil ini tidak membuktikan bahwa karakteristik tersebut secara langsung menyebabkan harga menjadi lebih tinggi atau lebih rendah.</p>

  <div class="page-break"></div>

  <!-- BAB IV -->
  <h1 class="section-title">BAB IV. KESIMPULAN</h1>

  <h2 class="sub-title">4.1 Kesimpulan Umum</h2>
  <p>Berdasarkan seluruh proses yang telah dilakukan, dapat disimpulkan bahwa:</p>
  <ul>
    <li>Dataset awal memiliki 295.451 baris dan 41 kolom. Setelah dibersihkan, dataset memiliki 295.451 baris dan 35 kolom.</li>
    <li>Proses Data Processing berhasil menangani data kosong, nilai yang tidak wajar, dan beberapa kolom yang tidak diperlukan.</li>
    <li>Hasil analisis Q1 menunjukkan bahwa sebagian besar kendaraan memiliki harga yang relatif rendah, sedangkan kendaraan dengan harga tinggi jumlahnya lebih sedikit.</li>
    <li>Hasil analisis Q2 menunjukkan bahwa kendaraan dengan tahun produksi lebih baru cenderung memiliki harga lebih tinggi. Sebaliknya, kendaraan dengan jarak tempuh lebih tinggi cenderung memiliki harga lebih rendah.</li>
    <li>Hasil analisis Q3 menunjukkan bahwa harga kendaraan memiliki perbedaan berdasarkan merek, jenis bahan bakar, dan jenis transmisi.</li>
  </ul>
  <p>Secara keseluruhan, Data Processing membuat data lebih siap digunakan, sedangkan Data Analysis membantu memberikan gambaran mengenai harga dan karakteristik kendaraan.</p>

  <h2 class="sub-title">4.2 Keterbatasan Analisis</h2>
  <p>Dalam pengerjaan ini terdapat beberapa keterbatasan, yaitu:</p>
  <ul>
    <li>Harga yang tercatat merupakan harga pada listing kendaraan dan belum tentu merupakan harga akhir saat transaksi.</li>
    <li>Beberapa informasi kendaraan masih kosong, seperti VIN dan informasi lokasi.</li>
    <li>Batas nilai yang digunakan untuk menangani anomali merupakan aturan yang ditentukan dalam proses analisis.</li>
    <li>Analisis Q2 dan Q3 menggunakan sebagian data yang telah disaring sesuai kebutuhan masing-masing analisis.</li>
    <li>Hasil korelasi hanya menunjukkan hubungan antarvariabel dan tidak membuktikan bahwa satu variabel menyebabkan perubahan pada variabel lainnya.</li>
  </ul>

  <h1 class="section-title">PENUTUP</h1>
  <p>Melalui tugas ini, dilakukan pemeriksaan, pembersihan, dan analisis terhadap dataset Craigslist Cars & Trucks. Proses tersebut membantu memahami kondisi data sekaligus menemukan beberapa pola harga kendaraan berdasarkan informasi yang tersedia.</p>

  <h1 class="section-title">DAFTAR PUSTAKA</h1>
  <p>Austin Reese. (n.d.). Used cars dataset. Kaggle. <a href="https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data" target="_blank">https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data</a></p>

</div>

</body>
</html>
"""

with open("Laporan_Tubes1_Data_Sains.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("File 'Laporan_Tubes1_Data_Sains.html' successfully updated!")
