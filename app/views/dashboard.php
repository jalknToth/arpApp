<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>A R P A</title>
    <link rel="shortcut icon" href="/public/img/favicon.png" type="image/x-icon">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="/public/styleIN.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>
<div class="topnav-container">
      <div>
        <a href="/dashboard" class="logoIN">
          <div class="nomPag">Dashboard</div>
        </a>
      </div>
      <div class="topnav">
        <a href="/dashboard"><i class="fa fa-bar-chart" style="color: #0b00a2;"></i></a>
        <a href="/logout"><i class="fa fa-sign-out"></i></a>  </div>
    </div>
    
    <div class="row">
        <div class="column">
          <div class="card">
            <a href="./personas.html"><i class="fa fa-id-card"><span class="titles">Personas</span></i>368</a>
          </div>
        </div>
      
        <div class="column">
          <div class="card">
            <a href="./auditorias.html"><i class="fa fa-book"><span class="titles">Auditorías</span></i>50</a>
          </div>
        </div>

        <div class="column">
          <div class="card">
            <a href="./informes.html"><i class="fa fa-file-text-o"><span class="titles">Informes</span></i>12</a>
          </div>
        </div>
        
        <div class="column">
          <div class="card">
            <a href="./alertas.html"><i class="fa fa-exclamation-circle" style="color: red;"><span class="titles" style="color: red;">Alertas</span></i>15</a>
          </div>
        </div>

        <div class="column">
          <div class="card">
            <a href="./upload.html" style="color: green;"><i class="fa fa-file-o"><span class="titles">Analizar Archivo</span></i><i class="fa fa-upload" style="color: #0b00a2;"></i></a>
          </div>
        </div>

        <div class="column">
          <div class="card">
            <a href=""><i class="fa fa-comment-o"><span class="titles">Preguntar Arpa</span></i><i class="fa fa-keyboard-o"></i></a>
          </div>
        </div>
        
    </div>

    <?php if(isset($user)): ?>
        <p>Welcome, <?php echo $user['username']; ?>! </p>
         <!-- Now you can access user data -->
    <?php endif; ?>

</body>
</html>