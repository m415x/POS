CREATE DATABASE IF NOT EXISTS POS;

USE POS;

CREATE TABLE IF NOT EXISTS Users (
    UserId INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    UserEmail VARCHAR(255),
    UserName VARCHAR(255),
    UserPassword VARCHAR(255),
    UserRole VARCHAR(5)
);

INSERT INTO Users (UserEmail, UserName, UserPassword, UserRole) 
VALUES ('lahozcristian@gmail.com', 'm415x', '1234567890', 'admin');

SELECT * FROM Users;