<?php
require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/src/Auth.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

try {
    $pdo = new PDO("mysql:host=" . $_ENV['DB_HOST'] . ";dbname=" . $_ENV['DB_NAME'], $_ENV['DB_USER'], $_ENV['DB_PASSWORD']);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage()); 
}

$auth = new Auth($pdo);
session_start();

$requestUri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

switch ($requestUri) {
    case '/register':
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            
            $nombre = $_POST['nombre'];
            $apellido = $_POST['apellido'];
            $cedula = $_POST['cedula'];
            $correo = $_POST['correo'];
            $cargo = $_POST['cargo'];
            $contrasena = $_POST['contrasena'];
            $confTrasena = $_POST['confTrasena'];

            if ($auth->register($nombre, $apellido, $cedula, $correo, $cargo, $contrasena, $confTrasena)) {
                header("Location: /login?registered=success"); 
                exit;
            } else {
                $_SESSION['error'] = "Registration failed."; 
                header("Location: /register"); 
                exit;
            }
        } else {
            include __DIR__ . '/views/register.php';
        }
        break;


    case '/login':
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            
            $username = $_POST['username'];  
            $password = $_POST['password'];
            if ($auth->login($username, $password)) {
                header("Location: /dashboard"); 
                exit;
            } else {
                $_SESSION['error'] = "Login failed."; 
                header("Location: /login");
                exit;
            }
        } else {
            include __DIR__ . '/views/login.php'; 
        }
        break;

    default:
        header("Location: /login"); 
        exit;
}
?>