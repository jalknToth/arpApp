# arpApp

Una aplicación web simple en Python para consultar el clima de una ciudad.

## Descripción

ClimaApp utiliza la API de OpenWeatherMap para obtener información meteorológica y la presenta al usuario en una interfaz web amigable.  Permite buscar el clima por nombre de ciudad y muestra la temperatura actual, la descripción del clima y un icono representativo. Tambien puedes conectarla a tu base de datos para cada informacion. 

## Capturas de Pantalla

![Captura de pantalla 1](screenshots/captura1.png)
![Captura de pantalla 2](screenshots/captura2.png)
![Captura de pantalla 3](screenshots/captura3.png)

## Estructura del proyecto

```
arpApp/
├── static/             # Static files (CSS)
│   └── style.css
├── templates/          # HTML templates
├── uploads/            # Upload directory
│   ├── error.html      # Error page
│   ├── index.html      # Main page
│   └── excelData.html  # Page to display Excel data
├── .gitignore          # Files ignored by Git
├── .git                # Git directory 
├── .env                # Environment variables 
├── README.md           # Project information
├── requirements.txt    # Project dependencies
├── structure.txt       # Structure file (this README)
├── server.py           # Main Flask server script
└── excelReader.py     # Module to process Excel files
```

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/jalknToth/arpApp.git
```

2. Crea un archivo `.env` en la raíz del proyecto y agrega tu clave de API de OpenWeatherMap:

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

1. Inicia la aplicación:

```bash
python server.py
```

2. Abre tu navegador web y visita `http://127.0.0.1:5000/`

## Uso

1. 
2.
3.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un *issue* o envía un *pull request*.
