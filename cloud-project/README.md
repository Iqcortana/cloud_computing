# Dokumentasi Singkat

komputasi awan dan containerization memberikan gambaran umum mengenai peran teknologi cloud dalam pengembangan aplikasi modern. dalam dokumentasi ini dituliskan dokumentasi untuk mengakses API Flask dan React + Vite

## API Sederhana dengan Flask

### 📌 Deskripsi

Proyek ini adalah API sederhana menggunakan Flask yang mengembalikan pesan JSON ketika diakses melalui endpoint /.

### 🎯 Tujuan
- Memahami dasar penggunaan Flask.
- Membuat dan menjalankan server lokal dengan Flask.
- Membuat endpoint sederhana yang mengembalikan JSON response.

### 🛠️ Cara Menjalankan

#### 1. Buat dan Aktifkan Virtual Environment

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

#### 2. Instal Dependensi

Pastikan semua dependensi yang dibutuhkan telah terinstal dengan menjalankan perintah berikut:

```
pip install -r requirements.txt
```

#### 3. Jalankan Server Flask

pip install -r requirements.txt

```
python app.py
```

#### 4. Akses API

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

### 📂 Struktur Proyek
Virtual Environment(venv) diinstal di terminal menggunakan perintah
```

```

```
backend/
├── venv/              # Virtual environment (disarankan untuk tidak di-commit ke Git)
├── app.py             # File utama Flask
├── requirements.txt   # Daftar library yang diperlukan
├── README.md          # Dokumentasi proyek
```

### 🔄 Catatan

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

## Proyek 2: Membuat Aplikasi Frontend Sederhana dengan React + Vite

### 📌 Deskripsi
Pembuatan kerangka kerja React menggunakan Vite untuk frontend. Tujuan utamanya adalah membuat tampilan dasar dan menampilkan tulisan sederhana untuk memastikan React berhasil dijalankan dengan Vite saat mengakses localhost http://localhost:5173/.

### 🎯 Tujuan
Mampu menjalankan aplikasi React di local development server menggunakan Vite.

### 🛠️ Cara Menjalankan

#### 1. Membuat Proyek React dengan Vite

Jalankan perintah berikut untuk membuat proyek React dengan Vite:

```sh
cd ../frontend
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

Setelah menjalankan `npm run dev`, salin URL lokal (misalnya, `http://127.0.0.1:5173/`) dari terminal dan buka di browser.

#### 2. Struktur Direktori React + Vite
```
frontend/
└─ my-react-app/
    ├─ src/
    ├─ public/
    ├─ package.json
    ├─ vite.config.js
    └─ ...
```

#### 3. Membuat Halaman Sederhana
Buka `src/App.jsx` dan ganti konten default dengan:

```jsx
import React from 'react';

function App() {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Hello from React + Vite!</h1>
      <p>This is a simple React app built with Vite.</p>
    </div>
  );
}

export default App;
```

#### 4. Menjalankan Aplikasi React + Vite
Jalankan aplikasi React + Vite dengan perintah:

```sh
npm run dev
```

Pastikan terminal menampilkan informasi seperti:
```
Local: http://127.0.0.1:5173/
```

Akses aplikasi di browser menggunakan URL yang diberikan (biasanya `http://127.0.0.1:5173/`).

## Proyek 4 : Menghubungkan React ke Flask

### 📌 Deskripsi
Pemanggilan API Flask dari React. Tujuannya adalah agar frontend dapat menampilkan data yang didapat dari backend.

### 🎯 Tujuan
- Memahami konsep fetching data di React.
- Dapat membuat permintaan (GET) ke API Flask dan menampilkannya di React.

### 🛠️ Cara Menjalankan

#### 1. Menambahkan Endpoint di Flask
Tambahkan endpoint berikut di app.py:
```
@app.route('/api/data')
def get_data():
    return jsonify({"data": "Hello from Flask API"})
```

