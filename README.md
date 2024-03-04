# Analisis Data Dicoding

## Deskripsi
Proyek ini berfokus pada analisis data dari sistem penyewaan/rental sepeda otomatis. Data yang digunakan dalam proyek ini berasal dari dua file CSV: `day.csv` dan `hour.csv` pada tahun 2011 dan 2012.

## Tujuan
Tujuan dari proyek ini adalah untuk memahami pola penggunaan sistem berbagi sepeda dan memberikan wawasan yang dapat membantu meningkatkan layanan.

## Metodologi
1. **Pemuatan Data**: Memuat data dari file CSV ke dalam DataFrame pandas.
2. **Pembersihan Data**: Memeriksa dan menangani nilai yang hilang atau tidak valid dalam data. Kemudian, mengubah nama variabel dan melakukan kategori agar data lebih mudah dibaca.
3. **Eksplorasi Data**: Melakukan analisis eksplorasi data untuk memahami distribusi dan hubungan antar variabel.
4. **Visualisasi Data**: Menampilkan hasil yang didapat dari eksplorasi data

## Hasil
- Jumlah penyewaan tiap tahunnya meningkat. Pola penyewaan tiap bulannya sama dari tahun 2011 hingga 2012. Dari Januari hingga tengah tahun menaik dan mulai menurun hingga desember. Waktu tinggi penyewaan adalah ketika siang-sore hari dari jam 1 siang hingga 6 sore. 
- Jumlah penyewaan akan tinggi sesuai dengan kecerahan cuaca. Jika cuaca cerah, kelembapan rendah, kecepatan angin rendah, dan suhu lingkungan tinggi maka akan semakin tinggi penyewaan. Sedangkan penyewaan akan menurun jika pada hari kerja.

## Dashboard

### Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

### Run steamlit app
```bash
streamlit run ./dashboard/dashboard.py
```
