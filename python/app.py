import flask as fk
import waitress as wt
import werkzeug.utils as wk
import mysql.connector as sql
import os
import dotenv as dt
import bcrypt as bc
import secrets as sc
import google.cloud as ai
import pandas as pd
import io
import PyPDF2
import re

#app set
dt.load_dotenv()
app = fk.Flask(__name__, static_folder='./static', template_folder='./templates')

SECRET_KEY = os.environ.get("SECRET_KEY")
app.secret_key = os.getenv("SECRET_KEY")
if "SECRET_KEY" not in os.environ:
       secret_key = sc.token_hex(32)
       os.environ["SECRET_KEY"] = secret_key
       
AICHAT = os.environ.get("GOOGLE_API_KEY")
if AICHAT is None:
    raise ValueError("aichat not set.")

#DB set
def getDBconnection():
    try:
        arpa = sql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return arpa
    except sql.Error as err:
        print('Error de conexión a la base de datos', err)
        return None

#Read pdf
def extract_text_from_pdf_stream(file_stream):
    """Extract text from PDF file stream."""
    try:
        reader = PyPDF2.PdfReader(file_stream)
        text = ''
        for page in reader.pages:
            text += page.extract_text() or ''
        return text
    except Exception as e:
        fk.current_app.logger.error(f"PDF extraction error: {e}")
        return ""

def generate_summary(text, num_sentences=3):
    """Generate simple extractive summary."""
    # Split text into sentences using basic regex
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # Remove empty or very short sentences
    sentences = [s.strip() for s in sentences if len(s.strip()) > 10]
    
    if len(sentences) <= num_sentences:
        return ' '.join(sentences)
    
    # Rank sentences by length
    ranked_sentences = sorted(
        [(sent, len(sent.split())) for sent in sentences], 
        key=lambda x: x[1], 
        reverse=True
    )
    
    # Select top sentences while maintaining original order
    summary_sentences = sorted(
        ranked_sentences[:num_sentences], 
        key=lambda x: sentences.index(x[0])
    )
    
    return ' '.join([sent for sent, _ in summary_sentences])

#Controllers set
#register
@app.route('/register', methods=['GET','POST'])
def register():
    if fk.request.method == 'POST':
        name = fk.request.form.get('nombre')
        surname = fk.request.form.get('apellido')
        ident = fk.request.form.get('cedula')
        email = fk.request.form.get('correo')
        jobTitle = fk.request.form.get('cargo')
        contrasena = fk.request.form.get('contrasena')
        confTrasena = fk.request.form.get('confTrasena')
        
        if contrasena != confTrasena:
            fk.session['error'] = "Las contraseñas no coinciden"
            return fk.redirect(fk.url_for('register'))
        
        if not all([name, surname, ident, email, jobTitle, contrasena]):
            fk.session['error'] = "Todos los campos son obligatorios"
            return fk.redirect(fk.url_for('register'))
        
        hashedPassword = bc.hashpw(contrasena.encode('utf-8'), bc.gensalt())
        
        arpa = getDBconnection()
        if arpa:
            try:
                cursor = arpa.cursor()
                sql = "INSERT INTO users (name, surname, ident, email, jobtitle, password) VALUES (%s, %s, %s, %s, %s, %s)"
                #val = (name, surname, ident, email, jobTitle, hashedPassword)
                #cursor.execute(sql, val)
                arpa.commit()
                print("Usuario registrado exitosamente")
                return fk.redirect(fk.url_for('login', registered='success')) 
            
            except sql.Error as err:
                if err.errno == 1062: 
                    
                    fk.session['error'] = "Cedula o correo ya registrado"
                else:
                    fk.session['error'] = "Error de registro", err
                return fk.redirect(fk.url_for('register'))
            
            finally:
                cursor.close()
                arpa.close()
                
        else:
            fk.session['error'] = "Error de conexión a la base de datos"
            return fk.redirect(fk.url_for('register'))

    return fk.render_template('register.html')

#login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if fk.request.method == 'POST':
        email = fk.request.form.get('usuario')
        contrasena = fk.request.form.get('contrasena')
        arpa = getDBconnection()
        if arpa:
            try:
                cursor = arpa.cursor(dictionary=True)
                mysql = "SELECT * FROM users WHERE email = %s"
                val = (email,)
                cursor.execute(mysql, val)
                user = cursor.fetchone()

                if user is None:  
                    fk.session['error'] = "Credenciales incorrectas" 
                    return fk.redirect(fk.url_for('login'))
                
                password_from_db = bytes(user['password'])
                if bc.checkpw(contrasena.encode('utf-8'), password_from_db):
                    fk.session['user_id'] = user['id']
                    fk.session['user_email'] = user['email']  
                    return fk.redirect(fk.url_for('dashboard'))
                else:
                    fk.session['error'] = "Credenciales incorrectas" 
                    return fk.redirect(fk.url_for('login'))

            except Exception as err: 
                print(err)
                fk.session['error'] = "Error during login"
                return fk.redirect(fk.url_for('login'))

            finally:
                cursor.close()
                arpa.close()
        else:
            fk.session['error'] = "Error de conexión a la base de datos"
            return fk.redirect(fk.url_for('login'))

    return fk.render_template('login.html')

