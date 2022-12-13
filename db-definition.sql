-- * CREAR DATABASE POS
CREATE DATABASE IF NOT EXISTS POS;



-- * CREAR TABLA USERS
CREATE TABLE IF NOT EXISTS pos.users (
    UserId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserEmail VARCHAR(255),
    UserName VARCHAR(255),
    UserPassword VARCHAR(255),
    UserRole VARCHAR(5)
);

-- * INSERTAR EJEMPLO DE USUARIO
INSERT INTO pos.users (UserEmail, UserName, UserPassword, UserRole) 
VALUES ('lahozcristian@gmail.com', 'm415x', '1234567890', 'admin');



-- * CREAR TABLA PRODUCTS
CREATE TABLE IF NOT EXISTS pos.products (
    code INT(5) ZEROFILL NOT NULL PRIMARY KEY AUTO_INCREMENT,
    type VARCHAR(255),
    name VARCHAR(255),
    info VARCHAR(255),
    stock DOUBLE,
    cost DOUBLE,
    price DOUBLE,
    img VARCHAR(255)
);


-- * CREAR TABLA SALES
CREATE TABLE IF NOT EXISTS pos.sales (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    datetime_sale INT(14) NOT NULL,
    detail json DEFAULT NULL,
    total DOUBLE
) ENGINE=InnoDB;

-- * INSERTAR EJEMPLO DE VENTA
INSERT INTO pos.sales (datetime_sale, detail, total)
VALUES (
    20221212211929,
    '{
        "0": [4524845, "Pinturería", "MECHA", "MECHA P/MAD DE CR.VA.7mm030207", 671.94, 2],
        "1": [4524847, "Maquinaria", "MECHA", "MECHA P/MAD DE CR.VA.9mm030209", 825.56, 10]
    }',
    9599.48
);

-- * EJEMPLO DE CONSULTA JSON (código del segundo elemento del carrito)
SELECT JSON_EXTRACT(detail, '$.1[0]') as codigo FROM pos.sales