<?php
class Auth {
    private $pdo;

    public function __construct(PDO $pdo) {
        $this->pdo = $pdo;
    }

    public function login($username, $password) {
        $stmt = $this->pdo->prepare("SELECT * FROM users WHERE username = :username"); // Or email if that's your login field
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$user || !password_verify($password, $user['password'])) {
            // Combined check for user existence and password verification
            return false; // Login failed (don't reveal specific reasons for security)
        }

        // Successful login
        session_regenerate_id(true); // Important for security: prevent session fixation
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        return true;
    }

    public function logout() {
        session_destroy(); 
    }

    public function register($nombre, $apellido, $cedula, $correo, $cargo, $contrasena, $confTrasena) {

        if ($contrasena !== $confTrasena) {
            return false;  // Passwords don't match – handle error (e.g., set an error message)
        }

        $hashedPassword = password_hash($contrasena, PASSWORD_DEFAULT);


        try {
            $stmt = $this->pdo->prepare("INSERT INTO users (nombre, apellido, cedula, correo, cargo, username, password) VALUES (:nombre, :apellido, :cedula, :correo, :cargo, :correo, :password)");


            $stmt->execute([
                'nombre' => $nombre,
                'apellido' => $apellido,
                'cedula' => $cedula,
                'correo' => $correo,
                'cargo' => $cargo,
                'password' => $hashedPassword
            ]);

            return true;

        } catch (PDOException $e) {
             // Handle database errors (duplicate username/email, etc.)
            if ($e->getCode() == 23000) { // Example: Duplicate entry error (MySQL)
               //  Handle the duplicate entry error (e.g., username already exists)
                return false; // or throw an exception
            } else {
                 // Handle other PDOExceptions
                 error_log("Database error: " . $e->getMessage());
                return false;
            }

        }
    }

    public function isLoggedIn() {
        return isset($_SESSION['user_id']);
    }


    public function getCurrentUser() {
        if (isset($_SESSION['user_id'])) {
            $userId = $_SESSION['user_id'];
            // Retrieve user details from the database based on $userId
            $stmt = $this->pdo->prepare("SELECT * FROM users WHERE id = :userId");
            $stmt->execute(['userId' => $userId]);
            return $stmt->fetch(PDO::FETCH_ASSOC);
        }

        return null;
    }

}