Penting: Urutan Definisi Fungsi
Pastikan fungsi get_data() didefinisikan di atas blok berikut dalam app.py:
```
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
Kode yang benar harus terlihat seperti ini:
```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/data')
def get_data():
    return jsonify({"data": "Hello from Flask API"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

#### 2. Menjalankan Flask
Pastikan Anda berada dalam virtual environment. Jika belum aktif, jalankan perintah berikut:
```
source venv/bin/activate  # Untuk Linux/MacOS
.\venv\Scripts\activate  # Untuk Windows
```
Jalankan server Flask dengan perintah:
```
python app.py
```
Pastikan endpoint dapat diakses di http://localhost:5000/api/data.

Catatan: Tidak perlu mematikan terminal server Flask. Buka tab baru atau terminal baru untuk menjalankan frontend React.

#### 3. Memanggil Endpoint dari React
Buka src/App.jsx pada proyek React dan ganti kontennya dengan kode berikut:
```
import React, { useState, useEffect } from 'react';

function App() {
  const [apiData, setApiData] = useState(null);

  useEffect(() => {
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => {
        setApiData(data.data);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>React & Flask Integration</h1>
      <p>{apiData ? apiData : "Loading data..."}</p>
    </div>
  );
}

export default App;
```

#### 4. Menjalankan Aplikasi React
Di terminal proyek React (frontend/my-react-app), jalankan perintah:
```
npm run dev
```
Buka browser ke http://localhost:5173/.

## Proyek 5 : Integrasi Flask dengan PostgreSQL

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

# Praktikum 6: Dockerfile untuk Backend Flask

## 📄 Deskripsi Singkat
Kami telah berhasil membuat Dockerfile untuk backend Flask sehingga aplikasi dapat dijalankan dalam kontainer.

## 🎯 Tujuan Pembelajaran
- Memahami sintaks dasar Dockerfile.
- Mampu membangun Docker image untuk aplikasi Flask.

## 👩‍💻 Pembagian Tugas Tim
- **Backend Engineer**: Menyusun Dockerfile untuk Flask.
- **Infrastructure Engineer**: Menjalankan container dan menguji image yang telah dibuat.

## 🛠️ Langkah-Langkah Praktikum

### Persiapan Awal
Sebelum menjalankan perintah Docker, kami memastikan bahwa Docker Desktop sudah berjalan. Jika belum, menjalankan `docker info` akan menghasilkan error seperti berikut:

```
Server:
ERROR: error during connect: Get "http://%2F%2F.%2Fpipe%2FdockerDesktopLinuxEngine/v1.47/info": open //./pipe/dockerDesktopLinuxEngine: The system cannot find the file specified.
```

Untuk mengatasinya, kami membuka aplikasi Docker Desktop dan menunggu hingga status **"Docker is running"** muncul.

### Membuat Dockerfile
Kami membuat file **Dockerfile** di dalam folder `backend` dengan isi sebagai berikut:

```dockerfile
# backend/Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

### Menyiapkan requirements.txt
Kami menambahkan dependensi berikut ke dalam file **requirements.txt**:

```
flask
flask-cors
psycopg2-binary
```

### Build Docker Image
Setelah semua file siap, kami membangun image Docker dengan perintah:

```
cd backend
docker build -t flask-backend:1.0 .
```

### Menjalankan Docker Container
Ketika image telah berhasil dibuat, kami menjalankan container menggunakan perintah berikut:

```
docker run -d -p 5000:5000 --name flask-container flask-backend:1.0
```

### Verifikasi di Browser
Kami kemudian memverifikasi bahwa aplikasi Flask berjalan dengan mengakses [http://localhost:5000](http://localhost:5000) di browser.

### ✅ Selesai!

## 📂 Struktur Keseluruhan
### A. Backend
1. Virtual Environment berisi semua library yang digunakan dalam proyek ini seperti Flask dan Flask-cors
2. app.py merupakan kode utama untuk backend. dijalankan menggunakan bahasa Python yang menggunakan Framework Flask dan library Flask-CORS
3. requirements.txt dibuat otomatis menggunakan perintah
```
pip freeze > requirements.txt
```

### B. Database
Untuk sekarang masih kosong, rencananya akan disambungkan dengan PostgreSQL.

### C. Frontend
1. berisi direktori my-react-app yang diinstal melalui terminal(instalasi React.JS) berisi file default framework React.JS.
2. file src/App.jsx merupakan file utama dalam tampilan frontend dalam proyek ini

```
backend/
├── venv/              # Virtual environment (disarankan untuk tidak di-commit ke Git)
├── app.py             # File utama Flask
├── requirements.txt   # Daftar library yang diperlukan
├── README.md          # Dokumentasi proyek
db/
frontend/
└─ my-react-app/
    ├─ src/
    ├─ public/
    ├─ package.json
    ├─ vite.config.js
    └─ ...
```
