<!DOCTYPE html>
<html>
<head>
    <!-- ... head content from register.html -->
</head>
<body>
<div class="item">
    <a href="/"><i class="logo" id="logo"></i></a>
</div>

<div class="container" id="container">

    <form method="POST" action="/register"> <div class="input-group">

            <input type="text" id="nombre" name="nombre" placeholder="Nombre" required autofocus >
        </div>

        <input type="text" id="apellido" name="apellido" placeholder="Apellido" required>

         <input type="text" id="cedula" name="cedula" placeholder="Cédula" required>

        <input type="email" id="correo" name="correo" placeholder="Correo" required>


        <input type="text" id="cargo" name="cargo" placeholder="Cargo" required>


        <input type="password" id="contrasena" name="contrasena" placeholder="Contraseña" required>


        <input type="password" id="confirmar_contrasena" name="confirmar_contrasena" placeholder="Confirmar contraseña" required>

        <button type="submit">
            <i class="fa fa-edit"></i>
            Registrarse
        </button>

    </form>
</div>
</body>
</html>