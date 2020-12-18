from flask import (Flask, render_template, redirect, request, url_for)
import sqlite3
from datetime import datetime


app = Flask(__name__)

# Funcion que introduce datos a la BBDD
def data_to_db(d1, d2):
    cursor = sqlite3.connect('consultas.db')
    cursor.execute(
        """
        INSERT INTO consultas (correo, consulta)
        VALUES (?, ?);
        """,
        (d1, d2)
    )
    cursor.commit()
    cursor.close()
    print('Datos ingresados con exito en la base de datos!')


# Vista de inicio
@app.route('/')
def inicio():
    return render_template('inicio.html')


# Vista de la pagina de servicio
@app.route('/servicio')
def servicio():
    return render_template('servicio.html')


# Vista de consultas y recibo de estas
@app.route('/consultas', methods=['POST', 'GET'])
def consultas():
    if request.method == 'POST':
        correo = request.form['correo']
        consulta = request.form['consulta']
        print(correo, consulta)
        data_to_db(correo, consulta)

        return redirect(url_for('inicio'))
    
    return render_template('consultas.html')

# Vista de contacto
@app.route('/contacto')
def contacto():    
    return render_template('contacto.html')