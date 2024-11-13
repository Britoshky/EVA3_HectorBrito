# app/routes.py
from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    result = None
    if request.method == 'POST':
        try:
            # Recoger y convertir las notas y la asistencia
            nota1 = int(request.form.get('nota1'))
            nota2 = int(request.form.get('nota2'))
            nota3 = int(request.form.get('nota3'))
            asistencia = int(request.form.get('asistencia'))

            # Calcular el promedio
            promedio = (nota1 + nota2 + nota3) / 3

            # Determinar el estado (aprobado o reprobado)
            if promedio >= 40 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

            # Pasar el resultado al template
            result = {
                'promedio': round(promedio, 2),
                'estado': estado
            }

        except ValueError:
            result = {
                'error': 'Por favor ingresa valores válidos para las notas y la asistencia.'
            }

    return render_template('ejercicio1.html', result=result)

@main.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    result = None
    if request.method == 'POST':
        # Recoger los nombres del formulario
        nombre1 = request.form.get('nombre1')
        nombre2 = request.form.get('nombre2')
        nombre3 = request.form.get('nombre3')

        # Encontrar el nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

        # Pasar el resultado al template
        result = {
            'nombre_mas_largo': nombre_mas_largo,
            'longitud': longitud
        }

    return render_template('ejercicio2.html', result=result)
