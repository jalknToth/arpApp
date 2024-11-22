<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Registrarse</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <link rel="stylesheet" href="/public/style.css">
</head>
<body>
  
  <?php if (isset($_SESSION['error'])): ?>
      <div class="error-message"><?php echo $_SESSION['error']; ?></div>
      <?php unset($_SESSION['error']); ?> 
  <?php endif; ?>

  <div class="item">
        <a href="/login"><i class="logo" id="logo"></i></a>
  </div>

  <div class="container" id="container">

    <div class="form">

      <form method="POST" action="/register"> 

        <div class="input-group">
            <i class=""></i>
            <input type="text" id="nombre" name="nombre" placeholder="Nombre" required autofocus >
        </div>
        <div class="input-group">
            <i class=""></i>
            <input type="text" id="apellido" name="apellido" placeholder="Apellido" required>
        </div>
        <div class="input-group">
            <i class=""></i>
            <input type="text" id="cedula" name="cedula" placeholder="Cédula" required>
        </div>
        <div class="input-group">
            <i class=""></i>
            <input type="email" id="correo" name="correo" placeholder="Correo" required>
        </div>
        <div class="input-group">
            <i class=""></i>
        <input type="text" id="cargo" name="cargo" placeholder="Cargo" required>
        </div>
        <div class="input-group">
            <i class=""></i>
            <input type="password" id="contrasena" name="contrasena" placeholder="Contraseña" required>
        </div>
        <div class="input-group">
            <i class=""></i>
            <input type="password" id="confTrasena" name="confTrasena" placeholder="Confirmar contraseña" required>
        </div>

        <div class="input-group">
            <button type="submit"> <i class="fa fa-edit"></i> Registrarse </button>
        </div>

      </form>

    </div>

  </div>
</body>
</html>