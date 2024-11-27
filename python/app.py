import flask as fk
import waitress as wt
import mysql.connector as sql
import os
import dotenv as dt
import bcrypt as bc
import secrets as sc

#app set
dt.load_dotenv()
app = fk.Flask(__name__, static_folder='./static', template_folder='./templates')

SECRET_KEY = os.environ.get("SECRET_KEY")

app.secret_key = os.getenv("SECRET_KEY")
if "SECRET_KEY" not in os.environ:
       secret_key = sc.token_hex(32)
       os.environ["SECRET_KEY"] = secret_key

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
   
@app.route('/chat')
def chat():
    if 'user_id' in fk.session:
       return fk.render_template('chat.html')
    else:
       return fk.redirect(fk.url_for('login'))
   
@app.route('/filesData')
def filesData():
    if 'user_id' in fk.session:
       return fk.render_template('filesData.html')
    else:
       return fk.redirect(fk.url_for('login'))
   
@app.route('/goods')
def goods():
    if 'user_id' in fk.session:
       return fk.render_template('goods.html')
    else:
       return fk.redirect(fk.url_for('login'))

@app.route('/logout')
def logout():
    fk.session.pop('user_id', None)  
    fk.session.pop('user_email', None)
    return fk.redirect(fk.url_for('login'))

@app.route('/')
def index():
    return fk.redirect(fk.url_for('login'))

if __name__ == '__main__':
    wt.serve(app, host='0.0.0.0', port=8080)

