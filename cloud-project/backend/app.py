from flask import Flask, jsonify, request    # import Flask dan jsonify to create an API
import psycopg2

# Connection to PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="test_db",
        user="student",
        password="password"
    )
    return conn


# Initialize the flask app and Enable CORS for cross-origin requests
app = Flask(__name__)

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

    items = []
    for row in rows:
        items.append({"id": row[0], "name": row[1], "description": row[2]})
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

# Endpoint PUT: Update data berdasarkan ID
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    name = data.get('name')
    description = data.get('description')

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM items WHERE id = %s;", (item_id,))
    item = cur.fetchone()

    if not item:
        cur.close()
        conn.close()
        return jsonify({"error": "Item not found"}), 404

    cur.execute("UPDATE items SET name = %s, description = %s WHERE id = %s;", (name, description, item_id))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": item_id, "name": name, "description": description})

# Endpoint DELETE: Hapus data berdasarkan ID
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM items WHERE id = %s;", (item_id,))
    item = cur.fetchone()

    if not item:
        cur.close()
        conn.close()
        return jsonify({"error": "Item not found"}), 404

    cur.execute("DELETE FROM items WHERE id = %s;", (item_id,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": f"Item {item_id} deleted successfully"})

# Run the flask server if the file executed directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)