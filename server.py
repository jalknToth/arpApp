import flask as fk 
import os
import pandas as pd
from excelReader import process_excel

# Crea una instancia de la aplicación Flask
app = fk.Flask(__name__)
# Configura la carpeta para subir archivos
app.config['UPLOAD_FOLDER'] = 'uploads'
# Define las extensiones de archivo permitidas
app.config['ALLOWED_EXTENSIONS'] = {'xlsx', 'xls'}

def allowed_file(filename):
    # Comprueba si la extensión del archivo está permitida
    # filename.rsplit('.', 1)[1].lower() obtiene la extensión en minúsculas
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route("/", methods=["GET", "POST"])
def index():
    # Maneja las solicitudes GET y POST a la ruta raíz
    if fk.request.method == 'POST': # Si la solicitud es POST (se ha enviado un formulario)
        # Verifica si se ha subido un archivo
        if 'file' not in fk.request.files:
            # Redirige a la página de error si no hay archivo
            return fk.redirect(fk.rurl_for('error', msg='No se ha subido ningún archivo')) # Redirige a la página de error si no se proporciona un archivo
        file = fk.request.files['file'] # Obtiene el archivo subido
        # Verifica si se ha seleccionado un archivo
        if file.filename == '':
            # Redirige a la página de error si no se ha seleccionado un archivo
            return fk.redirect(fk.rurl_for('error', msg='No se ha seleccionado ningún archivo'))  # Redirige a la página de error si no se selecciona un archivo
        # Verifica si el archivo es válido
        if file and allowed_file(file.filename):  # Si se ha subido un archivo y su extensión es permitida
            filename = file.filename  # Obtiene el nombre del archivo
            # Crea la ruta completa para guardar el archivo
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)  # Crea la ruta donde se guardará el archivo
            file.save(filepath)  # Guarda el archivo subido  # Guarda el archivo en el servidor

            try:
                # Procesa el archivo Excel
                df = process_excel(filepath) # Procesa el archivo Excel usando la función process_excel (definida en excelReader.py)
                # Renderiza la plantilla 'excelData.html' con los datos del archivo Excel
                return fk.render_template('excelData.html', tables=[df.to_html(classes='data')], titles=df.columns.values)  # Renderiza la plantilla y muestra los datos

            except Exception as e: # Captura cualquier excepción durante el procesamiento
                # Redirige a la página de error si ocurre un error durante el procesamiento
                return fk.redirect(fk.rurl_for('error', msg=f'Error al procesar el archivo: {str(e)}')) # Redirige a la página de error si hay un error al procesar el archivo
        else: # Si el tipo de archivo no es válido
            # Redirige a la página de error si el tipo de archivo no es válido
            return fk.redirect(fk.rurl_for('error', msg='Tipo de archivo no válido')) # Redirige a la página de error si el tipo de archivo no es válido

    return fk.render_template('index.html') # Renderiza la plantilla index.html si la solicitud es GET


@app.route('/uploads/<filename>') # Define la ruta para servir archivos estáticos desde la carpeta 'uploads'
def uploaded_file(filename):
    # Sirve el archivo subido desde la carpeta 'uploads'
    return fk.send_from_directory(app.config['UPLOAD_FOLDER'], filename)  # Envía el archivo solicitado al usuario


@app.route('/error/<msg>')  # Define la ruta para mostrar mensajes de error
def error(msg):
    # Renderiza la plantilla 'error.html' con el mensaje de error
    return fk.render_template('error.html', msg=msg)  # Renderiza la plantilla de error con el mensaje correspondiente


if __name__ == '__main__':
    # Ejecuta la aplicación en modo debug
    app.run(debug=True) # Inicia la aplicación Flask en modo debug