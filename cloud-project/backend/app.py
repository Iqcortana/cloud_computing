from flask import Flask, jsonify    # import Flask dan jsonify to create an API
from flask_cors import CORS         # import CORS to allow frontend access

# Initialize the flask app and Enable CORS for cross-origin requests
app = Flask(__name__)
CORS(app)

# Main endpoint 
@app.route('/')
def home():
  return jsonify({"message": "Hello from Flask!"})

# API data endpoint
@app.route('/api/data')
def get_data():
  return jsonify({"data": "Hello from Flask API"})

# Student Information endpoint
@app.route('/api/info')
def info():
  return jsonify({
    "Nama": "Taufik Ilham",
    "Nim": "10221081"
    })

# Run the flask server if the file executed directly
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)