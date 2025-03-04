# Dokumentasi Singkat

## Menghubungkan React ke Flask

### 📄 Deskripsi Singkat

Pada tahap ini, mahasiswa akan mempelajari cara memanggil API Flask dari React. Tujuannya adalah agar frontend dapat menampilkan data yang didapat dari backend dengan cara yang efisien dan optimal.

### 🎯 Tujuan Pembelajaran
- Mahasiswa memahami konsep fetching data di React.
- Mahasiswa dapat membuat permintaan (GET) ke API Flask dan menampilkannya di React.
- Mahasiswa memahami cara menangani error saat melakukan request ke API.

## Proyek 1 : API Sederhana dengan Flask

### 📌 Deskripsi

Proyek ini adalah API sederhana menggunakan Flask yang mengembalikan pesan JSON ketika diakses melalui endpoint /api/data. API ini akan digunakan oleh React sebagai sumber data.

### 🎯 Tujuan
- Memahami dasar penggunaan Flask.
- Membuat dan menjalankan server lokal dengan Flask.
- Membuat endpoint sederhana yang mengembalikan JSON response.
- Mengatur CORS agar React dapat mengakses API dengan aman.

### 🛠️ Langkah-langkah

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

Instal dependensi berikut agar frontend dapat mengakses endpoint dari backend:

```
pip install flask flask-cors
```

Juga menginstal dependensi berikut jika membuat virtual environment ulang di komputer lain :
```
pip install -r requirements.txt
```

#### 3. Tambahkan Endpoint di Flask

Buka app.py dan tambahkan kode berikut:
```py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/api/data')
def get_data():
    return jsonify({"data": "Hello from Flask API"})

// Latihan Mandiri
@app.route('/api/info')
def info():
  return jsonify({
    "Nama": "Taufik Ilham",
    "Nim": "10221081",
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

#### 3. Jalankan Server Flask

```
python app.py
```

#### 4. Akses API

Buka browser atau gunakan Postman untuk mengakses API di:

```
http://127.0.0.1:5000/

// Jika berhasil, akan menampilkan response JSON
{
  "message": "Hello from Flask!"
}
```

```
http://127.0.0.1:5000/api/data

// Jika berhasil, akan menampilkan response JSON
{
  "message": "Hello from Flask API!"
}
```

```
http://127.0.0.1:5000/api/info

// Jika berhasil, akan menampilkan response JSON
{
  "Nama": "Taufik Ilham",
  "Nim": "10221081"
}
```

### 📂 Struktur Proyek

```
backend/
├── venv/              # Virtual environment (disarankan untuk tidak di-commit ke Git)
├── app.py             # File utama Flask
├── requirements.txt   # Daftar library yang diperlukan
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

## Proyek 2: Menghubungkan React ke Flask

### 📌 Deskripsi
Pembuatan kerangka kerja React menggunakan Vite untuk frontend. Tujuan utamanya adalah menghubungkan React dengan API Flask dan menampilkan data dari backend.

### 🎯 Tujuan
- Mampu menjalankan aplikasi React di local development server menggunakan Vite.
- Mampu mengambil data dari Flask API dan menampilkannya dengan React.
- Memahami konsep useEffect dan useState dalam React.
- Menghandle error saat melakukan request ke API.

### 🛠️ Langkah-langkah

#### 1. Membuat Proyek React dengan Vite

Jalankan perintah berikut untuk membuat proyek React dengan Vite:

```
cd ../frontend
npm create vite@latest my-react-app -- --template react
cd my-react-app
npm install
npm run dev
```

Setelah menjalankan `npm run dev`, salin URL lokal (misalnya, `http://127.0.0.1:5173/`) dari terminal dan buka di browser.

#### 2. Membuat Fungsi Fetch di React
Buka src/App.jsx dan ubah kontennya menjadi:
```jsx
import React, { useState, useEffect } from 'react';     

function App() {
  const [apiData, setApiData] = useState(null);  
  
  // Latihan Mandiri       
  const [infoData, setInfoData] = useState(null);       

  useEffect(() => {
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => {
        setApiData(data.data);
      })
      .catch(error => console.error(error));

    // Latihan Mandiri
    fetch('http://localhost:5000/api/info')
      .then(response => response.json())
      .then(data => {
        setInfoData(data);
      })
      .catch(error => console.error(error));
  }, []);

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>React & Flask Integration</h1>
      <p>{apiData ? apiData : "Loading data..."}</p>

      // Latihan Mandiri
      <h2>Info Mahasiswa</h2>
      {infoData ? (
        <div>
          <p>Nama: {infoData.Nama}</p>
          <p>NIM: {infoData.Nim}</p>
        </div>
      ) : (
        <p>Loading info...</p>
      )}
    </div>
  );
}

export default App;
```

#### 3. Menjalankan Aplikasi React + Vite
Jalankan aplikasi React + Vite dengan perintah:

```
npm run dev
```

Pastikan terminal menampilkan informasi seperti:
```
Local: http://127.0.0.1:5173/
```

Akses aplikasi di browser menggunakan URL yang diberikan (biasanya `http://127.0.0.1:5173/`).

#### 4. Struktur Direktori React + Vite
```
frontend/
└─ my-react-app/
    ├─ src/
    │   ├─ App.jsx      # File utama React
    ├─ public/
    ├─ package.json
    ├─ vite.config.js
    └─ ...
```