# API Sederhana dengan Flask

## 📌 Deskripsi

Proyek ini adalah API sederhana menggunakan Flask yang mengembalikan pesan JSON ketika diakses melalui endpoint /.

## 🎯 Tujuan
- Memahami dasar penggunaan Flask.
- Membuat dan menjalankan server lokal dengan Flask.
- Membuat endpoint sederhana yang mengembalikan JSON response.

## 🛠️ Cara Menjalankan

### 1. Buat dan Aktifkan Virtual Environment

Sebelum menjalankan proyek, pastikan virtual environment sudah diaktifkan.

- **Windows:**
```
python -m venv venv
venv\Scripts\activate
```

- **Mac/Linux:**
```
python3 -m venv venv
source venv/bin/activate
```

### 2. Instal Dependensi

Pastikan semua dependensi yang dibutuhkan telah terinstal dengan menjalankan perintah berikut:

```
pip install -r requirements.txt
```

### 3. Jalankan Server Flask

pip install -r requirements.txt

```
python app.py
```

### 4. Akses API

Buka browser atau gunakan Postman untuk mengakses API di:

```
http://127.0.0.1:5000/
```

Jika berhasil, akan mendapatkan response JSON seperti berikut:

```
{
  "message": "Hello from Flask!"
}
```

## 📂 Struktur Proyek

```
backend/
├── venv/              # Virtual environment (disarankan untuk tidak di-commit ke Git)
├── app.py             # File utama Flask
├── requirements.txt   # Daftar library yang diperlukan
├── README.md          # Dokumentasi proyek
```

## 🔄 Catatan

Jika terdapat error terkait izin eksekusi skrip di Windows, jalankan perintah berikut di PowerShell sebagai Administrator:
```
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Jika Flask belum terinstal, jalankan:
```
pip install Flask
```

Untuk keluar dari virtual environment, gunakan perintah berikut:
```
deactivate
```