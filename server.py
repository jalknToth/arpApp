from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from werkzeug.utils import secure_filename
import os
import pandas as pd
import sql.connector  # Assuming you have a sql_connector.py for database interaction
import hashlib  # For password hashing
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")  # Get secret key from .env
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Database functions (in sql_connector.py, adjust as needed)
def get_db_connection():
    # ... your database connection logic ...
    pass

def register_user(username, password):
    # ... your user registration logic (hash password!)...
    pass

def login_user(username, password):
    # ... your user login logic (verify hashed password!)...
    pass

def get_audit_data():
    # ... your logic to fetch audit data from the database ...
    pass

# Route handling
@app.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:  # Check if the user is logged in
        return redirect(url_for('dashboard'))  # Redirect to dashboard if logged in
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest() # Hash password
        if login_user(username, hashed_password):  # Pass hashed password!
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password.')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if register_user(username, hashed_password):
            flash('Registration successful. Please log in.')
            return redirect(url_for('login'))
        else:
            flash('Registration failed. Username might already exist.')
    return render_template('register.html')

@app.route('/recover')
def recover():
    return render_template('recover.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login')) # Redirect to login if not logged in
    audit_data = get_audit_data()
    return render_template('dashboard.html', audit_data=audit_data)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            file.save(filepath)
            try:
                excel_data = pd.read_excel(filepath)  # Process Excel with pandas
                # .... Your logic to save data to database .... 

                return redirect(url_for('excel_data', filename=filename))
            except Exception as e:
                flash(f"Error processing Excel file: {e}")


    return render_template('excelData.html')  # Render upload form

@app.route('/uploads/<filename>')
def excel_data(filename):
    if 'username' not in session:
        return redirect(url_for('login'))
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)