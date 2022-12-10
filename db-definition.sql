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

INSERT INTO Users (UserEmail, UserName, UserPassword, UserRole) 
VALUES ('lahozcristian@gmail.com', 'm415x', '1234567890', 'admin');

SELECT * FROM Users;


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