# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from database.db import get_db_connection, create_tables
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default-secret-key')

# Create tables on startup
create_tables()

# Login required decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Routes
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('usuario')
        password = request.form.get('contrasena')
        
        connection = get_db_connection()
        if connection is None:
            flash('Database connection error')
            return redirect(url_for('login'))
        
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE correo = %s", (correo,))
            user = cursor.fetchone()
            
            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['id']
                session['user_email'] = user['correo']
                return redirect(url_for('dashboard'))
            
            flash('Invalid credentials')
            return redirect(url_for('login'))
            
        except Error as e:
            flash('Login error')
            return redirect(url_for('login'))
        finally:
            cursor.close()
            connection.close()
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        cedula = request.form.get('cedula')
        correo = request.form.get('correo')
        cargo = request.form.get('cargo')
        password = request.form.get('contrasena')
        confirm_password = request.form.get('confTrasena')
        
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('register'))
        
        connection = get_db_connection()
        if connection is None:
            flash('Database connection error')
            return redirect(url_for('register'))
        
        try:
            cursor = connection.cursor(dictionary=True)
            
            # Check if email exists
            cursor.execute("SELECT id FROM users WHERE correo = %s", (correo,))
            if cursor.fetchone():
                flash('Email already registered')
                return redirect(url_for('register'))
            
            # Check if cedula exists
            cursor.execute("SELECT id FROM users WHERE cedula = %s", (cedula,))
            if cursor.fetchone():
                flash('Cedula already registered')
                return redirect(url_for('register'))
            
            # Insert new user
            hashed_password = generate_password_hash(password)
            cursor.execute("""
                INSERT INTO users (nombre, apellido, cedula, correo, cargo, password)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (nombre, apellido, cedula, correo, cargo, hashed_password))
            
            connection.commit()
            flash('Registration successful')
            return redirect(url_for('login'))
            
        except Error as e:
            connection.rollback()
            flash('Registration failed')
            return redirect(url_for('register'))
        finally:
            cursor.close()
            connection.close()
    
    return render_template('register.html')

@app.route('/dashboard')
@login_required
def dashboard():
    connection = get_db_connection()
    if connection is None:
        return redirect(url_for('login'))
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (session['user_id'],))
        user = cursor.fetchone()
        return render_template('dashboard.html', user=user)
    finally:
        cursor.close()
        connection.close()

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)