CREATE DATABASE IF NOT EXISTS POS;

USE POS;

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


CREATE TABLE IF NOT EXISTS pos.products (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    image VARCHAR(255),
    code VARCHAR(10),
    type VARCHAR(255),
    name VARCHAR(255),
    description VARCHAR(255),
    stock DOUBLE,
    cost DOUBLE,
    price DOUBLE
);