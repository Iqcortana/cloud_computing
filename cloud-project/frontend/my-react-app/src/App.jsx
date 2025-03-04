import React, { useState, useEffect } from 'react'; // Mengimpor React dan hooks useState, useEffect

function App() {
  // Mendefinisikan state apiData untuk menyimpan data dari API
  const [apiData, setApiData] = useState(null);

  // useEffect digunakan untuk melakukan fetch data saat komponen pertama kali dirender
  useEffect(() => {
    fetch('http://localhost:5000/api/data') // Mengambil data dari API Flask di localhost:5000
      .then(response => response.json()) // Mengonversi respons ke format JSON
      .then(data => {
        setApiData(data.data); // Menyimpan data dari respons ke state apiData
      })
      .catch(error => console.error(error)); // Menangani error jika request gagal
  }, []); // Dependency array kosong menandakan useEffect hanya dijalankan sekali saat komponen dimount

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}> {/* Menata tampilan dengan style inline */}
      <h1>React & Flask Integration</h1> {/* Judul aplikasi */}
      <p>{apiData ? apiData : "Loading data..."}</p> {/* Menampilkan data atau pesan "Loading data..." jika masih fetching */}
    </div>
  );
}

export default App; // Mengekspor komponen App agar bisa digunakan di file lain
