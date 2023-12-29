/*Creamos el esquema para la base de datos*/
CREATE SCHEMA Ejercicio1;


/*Creamos las tablas para nuestra base */

CREATE TABLE Ejercicio1.Clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    domicilio VARCHAR(200),
    ciudad VARCHAR(200),
    estado VARCHAR(200),
    codigopostal INT,
    email VARCHAR(200)
);

CREATE TABLE Ejercicio1.PEDIDOS (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombrepedido VARCHAR (255),
    vendedor VARCHAR(255),
    fechadepedido DATE,
    producto VARCHAR(255),
    cantidad INT,
    precio DECIMAL(10, 2),
    total DECIMAL(10, 2)
);

CREATE TABLE Ejercicio1.PROVEEDORES (
    id INT AUTO_INCREMENT PRIMARY KEY,
    empresa VARCHAR (255),
    nombredelcontacto VARCHAR (255),
    direccion VARCHAR (255),
    ciudad VARCHAR(255),
    estado VARCHAR(255),
    codigopostal INT,
    email VARCHAR(255)
);

CREATE TABLE Ejercicio1.PRODUCTO (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR (255),
    precio INT,
    marca VARCHAR (255),
    existencia INT
);


/* Insertar datos en las tablas */ 
INSERT INTO Ejercicio1.Clientes (nombre, domicilio, ciudad, estado, codigopostal, email)
    VALUES
    ("Juan Pérez", "Calle 123, Colonia A", "Mexico", "Estado A", 12345, "juan@email.com"),
    ("María Rodríguez", "Avenida 456, Colonia B", "España", "Durango", 54321, "maria@email.com"),
    ("Carlos López", "Calle 789, Colonia C", "Inglaterra", "Estado C", 98765, "carlos@email.com"),
    ("Ana García", "Calle 101, Colonia D", "London", "Estado D", 10101, "ana@email.com"),
    ("Luis Martínez", "Avenida 202, Colonia E", "Brasil", "Estado E", 20202, "luis@email.com"),
    ("Laura González", "Calle 303, Colonia F", "CDMX", "Estado F", 30303, "laura@email.com"),
    ("Pedro Sánchez", "Avenida 404, Colonia G", "CDMX", "Durango", 40404, "pedro@email.com"),
    ("Sofía Torres", "Calle 505, Colonia H", "H", "Estado H", 50505, "sofia@email.com"),
    ("Miguel Ruiz", "Avenida 606, Colonia I", "I", "Estado I", 60606, "miguel@email.com"),
    ("Carmen Vargas", "Calle 707, Colonia J", "J", "Estado J", 70707, "carmen@email.com"),
    ("Fernando Ríos", "Avenida 808, Colonia K", "K", "Estado K", 80808, "fernando@email.com"),
    ("Isabel Morales", "Calle 909, Colonia L", "L", "Estado L", 90909, "isabel@email.com"),
    ("Roberto Paredes", "Avenida 010, Colonia M", "M", "Durango", 10101, "roberto@email.com"),
    ("Gabriela Silva", "Calle 111, Colonia N", "N", "Estado N", 11111, "gabriela@email.com"),
    ("Javier Castro", "Avenida 121, Colonia O", "O", "Durango", 12121, "javier@email.com");

INSERT INTO Ejercicio1.PEDIDOS (nombrepedido,vendedor,fechadepedido,producto,cantidad,precio,total)
    VALUES
    ("Luces led", "Octavio", "2023-04-12", "Luz roja", 3, 10, 30),
    ("Televisor 4K", "Ana", "2023-04-15", "TV Samsung", 1, 500, 500),
    ("Portátil", "Carlos", "2023-04-18", "Laptop HP", 2, 800, 1600),
    ("Teléfono móvil", "Laura", "2023-04-20", "iPhone 13", 1, 1000, 1000),
    ("Aire acondicionado", "Roberto", "2023-04-22", "AC LG", 1, 600, 600),
    ("Sofá", "Isabel", "2023-04-25", "Sofá de cuero", 1, 700, 700),
    ("Mesa de comedor", "Miguel", "2023-04-28", "Mesa de madera", 1, 300, 300),
    ("Lavadora", "Carmen", "2023-05-02", "Lavadora Samsung", 1, 400, 400),
    ("Refrigerador", "Javier", "2023-05-05", "Refrigerador LG", 1, 600, 600),
    ("Bicicleta", "Sofía", "2023-05-08", "Bicicleta de montaña", 2, 250, 500),
    ("Micrófono", "Fernando", "2023-05-10", "Micrófono Shure", 10, 150, 1500),
    ("Impresora", "María", "2023-05-15", "Impresora HP", 10, 120, 1200),
    ("Monitor", "Pedro", "2023-05-18", "Monitor Dell", 2, 180, 360),
    ("Muebles de jardín", "Gabriela", "2023-05-22", "Juego de muebles", 10, 350, 3500),
    ("Horno de microondas", "Luis", "2023-05-25", "Microondas Panasonic", 10, 80, 800);
    
