// import React, { useState, useEffect } from 'react'; // Mengimpor React dan hooks useState, useEffect

// function App() {
//   // Mendefinisikan state apiData untuk menyimpan data dari API
//   const [apiData, setApiData] = useState(null);

//   // useEffect digunakan untuk melakukan fetch data saat komponen pertama kali dirender
//   useEffect(() => {
//     fetch('http://localhost:5000/api/data') // Mengambil data dari API Flask di localhost:5000
//       .then(response => response.json()) // Mengonversi respons ke format JSON
//       .then(data => {
//         setApiData(data.data); // Menyimpan data dari respons ke state apiData
//       })
//       .catch(error => console.error(error)); // Menangani error jika request gagal
//   }, []); // Dependency array kosong menandakan useEffect hanya dijalankan sekali saat komponen dimount

//   return (
//     <div style={{ textAlign: 'center', marginTop: '50px' }}> {/* Menata tampilan dengan style inline */}
//       <h1>React & Flask Integration</h1> {/* Judul aplikasi */}
//       <p>{apiData ? apiData : "Loading data..."}</p> {/* Menampilkan data atau pesan "Loading data..." jika masih fetching */}
//     </div>
//   );
// }

import { useState, useEffect } from "react";

function App() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:5000/api/items")
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