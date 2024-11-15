# arpApp



## Descripción



## Capturas de Pantalla

![Captura de pantalla 1](screenshots/captura1.png)
![Captura de pantalla 2](screenshots/captura2.png)
![Captura de pantalla 3](screenshots/captura3.png)

## Estructura del proyecto

```
arpApp/
├── static/             # Static files (CSS)
│   └── style.css
├── uploads/            # Upload directory
├── templates/          # HTML templates
│   ├── error.html      # Error page
│   ├── index.html      # Main page
│   ├── register.html   # Main page
│   ├── recover.html    # Main page
│   ├── login.html      # Main page
│   ├── dashboard.html  # Main page
│   └── excelData.html  # Page to display Excel data
├── .gitignore          # Files ignored by Git
├── .git                # Git directory 
├── .env                # Environment variables 
├── README.md           # Project information
├── requirements.txt    # Project dependencies
├── structure.txt       # Structure file (this README)
├── server.py           # Main Flask server script
└── excelReader.py      # Module to process Excel files
```

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/jalknToth/arpApp.git
```

2. Crea un archivo `.env` en la raíz del proyecto 

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