@app.route('/dashboard')
def dashboard():

    if 'user_id' in fk.session: 
      return fk.render_template('dashboard.html')
    else:
        return fk.redirect(fk.url_for('login'))

@app.route('/persons')
def persons():
    if 'user_id' in fk.session:
       return fk.render_template('persons.html')
    else:
       return fk.redirect(fk.url_for('login'))

@app.route('/audits')
def audits():
    if 'user_id' in fk.session:
       return fk.render_template('audits.html')
    else:
       return fk.redirect(fk.url_for('login'))
   
@app.route('/reports')
def reports():
    if 'user_id' in fk.session:
       return fk.render_template('reports.html')
    else:
       return fk.redirect(fk.url_for('login'))

@app.route('/alerts')
def alerts():
    if 'user_id' in fk.session:
       return fk.render_template('alerts.html')
    else:
       return fk.redirect(fk.url_for('login'))

@app.route('/readFiles')
def readFiles():
    if 'user_id' in fk.session:
       return fk.render_template('readFiles.html')
    else:
       return fk.redirect(fk.url_for('login'))

@app.route('/filesData')
def filesData():
    if 'user_id' in fk.session:
       return fk.render_template('filesData.html')
    else:
       return fk.redirect(fk.url_for('login'))
        

@app.route('/upload', methods=['GET', 'POST'])
def uploadExcel():
    if fk.request.method == 'POST':
        
        if 'file' not in fk.request.files:
            return fk.render_template('uploadExcel.html', error='Carga un archivo')
        
        file = fk.request.files['file']
        
        if file.filename == '':
            return fk.render_template('uploadExcel.html', error='Selecciona un archivo')
        
        if not file.filename.lower().endswith(('.xls', '.xlsx', '.xlsm', '.xlsb')):
            return fk.render_template('uploadExcel.html', error='Archivo invalido')
        
        try:
            df = pd.read_excel(file)

            stats = {
                'filename': file.filename,
                'total_rows': len(df),
                'total_value': df.iloc[:, -1].sum(),
                'average_value': df.iloc[:, -1].mean(),
                'null_values': df.isnull().sum().sum()
            }
            
            return fk.render_template('results.html', 
                                   stats=stats, 
                                   data=df.to_dict('records'), 
                                   columns=df.columns.tolist())
        
        except Exception as e:
            return fk.render_template('uploadExcel.html', error=str(e))
    
    return fk.render_template('uploadExcel.html')

@app.route('/uploadPDF', methods=['GET', 'POST'])
def uploadPDF():
    
    if fk.request.method == 'GET':
        return fk.render_template('uploadPDF.html')
    
    if 'file' not in fk.request.files:
        return fk.render_template('uploadPDF.html', error='No file part')
    
    file = fk.request.files['file']
    
    if file.filename == '':
        return fk.render_template('uploadPDF.html', error='No selected file')
    
    if not file.filename.lower().endswith('.pdf'):
        return fk.render_template('uploadPDF.html', error='Invalid file type. Please upload a PDF.')
    
    try:
        file_stream = io.BytesIO(file.read())

        extracted_text = extract_text_from_pdf_stream(file_stream)
        
        if not extracted_text:
            return fk.render_template('uploadPDF.html', error='Could not extract text from PDF')

        summary = generate_summary(extracted_text)
        
        return fk.render_template('PDFresults.html', summary=summary)
    
    except Exception as e:
        fk.current_app.logger.error(f"PDF processing error: {e}")
        return fk.render_template('uploadPDF.html', error='An unexpected error occurred')
   
@app.route('/goods')
def goods():
    if 'user_id' in fk.session:
       return fk.render_template('goods.html')
    else:
       return fk.redirect(fk.url_for('login'))

@app.route('/chat')
def chat():
    if 'user_id' in fk.session:
       return fk.render_template('chat.html')
    else:
       return fk.redirect(fk.url_for('login'))
   
@app.route("/aichat", methods=["POST"])
def aichat():
    user_message = fk.request.form.get("user_message")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {AICHAT}" 
    }

    request_body = {
        "queryInput": {
            "text": {
                "text": user_message
            }
        }
    }

    try:
        response = fk.requests.post(AICHAT, headers=headers, json=request_body)
        response.raise_for_status()  
        response_json = response.json()
        bot_message = response_json["queryResult"]["fulfillmentText"] 

    except fk.requests.exceptions.RequestException as e:
        print(f"Error with Gemini API: {e}")
        bot_message = "I'm having trouble right now. Please try again later."


    messages = fk.session.get('messages', [])
    messages.append({"role": "user", "content": user_message})
    messages.append({"role": "assistant", "content": bot_message})
    fk.session['messages'] = messages

    return fk.jsonify({"messages": messages[-2:]})

@app.route('/logout')
def logout():
    fk.session.pop('user_id', None)  
    fk.session.pop('user_email', None)
    return fk.redirect(fk.url_for('login'))

@app.route('/')
def index():
    return fk.redirect(fk.url_for('login'))

if __name__ == '__main__':
    wt.serve(app, host='0.0.0.0', port=7070)




