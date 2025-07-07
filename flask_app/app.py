import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, render_template, request, redirect, url_for
from herramientas import listar_herramientas, agregar_herramienta
from retiros import registrar_retiro
from devoluciones import devolver_herramienta
from herramientas import obtener_herramientas
from responsables import obtener_responsables

app = Flask(__name__, template_folder='templates')

@app.route('/')
def inicio():
    herramientas = listar_herramientas()
    return render_template('index.html', herramientas=herramientas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cantidad = int(request.form['cantidad'])
        ubicacion = request.form['ubicacion']
        descripcion = request.form['descripcion']
        agregar_herramienta(nombre, cantidad, ubicacion, descripcion)
        return redirect(url_for('inicio'))
    return render_template('agregar.html')

@app.route('/retirar', methods=['GET', 'POST'])
def retirar():
    if request.method == 'POST':
        herramienta_id = int(request.form['herramienta_id'])
        responsable_id = int(request.form['responsable_id'])
        cantidad = int(request.form['cantidad'])
        observaciones = request.form.get('observaciones', '')
        registrar_retiro(herramienta_id, responsable_id, cantidad, observaciones)
        return redirect(url_for('inicio'))

    herramientas = obtener_herramientas()
    responsables = obtener_responsables()
    return render_template('retirar.html', herramientas=herramientas, responsables=responsables)

@app.route('/devolver', methods=['GET', 'POST'])
def devolver():
    if request.method == 'POST':
        id_herramienta = int(request.form['herramienta_id'])
        cantidad = int(request.form['cantidad'])
        devolver_herramienta(id_herramienta, cantidad)
        return redirect(url_for('inicio'))
    return render_template('devolver.html')

if __name__ == '__main__':
    app.run(debug=True)
