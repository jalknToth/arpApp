<?php
require_once __DIR__ . '/../src/config.php'; // Include configuration
require_once __DIR__ . '/../vendor/autoload.php'; // Autoload Composer dependencies

use App\Controllers\HomeController;
use App\Controllers\AuthController;


// Routing (simple example - you might want to use a routing library)
$request_uri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

switch ($request_uri) {
    case '/':
        $controller = new HomeController();
        $controller->index();
        break;
    case '/login':
        $controller = new AuthController();
        $controller->login();
        break;
    case '/register':
        $controller = new AuthController();
        $controller->register();
        break;
    case '/recover':
        $controller = new AuthController();
        $controller->recover();
        break;
    // ... other routes ...
    default:
        // 404 Not Found
        http_response_code(404);
        echo "404 Not Found";
        break;
}
?>