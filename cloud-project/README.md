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
