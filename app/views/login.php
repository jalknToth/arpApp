<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="../public/style.css">
</head>
<body>

    <?php if (isset($error_message)): ?>
        <div style="color: red;"><?php echo $error_message; ?></div>
    <?php endif; ?>

    <div class="test">
        <a href="/dashboard"><i class="fa fa-eye"></i>demo</a>
    </div>

    <div class="item">
      <a href="/login"><i class="logo" id="logo"></i></a> </div>

    <div class="container" id="container">

      <div class="form"> 

        <form method="POST" action="/login">
          <div class="input-group">
            <input type="text" id="usuario" name="usuario" placeholder="Correo" required >
          </div>

          <div class="input-group">
            <input type="password" id="contrasena" name="contrasena" placeholder="Contraseña" required>
          </div>
            
          <div class="input-group">
            <button type="submit" value="Submit">
                <i class="fa fa-sign-in"></i> Ingresar
            </button>
          </div>
        </form> 

        <div class="input-group"> 
          <a href="/register">
          <button type="button"> 
              <i class="fa fa-edit"></i> Registrarse
          </button>
          </a>
        </div>

      </div>

    </div>
</body>
</html>