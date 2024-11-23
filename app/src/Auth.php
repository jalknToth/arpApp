<?php
class Auth {
    private $pdo;

    public function __construct(PDO $pdo) {
        $this->pdo = $pdo;
        $this->setupDatabase(); 
    }

    private function setupDatabase() {
        try {
            $this->pdo->exec("
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(50) NOT NULL,
                    apellido VARCHAR(50) NOT NULL,
                    cedula VARCHAR(20) NOT NULL UNIQUE,
                    correo VARCHAR(100) NOT NULL UNIQUE,
                    cargo VARCHAR(50) NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                ) 
            ");
        } catch (PDOException $e) {
            error_log("Error creando la base de datos: " . $e->getMessage());
            throw new Exception("Tabla no creada");
        }
    }

    public function login($username, $password) {
        try {
            $stmt = $this->pdo->prepare("SELECT * FROM users WHERE correo = :correo");
            $stmt->execute(['correo' => $username]);
            $user = $stmt->fetch(PDO::FETCH_ASSOC);

            if (!$user || !password_verify($password, $user['password'])) {
                error_log("Ingreso fallido " . $username);
                return false;
            }

            session_regenerate_id(true);
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['user_email'] = $user['correo'];
            return true;
        } catch (PDOException $e) {
            error_log("Error de ingreso: " . $e->getMessage());
            return false;
        }
    }

    public function register($nombre, $apellido, $cedula, $correo, $cargo, $contrasena, $confTrasena) {
        
        if ($contrasena !== $confTrasena) {
            error_log("Las contraseñas no coinciden");
            return false;
        }

        if (empty($nombre) || empty($apellido) || empty($cedula) || 
            empty($correo) || empty($cargo) || empty($contrasena)) {
            error_log("Campos sin llenar");
            return false;
        }

        if (!filter_var($correo, FILTER_VALIDATE_EMAIL)) {
            error_log("Tipo email incorrecto " . $correo);
            return false;
        }

        $hashedPassword = password_hash($contrasena, PASSWORD_DEFAULT);

        try {
            $stmt = $this->pdo->prepare("
                INSERT INTO users (
                    nombre, apellido, cedula, correo, cargo, password
                ) VALUES (
                    :nombre, :apellido, :cedula, :correo, :cargo, :password
                )
            ");

            $result = $stmt->execute([
                'nombre' => $nombre,
                'apellido' => $apellido,
                'cedula' => $cedula,
                'correo' => $correo,
                'cargo' => $cargo,
                'password' => $hashedPassword
            ]);

            if ($result) {
                error_log("Registro exitoso: " . $correo);
            }
            return $result;

        } catch (PDOException $e) {
            if ($e->getCode() == 23000) { 
                error_log("Registro duplicados: " . $correo);
                return false;
            }
            error_log("Error durante el registro: " . $e->getMessage());
            return false;
        }
    }

    public function isLoggedIn() {
        return isset($_SESSION['user_id']);
    }
}