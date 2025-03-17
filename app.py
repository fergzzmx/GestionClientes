om flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Ruta al directorio de clientes
CLIENTES_DIR = 'clientes'

@app.route('/')
#def index():
    # Listar los archivos de clientes
    clientes = os.listdir(CLIENTES_DIR)
    return render_template('index.html', clientes=clientes)

@app.route('/ver/<nombre_archivo>')
def ver_cliente(nombre_archivo):
    # Leer el contenido del archivo del cliente
    ruta_archivo = os.path.join(CLIENTES_DIR, nombre_archivo)
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
    return render_template('ver_cliente.html', nombre_archivo=nombre_archivo, contenido=contenido)

@app.route('/editar/<nombre_archivo>', methods=['GET', 'POST'])
def editar_cliente(nombre_archivo):
    ruta_archivo = os.path.join(CLIENTES_DIR, nombre_archivo)
    if request.method == 'POST':
        # Guardar los cambios en el archivo
        nuevo_contenido = request.form['contenido']
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(nuevo_contenido)
        return redirect(url_for('ver_cliente', nombre_archivo=nombre_archivo))
    else:
        # Mostrar el formulario de edición
        with open(ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
        return render_template('editar_cliente.html', nombre_archivo=nombre_archivo, contenido=contenido)

@app.route('/crear', methods=['GET', 'POST'])
def crear_cliente():
    if request.method == 'POST':
        # Crear un nuevo archivo de cliente
        nombre_archivo = request.form['nombre_archivo']
        contenido = request.form['contenido']
        ruta_archivo = os.path.join(CLIENTES_DIR, nombre_archivo)
        with open(ruta_archivo, 'w') as archivo:
            archivo.write(contenido)
        return redirect(url_for('index'))
    else:
        # Mostrar el formulario de creación
        return render_template('crear_cliente.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
