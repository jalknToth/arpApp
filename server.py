from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import mysql.connector
import os
import pandas as pd
from werkzeug.utils import secure_filename
import excelReader  # Assuming you have a module for Excel processing

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for flash messages

# Load database credentials from .env file
import os
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_DATABASE = os.getenv("DB_DATABASE")

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}  # Allowed file extensions
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1000 * 1000 # 16MB upload limit


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    try:
        cnx = mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)
        return cnx
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None



@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # ... (Handle registration logic, insert user data into the database) ...
        return redirect(url_for("login")) # Redirect to login after registration
    return render_template("register.html")


@app.route("/recover", methods=["GET", "POST"])
def recover():
    # ... Password recovery logic ...
    return render_template("recover.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'] 
        cnx = get_db_connection()
        if cnx:
            cursor = cnx.cursor()
            query = "SELECT * FROM users WHERE username = %s AND password = %s"  # Vulnerable to SQL injection! Fix below
            cursor.execute(query, (username, password)) # Use parameterized query
            user = cursor.fetchone()
            cursor.close()
            cnx.close()
            if user:
                # Successful login
                return redirect(url_for('dashboard'))  # Redirect to dashboard or protected area
            else:
                flash("Invalid username or password. Please try again.", "danger") #Flash message (requires secret key set in app config)
    return render_template('login.html')



@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
     if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename) # Sanitize filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # Save file
            # Process the Excel file (using pandas or your excelReader module)
            try:
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                df = pd.read_excel(filepath)  # Read the Excel file using pandas
                data = df.to_html() # Convert DataFrame to HTML
                # ... further processing (e.g., store data in DB) ...
                return render_template('excelData.html', table_data=data, filename=filename)

            except Exception as e: # Catch potential errors during file processing
                flash(f'Error processing file: {e}', 'danger')



     return render_template("dashboard.html") # Render dashboard on GET request






@app.route('/uploads/<filename>') # Make uploaded file available for download
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run(debug=True)