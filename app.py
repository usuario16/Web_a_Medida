from flask import (Flask, render_template, redirect, request, url_for)
import mysql.connector

app = Flask(__name__)

# Funcion que introduce datos a la BBDD
def data_to_db(d1, d2):
    conection_db = mysql.connector.connect(
        host='localhost',
        user='usuario16',
        password='2866049diego',
        database='sitioweb'
    )

    cursor = conection_db.cursor(dictionary=True)

    cursor.execute(
        """
        INSERT INTO consultas (correo, consulta)
        VALUES (%s, %s);
        """,
        (d1, d2)
    )
    conection_db.commit()
    conection_db.close()
    print('Datos ingresados con exito en la base de datos!')


# Vista de inicio
@app.route('/')
def inicio():
    return render_template('index.html')


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