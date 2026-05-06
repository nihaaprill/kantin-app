from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

film_data = {
    "nama_film": "Daftar Film Favorit",
    "film": ["Avengers", "Interstellar", "Inception"]
}

@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify(film_data)

@app.route('/api/add-film', methods=['POST'])
def add_film():
    item_baru = request.json.get('item')
    if item_baru:
        film_data["film"].append(item_baru)
        return jsonify({
            "message": "Film berhasil ditambah!",
            "film": film_data["film"]
        }), 201
    return jsonify({"error": "Data tidak valid"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)