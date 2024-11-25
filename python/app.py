import flask as fk
import waitress as wt
import mysql.connector as sql
import os
import dotenv as dt
import bcrypt as bc

#App config.
dt.load_dotenv()

app = fk.Flask(
    __name__, static_folder='./static',
    template_folder='./templates')

app.secretKey = os.getenv("SECRET_KEY")

#DB config.
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

#Controllers config.
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
                val = (name, surname, ident, email, jobTitle, hashedPassword)
                cursor.execute(sql, val)
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
#auth = fk.Blueprint('auth', __name__)
@app.route('/login', methods=['GET','POST'])
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
                user = cursor.fetchone()
                
                if user and bc.checkpw(contrasena.encode('utf-8'), user['password']):
                    fk.session['user_id'] = user['id']
                    fk.session['user_email'] = user['correo'] 
                    return fk.redirect(fk.url_for('dashboard'))
                
                else:
                    fk.session['error'] = "Credenciales incorrectas"
                    return fk.redirect(fk.url_for('login'))  
                
            except mysql.connector.Error as err:
                print(err)
                fk.session['error'] = "Error during login"
                return fk.redirect(fk.url_for('login'))
            
            finally:
                cursor.close()
                arpa.close()
        else:
             fk.session['error'] = "Error de conexión a la base de datos"
             return fk.redirect(fk.url_for('login')) # redirect back to login with message


    return fk.render_template('login.html')

#app.register_blueprint(auth)

@app.route('/dashboard')
def dashboard():

    if 'user_id' in fk.session: 
      return fk.render_template('dashboard.html')
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

