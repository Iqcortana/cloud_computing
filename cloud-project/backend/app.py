from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
  return jsonify({"message": "Hello from Flask!"})

# Endpoint tambahan:
# @app.route('/about')
# def about():
#   return jsonify({
#       "nama" : "Ilham",
#       "nim" : "10221081",
#       "instansi" : "Institut Teknologi Kalimantan",
#       "program studi" : "Sistem"
#   })

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)