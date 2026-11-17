# Analisis Data Craigslist Cars & Trucks
### Tugas Besar 1 / Ujian Tengah Semester (UTS) — Data Sains

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AliefReefandi/Data_sains/blob/main/UTS_Data_Science_Kendaraan.ipynb)

Repository ini memuat proyek analisis data komprehensif terhadap dataset **Craigslist Cars & Trucks**, mencakup tahapan pemeriksaan struktur data, analisis eksploratif (EDA Q1–Q3), pembersihan dan validasi data (*Data Processing & Imputation*), serta analisis korelasi statistik (*Pearson & Spearman*).

---

## 🚀 Buka Langsung di Google Colab

Kamu bisa langsung menjalankan notebook ini di Google Colab tanpa perlu instalasi apa pun:

👉 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AliefReefandi/Data_sains/blob/main/UTS_Data_Science_Kendaraan.ipynb)

*(Tautan langsung: [Buka di Google Colab](https://colab.research.google.com/github/AliefReefandi/Data_sains/blob/main/UTS_Data_Science_Kendaraan.ipynb))*

---

## 📂 Struktur Berkas Repository

```text
├── UTS_Data_Science_Kendaraan.ipynb       # Jupyter Notebook utama (lengkap dengan output visualisasi)
├── images/                                # Direktori grafik dan visualisasi pendukung
├── .gitignore                             # Konfigurasi standar git
└── README.md                              # Dokumentasi proyek & tombol Open in Colab
```

---

## 📊 Dataset yang Digunakan

* **Nama Dataset:** Craigslist Cars & Trucks Data (Kaggle)
* **Penulis / Sumber:** Austin Reese
* **Tautan Dataset:** [Kaggle - Craigslist Cars & Trucks Data](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data/data)
* **Dimensi Awal:** 295.451 baris dan 41 kolom (~92,4 MB)

---

## 🎯 Tahapan & Hasil Analisis Inti

### 1. Struktur Data & Kualitas Awal
* **Dimensi Awal:** 295.451 baris dan 41 kolom.
* **Duplikasi:** 0 baris duplikat identik dan 0 ID duplikat.
* **Missing Values Awal:** Kolom `size` dan `county` 100% kosong, `monthly_payment` 97,95% kosong, `other_attributes` 90,48% kosong.

### 2. Exploratory Data Analysis (EDA)
* **Q1 (Distribusi Harga):**
  * Bentuk distribusi: *Right-Skewed* (menceng ke kanan).
  * Median ($Q_2$): **$12.995** | $Q_1$ (25%): **$6.950** | $Q_3$ (75%): **$22.995** | IQR: **$16.045**.
  * Persentil ke-99: **$89.900**.
  * Ditemukan 10.288 data berharga $0 dan 71 data berharga fiktif > $1.000.000.
* **Q2 (Hubungan Usia & Jarak Tempuh):**
  * Tahun produksi berkorelasi positif dengan harga (mobil baru cenderung bernilai lebih tinggi).
  * Odometer berkorelasi negatif dengan harga (semakin tinggi km, harga terkonsentrasi di batas bawah).
* **Q3 (Segmentasi Karakteristik):**
  * **Merek:** RAM memiliki median harga tertinggi ($23.450) karena segmen truk *heavy-duty*, diikuti GMC ($18.985), dan Nissan terendah ($10.599).
  * **Bahan Bakar:** Diesel mencatat median tertinggi ($33.900), disusul Electric ($23.499,50), sedangkan bensin biasa (Gas) memiliki median terendah ($11.500).
  * **Transmisi:** Transmisi otomatis mendominasi 86,3% listing pasar.

### 3. Data Processing (Cleaning, Validation, & Imputation)
* **Drop Kolom:** Menghapus kolom 100% kosong (`size`, `county`) dan minim data (`monthly_payment`, `other_attributes`, `updated_date`, `address_street`).
* **Standarisasi:** Mengonversi `price` menjadi numerik float64 serta `posting_date` menjadi format datetime UTC.
* **Handling Anomali:** Mengubah harga $0, harga > $1.000.000, tahun 1900, dan odometer > 1.000.000 mil menjadi `NaN`.
* **Validasi Integritas:** Memverifikasi konsistensi koordinat geografis (149 data kosong pada lat dan long secara berpasangan, 100% konsisten) dan URL gambar (`image_url` vs `image_urls`).
* **Imputasi:** Mengisi nilai kosong fitur kategorikal dengan kategori `'Unknown'`.
* **Hasil Akhir:** Dataset bersih berukuran **295.451 baris dan 35 kolom** (`vehicles_cleaned.csv`).

### 4. Analisis Korelasi (Data yang Dikorelasikan)
Korelasi dihitung pada **275.254 data kendaraan valid** untuk 3 variabel numerik kontinu: **Tahun Produksi (`year`)**, **Jarak Tempuh (`odometer`)**, dan **Harga (`price`)**.

| Pasangan Variabel | Pearson ($r$) | Spearman ($\rho$) | Sifat Hubungan |
| :--- | :---: | :---: | :--- |
| **Year — Price** | **+0,209** | **+0,523** | Positif Sedang (Kurvilinear / Non-linear) |
| **Odometer — Price** | **-0,496** | **-0,538** | Negatif Sedang (Penurunan nilai konsisten) |
| **Year — Odometer** | **-0,138** | **-0,424** | Negatif Sedang (Mobil tua memiliki jarak tempuh lebih tinggi) |

> **Insight Ilmiah:** Nilai korelasi Spearman (+0,523) jauh melampaui Pearson (+0,209) pada *Year vs Price* karena **depresiasi harga kendaraan bersifat non-linear (kurvilinear)**. Nilai mobil jatuh drastis pada beberapa tahun awal pemakaian kemudian melandai pada tahun-tahun berikutnya.

---

## 🚀 Panduan Menjalankan Notebook

Notebook `UTS_Data_Science_Kendaraan.ipynb` telah dioptimalkan agar dapat dijalankan secara fleksibel:

### A. Dijalankan di Google Colab (1-Klik)
1. Klik tombol badge: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/AliefReefandi/Data_sains/blob/main/UTS_Data_Science_Kendaraan.ipynb)
2. Unggah `vehicles.csv` atau `Datasets.zip` ke storage session Colab jika ingin me-run ulang seluruh sel dari awal.
3. Jalankan seluruh sel secara berurutan (*Runtime* $\to$ *Run all*).

### B. Dijalankan di Komputer Lokal (Jupyter Notebook / VS Code)
1. Clone repository:
   ```bash
   git clone https://github.com/AliefReefandi/Data_sains.git
   cd Data_sains
   ```
2. Pastikan file `vehicles.csv` berada di direktori kerja (atau di folder `datasets/`).
3. Buka dan jalankan `UTS_Data_Science_Kendaraan.ipynb`.
