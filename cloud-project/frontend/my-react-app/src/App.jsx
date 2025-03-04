import React, { useState, useEffect } from 'react';     // Import React hooks

function App() {
  const [apiData, setApiData] = useState(null);         // State for API data
  const [infoData, setInfoData] = useState(null);       // State for student info

  // Fetching Data
  useEffect(() => {

    // Fetch data from endpoint '/api/data'
    fetch('http://localhost:5000/api/data')
      .then(response => response.json())
      .then(data => {
        setApiData(data.data);
      })
      .catch(error => console.error(error));

    // Fetch data from endpoint '/api/info'
    fetch('http://localhost:5000/api/info')
      .then(response => response.json())
      .then(data => {
        setInfoData(data);
      })
      .catch(error => console.error(error));
  }, []);


  // {/* Returning data from fetch */}
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>React & Flask Integration</h1>
      <p>{apiData ? apiData : "Loading data..."}</p>

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