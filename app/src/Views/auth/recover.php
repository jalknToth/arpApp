<!DOCTYPE html>
<html lang="es">
<head>
    <!-- ... head content from recover.html -->
</head>
<body>
    <div class="item">
        <a href="/"><i class="logo" id="logo"></i></a>
    </div>

    <div class="container" id="container">
        <form method="POST" action="/recover">
            <div class="input-group">
                <input type="text" id="usuario" name="email" placeholder="Email" required>
            </div>
            <button type="submit" value="Submit">
                <i class="fa fa-key"></i> Recuperar contraseña
            </button>


        <a href="/login">
            <button type="button">
                <i class="fa fa-sign-in"></i> Ingresar
            </button>
        </a>
        </form>

    </div>
</body>
</html>