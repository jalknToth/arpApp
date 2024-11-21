underconstr.


https://jalkntoth.github.io/arpApp/


arpa/
├── composer.json
├── public/
│   ├── index.php
│   ├── static/
│   │   └── style.css
├── src/
│   ├── Controllers/
│   │   ├── AuthController.php
│   │   └── HomeController.php
│   ├── Models/
│   │   └── User.php
│   ├── Views/
│   │   ├── auth/
│   │   │   ├── login.php
│   │   │   ├── register.php
│   │   │   └── recover.php
│   │   └── home/
│   │       └── index.php  // corresponds to dashboard.html
│   └── config.php // Database connection, etc.
└── vendor/
    └── ... // Composer dependencies