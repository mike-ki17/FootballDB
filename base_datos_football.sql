create database futballDB;
use futballDB;


CREATE TABLE equipos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    ciudad VARCHAR(100),
    estadio VARCHAR(100),
    fechaFundacion DATE
);

CREATE TABLE jugadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    fechaNacimiento DATE,
    nacionalidad VARCHAR(50),
    posicion VARCHAR(50),
    numeroCamiseta INT,
    equipoActual INT
);



CREATE TABLE arbitros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    experiencia INT
);

CREATE TABLE partidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fechaHora DATETIME NOT NULL,
    equipoLocal INT,
    equipoVisitante INT,
    estadio VARCHAR(100),
    resultado VARCHAR(10),
    arbitro INT
);



CREATE TABLE plantillas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    equipoId INT,
    temporada VARCHAR(10)
);

CREATE TABLE plantilla_jugadores (
    plantillaId INT,
    jugadorId INT
);





ALTER TABLE jugadores 
ADD CONSTRAINT fk_judadores_equipoAcual
FOREIGN KEY (equipoActual) REFERENCES equipos(id);


ALTER TABLE partidos 
ADD CONSTRAINT fk_partidos_equipoLocal
FOREIGN KEY (equipoLocal) REFERENCES equipos(id);


ALTER TABLE partidos
ADD CONSTRAINT fk_partidos_equipoVisitante
FOREIGN KEY (equipoVisitante) REFERENCES equipos(id);

ALTER TABLE partidos
ADD CONSTRAINT fk_partidos_arbitro
FOREIGN KEY (arbitro) REFERENCES arbitros(id);

ALTER TABLE plantillas
ADD CONSTRAINT fk_plantillas_equipoId
FOREIGN KEY (equipoId) REFERENCES equipos(id);

ALTER TABLE plantilla_jugadores
ADD CONSTRAINT fk_plantilla_jugadores_plantillaId
FOREIGN KEY (plantillaId) REFERENCES plantillas(id);

ALTER TABLE plantilla_jugadores
ADD CONSTRAINT fk_plantilla_jugadores_jugadorId
FOREIGN KEY (jugadorId) REFERENCES jugadores(id);















