# Dokumentasi Singkat

## Full Stack Project with Docker Compose

### 📄 Deskripsi Singkat

Proyek ini mengintegrasikan aplikasi Flask (Backend), React (Frontend), dan PostgreSQL (Database) menggunakan Docker Compose untuk mempermudah orkestrasi layanan dalam satu lingkungan pengembangan.

### 🎯 Tujuan Pembelajaran
- Menggunakan docker-compose.yml untuk mengelola multi-container aplikasi.
- Menghubungkan React dan Flask serta memastikan data tersimpan dalam PostgreSQL.
- Menggunakan environment variables untuk konfigurasi koneksi database.


### 🛠 Persyaratan Sistem
Sebelum memulai, pastikan sistem Anda memiliki:
- Python 3.x terinstal
- PostgreSQL terinstal dan dikonfigurasi
- Node.js terinstal untuk pengembangan frontend React
- Docker dan Docker Desktop terinstal dan berjalan
- Virtual Environment Python

### 🛠️ Struktur Proyek
```
cloud-project/
│── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│── frontend/
│   ├── my-react-app/
│   │   ├── src/
│   │   │   ├── App.jsx
│   |   ├── Dockerfile
│── init.sql
│── docker-compose.yml
```

### Langkah-Langkah Implementasi

#### 1️⃣ Membuat docker-compose.yml
Buat file docker-compose.yml di root proyek

```yml
version: '3.7'
services:
  backend:
    build: 
      context: ./backend
    container_name: flask_container
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      - DB_HOST=db
      - DB_NAME=test_db
      - DB_USER=student
      - DB_PASSWORD=password

  frontend:
    build:
      context: ./frontend/my-react-app
    container_name: react_container
    ports:
      - "3000:80"
    depends_on:
      - backend

  db:
    image: postgres:12-alpine
    container_name: postgres_container
    environment:
      - POSTGRES_DB=test_db
      - POSTGRES_USER=student
      - POSTGRES_PASSWORD=password
    ports:
      - "5432:5432"
    volumes:
      - db_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  db_data:
```

#### 2️⃣ Membuat init.sql untuk Database

Tambahkan file init.sql dengan isi berikut untuk membuat tabel awal:

```sql
CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

INSERT INTO items (name, description) VALUES
('Test Item', 'This is a test description'),
('Test Item 2', 'This is a test description 2');
```

#### 3️⃣ Menyesuaikan Backend 

Sesuaikan `backend\app.py` dengan code dibawah ini :

```py
from flask import Flask, jsonify, request  # Import Flask untuk membuat API, jsonify untuk mengembalikan data dalam format JSON, dan request untuk menerima data dari client
from flask_cors import CORS  # Import CORS untuk mengizinkan akses lintas sumber (Cross-Origin Resource Sharing)
import psycopg2  # Import psycopg2 untuk berinteraksi dengan database PostgreSQL
import os  # Import os untuk membaca environment variables

# Koneksi ke database PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "localhost"),
        database=os.environ.get("DB_NAME", "test_db"),
        user=os.environ.get("DB_USER", "student"),
        password=os.environ.get("DB_PASSWORD", "password")
    )
    return conn


# Inisialisasi Flask app
app = Flask(__name__)
CORS(app) # Mengaktifkan CORS agar API bisa diakses dari domain yang berbeda (misalnya React di port 3000) 

# Main endpoint 
@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask!"})

# Endpoint untuk membaca data ke tabel 'items'
@app.route('/api/items', methods=['GET'])
def get_items():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, description FROM items;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    items = [{"id": row[0], "name": row[1], "description": row[2]} for row in rows]
    return jsonify(items)

# Endpoint untuk menambahkan data ke tabel 'items'
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.json
    name = data['name']
    description = data['description']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO items (name, description) VALUES (%s, %s) RETURNING id;", (name, description))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": new_id, "name": name, "description": description}), 201

# Menjalankan server Flask jika file ini dieksekusi langsung
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

#### 4️⃣ Menyesuaikan Frontend (App.jsx)

```jsx
import { useState, useEffect } from "react";

function App() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/items")
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setItems(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading data...</div>;
  }

  return (
    <div>
      <h1>React & Flask Integration</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>
            <strong>{item.name}</strong>: {item.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

#### 5️⃣ Menjalankan Docker Compose

Jalankan perintah berikut untuk membangun ulang image dan menjalankan semua container:

```
docker compose up -d --build
```

Untuk melihat log:

```
docker compose logs -f
```


#### 6️⃣ Verifikasi Integrasi

- Buka http://localhost:3000 untuk melihat UI React.
- Backend (Flask) bisa dicek di http://localhost:5000/api/items.
- Pastikan React dapat mengambil data dari Flask dan Flask dapat menyimpan data ke PostgreSQL.

### ✅ Kesimpulan
Proyek ini telah mengintegrasikan Flask, React, dan PostgreSQL menggunakan Docker Compose. Dengan pendekatan ini, semua layanan dapat dikelola secara lebih efisien dalam satu lingkungan pengembangan. 🚀