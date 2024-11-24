-- Crear la tabla Personas
CREATE TABLE Personas (
    IDpersona INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    cedula VARCHAR(20) UNIQUE NOT NULL,
    correo VARCHAR(255),
    cargo VARCHAR(255),
    contrasena VARCHAR(255)
    compañia VARCHAR(255)
    tipoUsuario VARCHAR(255)
);

-- Crear la tabla Bienes
CREATE TABLE Bienes (
    idBien INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) NOT NULL,
    tipoBien VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fechAdquisicion DATE,
    valor DECIMAL(10,2),
    personaBienID INT,
    FOREIGN KEY (personaBienID) REFERENCES Personas(IDpersona)
);

-- Crear la tabla Rentas
CREATE TABLE Rentas (
    idRenta INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    personaRentaID INT,
    FOREIGN KEY (personaRentaID) REFERENCES Personas(IDpersona)
);

-- Crear la tabla InformesAuditoria
CREATE TABLE InformesAuditoria (
    IDinforme INT PRIMARY KEY AUTO_INCREMENT,
    fechaInforme DATE NOT NULL,
    descripcion TEXT,
    tipoInforme VARCHAR(255) NOT NULL,
    estado VARCHAR(100) NOT NULL
);

-- Crear la tabla DeclaracionConflictos
CREATE TABLE DeclaracionConflictos (
    IDdeclaracion INT PRIMARY KEY AUTO_INCREMENT,
    personaDeclaID INT,
    fecha DATE NOT NULL,
    tipoConflicto VARCHAR(255) NOT NULL,
    descripcion TEXT,
    FOREIGN KEY (personaDeclaID) REFERENCES Personas(IDpersona)
);

-- Crear la tabla LineaTransparencia
CREATE TABLE LineaTransparencia (
    idEntrada INT PRIMARY KEY AUTO_INCREMENT,
    personaEntraID INT,
    fechaEntrada DATE NOT NULL,
    descripcion TEXT,
    tipoInformacion VARCHAR(255),
    estado VARCHAR(255),
    FOREIGN KEY (personaEntraID) REFERENCES Personas(IDpersona)
);

-- Crear la tabla AccesosSAP
CREATE TABLE AccesosSAP (
    idSAP INT PRIMARY KEY AUTO_INCREMENT,
    personaSAPid INT,
    usuario VARCHAR(255) NOT NULL,
    rol VARCHAR(255) NOT NULL,
    fecha_creacion DATE NOT NULL,
    fecha_modificacion DATE,
    estado VARCHAR(255),
    FOREIGN KEY (personaSAPid) REFERENCES Personas(IDpersona)
);

-- Crear la tabla SuccessFactor
CREATE TABLE SuccessFactor (
    idFactor INT PRIMARY KEY AUTO_INCREMENT,
    personaFactorID INT,
    puesto VARCHAR(255) NOT NULL,
    departamento VARCHAR(255) NOT NULL,
    fecha_ingreso DATE NOT NULL,
    FOREIGN KEY (personaFactorID) REFERENCES Personas(IDpersona)
);

-- Crear la tabla InformacionEspecial
CREATE TABLE InformacionEspecial (
    idInforme INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    descripcion TEXT,
    tipo VARCHAR(255) NOT NULL,
    nivel VARCHAR(255) NOT NULL
);

-- Crear la tabla Alertas
CREATE TABLE Alertas (
    idAlerta INT PRIMARY KEY AUTO_INCREMENT,
    fechaDeteccion DATETIME NOT NULL,
    tipo VARCHAR(255) NOT NULL,
    descripcion TEXT,
    nivel ENUM('Bajo', 'Medio', 'Alto') NOT NULL,
    tablaOrigen VARCHAR(255) NOT NULL,
    idTablaOrigen INT NOT NULL,
    estado ENUM('Pendiente', 'En investigación', 'Resuelta') NOT NULL,
    usuarioResponsable VARCHAR(255),
    personaID INT,
    FOREIGN KEY (personaID) REFERENCES Personas(IDpersona)
);

-- Añadir índices para mejorar el rendimiento
CREATE INDEX idx_persona_cedula ON Personas(cedula);
CREATE INDEX idx_bienes_persona ON Bienes(personaBienID);
CREATE INDEX idx_rentas_persona ON Rentas(personaRentaID);
CREATE INDEX idx_declaracion_persona ON DeclaracionConflictos(personaDeclaID);
CREATE INDEX idx_linea_persona ON LineaTransparencia(personaEntraID);
CREATE INDEX idx_sap_persona ON AccesosSAP(personaSAPid);
CREATE INDEX idx_success_persona ON SuccessFactor(personaFactorID);
CREATE INDEX idx_alertas_persona ON Alertas(personaID);
CREATE INDEX idx_alertas_estado ON Alertas(estado);
CREATE INDEX idx_alertas_nivel ON Alertas(nivel);