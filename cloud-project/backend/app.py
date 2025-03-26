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