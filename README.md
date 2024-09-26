# Inserción de Datos en Base de Datos de Fútbol

Este proyecto consiste en un script de Python que utiliza la biblioteca `Faker` para generar datos ficticios e insertarlos en una base de datos MySQL para un sistema de gestión de fútbol. Las tablas incluidas son `equipos`, `jugadores` y `arbitros`.

## Estructura de la Base de Datos

El script inserta datos en las siguientes tablas:

1. **Equipos**
   - `id`: Identificador único (PK, AUTO_INCREMENT)
   - `nombre`: Nombre del equipo (VARCHAR)
   - `ciudad`: Ciudad del equipo (VARCHAR)
   - `estadio`: Nombre del estadio (VARCHAR)
   - `fechaFundacion`: Fecha de fundación del equipo (DATE)

2. **Jugadores**
   - `id`: Identificador único (PK, AUTO_INCREMENT)
   - `nombre`: Nombre del jugador (VARCHAR)
   - `apellido`: Apellido del jugador (VARCHAR)
   - `fechaNacimiento`: Fecha de nacimiento del jugador (DATE)
   - `nacionalidad`: Nacionalidad del jugador (VARCHAR)
   - `posicion`: Posición del jugador en el campo (VARCHAR)
   - `numeroCamiseta`: Número de la camiseta (INT)
   - `equipoActual`: ID del equipo actual (FK, referencia a `equipos.id`)

3. **Árbitros**
   - `id`: Identificador único (PK, AUTO_INCREMENT)
   - `nombre`: Nombre del árbitro (VARCHAR)
   - `apellido`: Apellido del árbitro (VARCHAR)
   - `nacionalidad`: Nacionalidad del árbitro (VARCHAR)
   - `experiencia`: Años de experiencia (INT)

## Requisitos

- Python 3.x
- MySQL
- Biblioteca `mysql-connector-python`
- Biblioteca `Faker`

### Instalación

Para instalar las bibliotecas necesarias, ejecuta:

```bash
pip install mysql-connector-python faker
