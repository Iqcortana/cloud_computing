from flask import Flask, jsonify  # Mengimpor Flask untuk membuat aplikasi web dan jsonify untuk mengembalikan data dalam format JSON
from flask_cors import CORS  # Mengimpor CORS untuk mengizinkan akses lintas domain (Cross-Origin Resource Sharing)

app = Flask(__name__)  # Membuat instance aplikasi Flask
CORS(app)  # Mengaktifkan CORS agar API bisa diakses dari frontend React

@app.route('/')  # Menentukan rute untuk URL root ('/')
def home():
    return jsonify({"message": "Hello from Flask!"})  # Mengembalikan respons dalam format JSON dengan pesan sederhana

@app.route('/api/data')  # Menentukan rute untuk endpoint '/api/data'
def get_data():
    return jsonify({"data": "Hello from Flask API"})  # Mengembalikan JSON berisi data contoh

if __name__ == '__main__':  # Memastikan bahwa server hanya berjalan jika file ini dieksekusi langsung
    app.run(debug=True, host='0.0.0.0', port=5000)  
    # Menjalankan server Flask pada port 5000
    # debug=True: Mengaktifkan mode debug untuk melihat error secara langsung dan otomatis reload saat ada perubahan
    # host='0.0.0.0': Membuat server bisa diakses dari jaringan lokal
