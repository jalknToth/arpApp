<!DOCTYPE html>
<html>
<head>
    <!-- ... head content from login.html -->
</head>
<body>

    <div class="item">
      <a href="/"><i class="logo" id="logo"></i></a> </div>


      <div class="container" id="container">
      <form method="POST" action="/login">  </form>
        <div class="input-group">

          <input type="text" id="usuario" name="usuario" placeholder="Usuario" required >
        </div>

        <div class="input-group">

          <input type="password" id="contrasena" name="contrasena" placeholder="Contraseña" required>
        </div>

        <div class="input-group">
          <button type="submit" value="Submit">
              <i class="fa fa-sign-in"></i>
              Ingresar
          </button>
        </div>
        <div class="input-group">
          <button type="button"> <a href="/recover">
                Recuperar contraseña
              </a>
          </button>

      </div>
    </div>
</body>
</html>