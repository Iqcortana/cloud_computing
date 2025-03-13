import psycopg2
from flask import Flask, jsonify, request  # Mengimpor Flask untuk membuat aplikasi web dan jsonify untuk mengembalikan data dalam format JSON
from flask_cors import CORS  # Mengimpor CORS untuk mengizinkan akses lintas domain (Cross-Origin Resource Sharing)

# Tambahkan di bagian atas file sebelum deklarasi route
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="test_db",
        user="student",
        password="password"
    )
    return conn

app = Flask(__name__)  # Membuat instance aplikasi Flask
CORS(app)  # Mengaktifkan CORS agar API bisa diakses dari frontend React

@app.route('/')  # Menentukan rute untuk URL root ('/')
def home():
    return jsonify({"message": "Hello from Flask!"})  # Mengembalikan respons dalam format JSON dengan pesan sederhana

@app.route('/api/data')  # Menentukan rute untuk endpoint '/api/data'
def get_data():
    return jsonify({"data": "Hello from Flask API"})  # Mengembalikan JSON berisi data contoh

# Endpoint untuk membaca data dari tabel 'items'
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

if __name__ == '__main__':  # Memastikan bahwa server hanya berjalan jika file ini dieksekusi langsung
    app.run(debug=True, host='0.0.0.0', port=5000)  
    # Menjalankan server Flask pada port 5000
    # debug=True: Mengaktifkan mode debug untuk melihat error secara langsung dan otomatis reload saat ada perubahan
    # host='0.0.0.0': Membuat server bisa diakses dari jaringan lokal
