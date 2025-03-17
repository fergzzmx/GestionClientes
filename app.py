from flask import Flask, jsonify

app = Flask(__name__)

# Datos de ejemplo de clientes
clientes = [
    {"id": 1, "nombre": "Juan Pérez", "email": "juan@example.com"},
    {"id": 2, "nombre": "Ana Gómez", "email": "ana@example.com"}
]

@app.route('/')
def inicio():
    return "Bienvenido a la aplicación de gestión de clientes."

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    return jsonify(clientes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
