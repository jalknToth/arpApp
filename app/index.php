<?php 
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/src/Auth.php';

// Load .env variables
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

// Database connection (try/catch remains the same)
try {
    $pdo = new PDO("mysql:host=" . $_ENV['DB_HOST'] . ";dbname=" . $_ENV['DB_NAME'], $_ENV['DB_USER'], $_ENV['DB_PASSWORD']);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage()); 
}

$auth = new Auth($pdo);

session_start(); // Start the session ONCE at the beginning

// Routing (improved with switch)
$requestUri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

switch ($requestUri) {
    case '/register':
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            // ... registration logic (same as before)
            $nombre = $_POST['nombre'];
            $apellido = $_POST['apellido'];
            $cedula = $_POST['cedula'];
            $correo = $_POST['correo'];
            $cargo = $_POST['cargo'];
            $contrasena = $_POST['contrasena'];
            $confTrasena = $_POST['confTrasena'];

            if ($auth->register($nombre, $apellido, $cedula, $correo, $cargo, $contrasena, $confTrasena)) {
                header("Location: /login?registered=success"); // Add success message
                exit;
            } else {
                $_SESSION['error'] = "Registration failed.";  // Store error message in session
                header("Location: /register"); // Redirect back to registration page
                exit;
            }
        } else {
            include __DIR__ . '/views/register.php';
        }
        break;


    case '/login':
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            // ... login logic (corrected username/password check) ...
            $username = $_POST['username'];  // Use 'username' from the form
            $password = $_POST['password'];
            if ($auth->login($username, $password)) {
                header("Location: /dashboard"); 
                exit;
            } else {
                $_SESSION['error'] = "Login failed."; // Store error message in session
                header("Location: /login");
                exit;
            }
        } else {
            include __DIR__ . '/views/login.php'; 
        }
        break;


    case '/logout':
        $auth->logout();
        header("Location: /login"); 
        exit;
        break;

    case '/dashboard':
        if ($auth->isLoggedIn()) {
            $user = $auth->getCurrentUser();
            include __DIR__ . '/views/dashboard.php'; // Use a view for dashboard content
        } else {
            header("Location: /login");
            exit;
        }
        break;

    default:
        header("Location: /login"); 
        exit;
}

?>