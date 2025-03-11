# Dokumentasi Singkat

## Integrasi Flask dengan PostgreSQL

### 📄 Deskripsi Singkat

Proyek ini adalah implementasi sederhana dari aplikasi web berbasis Flask yang terintegrasi dengan database PostgreSQL. Pengguna dapat melakukan operasi CRUD (Create, Read, Update, Delete) pada database PostgreSQL menggunakan API yang disediakan.

### 🎯 Tujuan Pembelajaran
- Menghubungkan aplikasi Flask dengan PostgreSQL.
- Memahami cara kerja database relational dalam konteks aplikasi web.
- Mengimplementasikan operasi CRUD menggunakan Flask dan PostgreSQL.

### 🛠 Persyaratan Sistem
Sebelum memulai, pastikan sistem Anda memiliki:
- Python 3.x terinstal
- PostgreSQL terinstal dan dikonfigurasi
- Virtual Environment Python

### 🚀 Instalasi dan Konfigurasi

#### 1. Clone Repository

```
git clone https://github.com/Iqcortana/cloud_computing.git
cd cloud-project\backend
```

#### 2. Buat dan Aktifkan Virtual Environment

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

#### 3. Instal Dependensi

Instal dependensi berikut agar frontend dapat mengakses endpoint dari backend:

```
pip install flask flask-cors
```

Juga menginstal dependensi berikut jika membuat virtual environment ulang di komputer lain :
```
pip install -r requirements.txt
```

#### 4. Instal dan Konfigurasi PostgreSQL

Pastikan PostgreSQL telah terinstal dan jalankan perintah berikut untuk membuat database:

```
CREATE DATABASE test_db;
CREATE USER student WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE test_db TO student;
```

Jika perlu, buat tabel dengan perintah berikut:

```
CREATE TABLE IF NOT EXISTS items (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  description TEXT
);
```

#### 5. Konfigurasi Koneksi Database di app.py

Pastikan app.py memiliki konfigurasi koneksi seperti berikut:

```
import psycopg2
from flask import Flask, jsonify, request

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="test_db",
        user="student",
        password="password"
    )
    return conn
```

### 🔧 Menjalankan Aplikasi

Jalankan server Flask dengan perintah berikut:

```
python app.py
```

Aplikasi akan berjalan di http://127.0.0.1:5000.

### 🔍 Menguji API dengan Postman


#### 1. Menjalankan POST Request (Menambah data baru)

- URL: http://127.0.0.1:5000/api/items
- Method: POST
- Headers: Content-Type: application/json
- Body (JSON):

```
{
  "name": "Item 1",
  "description": "Description Item 1"
}
```

- Response :

``` 
{
    "description": "Description Item 1",
    "id": 1,
    "name": "Item 1"
}
```

#### 2. Menjalankan GET Request (Membaca data)

- URL: http://127.0.0.1:5000/api/items
- Method: GET
- Response:

```
[
    {
        "description": "Description Item 1",
        "id": 1,
        "name": "Item 1"
    }
]
```

Ulangi langkah di atas untuk menguji fitur CRUD lainnya seperti Update dan Delete.

### ✅ Selesai!

Sekarang Anda telah berhasil menjalankan proyek Flask dengan PostgreSQL dan menguji API menggunakan Postman! 🚀