INSERT INTO Ejercicio1.PROVEEDORES (empresa,nombredelcontacto,direccion,ciudad,estado,codigopostal,email)
    VALUES
    ("ALPLA", "Pedro", "Lomas calle 3", "CDMX", "Mexico", 53719, "pedrojf@hotmail.com"),
    ("FabricaTech", "Ana", "Avenida Principal 45", "Guadalajara", "Mexico", 44000, "ana@gmail.com"),
    ("Suministros Industriales", "Carlos", "Calle Industrial 12", "Monterrey", "Mexico", 64000, "carlos@suministros.com"),
    ("Materiales Constructivos", "Luisa", "Avenida Construcción 78", "Puebla", "Mexico", 72000, "luisa@materiales.com"),
    ("TechSolutions", "María", "Calle Innovación 9", "Tijuana", "Mexico", 22000, "maria@techsolutions.com"),
    ("Proveedora de Componentes", "Javier", "Avenida Componentes 22", "Hermosillo", "Mexico", 83000, "javier@proveedora.com"),
    ("Productos Electrónicos", "Sofía", "Calle Electrónica 33", "Querétaro", "Mexico", 76000, "sofia@gmail.com"),
    ("Distribuidora de Acero", "Miguel", "Avenida Acero 15", "Aguascalientes", "Mexico", 20000, "miguel@distribuidora.com"),
    ("Papel y Suministros", "Carmen", "Calle Papel 7", "Cancún", "Mexico", 77500, "carmen@papelysuministros.com"),
    ("Industrias Plásticas", "Fernando", "Calle Plástico 26", "Mérida", "Mexico", 97000, "fernando@plasticas.com"),
    ("Productos Químicos", "Isabel", "Avenida Químicos 18", "Cuernavaca", "Mexico", 62000, "isabel@gmail.com"),
    ("Logística y Transporte", "Roberto", "Avenida Logística 13", "Veracruz", "Mexico", 91700, "roberto@logistica.com"),
    ("Suministros de Oficina", "Gabriela", "Calle Oficina 54", "Oaxaca", "Mexico", 68000, "gabriela@gmail.com"),
    ("Maquinaria Pesada", "Lorenzo", "Avenida Maquinaria 31", "Chihuahua", "Mexico", 31000, "lorenzo@maquinaria.com"),
    ("Construcciones S.A.", "Natalia", "Calle Construcción 62", "Durango", "Mexico", 34000, "natalia@gmail.com");
    
INSERT INTO Ejercicio1.PRODUCTO (descripcion,precio,marca,existencia)
    VALUES
    ("Cuidados para piso", 10, "Bandai", 8),
    ("Laptop HP", 799, "HP", 15),
    ("Teléfono Samsung", 499, "Samsung", 20),
    ("Impresora Canon", 149, "Canon", 5),
    ("Refrigerador LG", 1299, "LG", 10),
    ("Camiseta Nike", 25, "Nike", 50),
    ("Zapatos Adidas", 70, "Adidas", 30),
    ("Smart TV Sony", 899, "Sony", 8),
    ("Cámara Canon", 399, "Canon", 12),
    ("Tablet Apple", 349, "Apple", 18),
    ("Mouse Logitech", 20, "Logitech", 25),
    ("Auriculares Bose", 149, "Bose", 15),
    ("Silla de Oficina", 79, "IKEA", 30),
    ("Licuadora Oster", 39, "Oster", 7),
    ("Teclado Razer", 89, "Razer", 10),
    ("Mochila North Face", 69, "The North Face", 20);

/*Consultas */

SELECT * FROM Clientes 
WHERE ESTADO = 'Durango';

SELECT * FROM PROVEEDORES 
WHERE email LIKE '%@gmail%';

SELECT * FROM PRODUCTO
WHERE precio > 100 ;

SELECT * FROM PRODUCTO 
WHERE precio BETWEEN 15 and 50;

SELECT * FROM PEDIDOS
WHERE total > 200 AND cantidad >=10;

SELECT * FROM PROVEEDORES
WHERE empresa LIKE '%i%';

/*Update para las tablas */

UPDATE Clientes
SET nombre = 'NuevoNombre', domicilio = 'NuevaDireccion'
WHERE id IN (1, 2, 3, 4);

UPDATE PROVEEDORES
SET ciudad = 'Portugal', estado = 'Durango'
WHERE id IN (1, 2, 3, 4);

UPDATE PRODUCTO
SET marca = 'Axe'
WHERE id IN (1, 2, 3, 4);

UPDATE PEDIDOS
SET vendedor = 'Carlos'
WHERE id IN (1, 2, 3, 4);

/*Eliminar datos de tablas */
DELETE FROM Clientes
WHERE id IN (1, 2, 3, 4, 5);

DELETE FROM PEDIDOS
WHERE Id IN (1, 2, 3, 4, 5);

DELETE FROM PRODUCTO
WHERE Id IN (1, 2, 3, 4, 5);

DELETE FROM PROVEEDORES
WHERE Id IN (1, 2, 3, 4, 5);

