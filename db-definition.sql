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


INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Ferretería','MECHA','MECHA T/PALA P/MADE 6mm 030063',10,237.1,364.77);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Electricidad','MECHA','MECHA T/PALA P/MADE 8mm 030064',9,247.06,380.09);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Plomería','MECHA','MECHA T/PALA P/MAD 28mm 030065',5,349.4,537.54);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Pinturería','MECHA','MECHA T/PALA P/MAD30mm 030066',3,361.88,556.74);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Herramientas','MECHA','MECHA T/PALA P/MAD35mm 030067',8,449.26,691.17);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Maquinaria','MECHA','MECHA T/PALA P/MAD38mm 030068',2,474.23,729.58);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Ferretería','MECHA','MECHA T/PALA P/MAD40mm 030069',0,496.66,764.09);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Electricidad','MECHA','MECHA T/PALA P/MAD10mm 030070',12,254.55,391.62);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Plomería','MECHA','MECHA T/PALA P/MAD12mm 030071',15,262.06,403.17);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Pinturería','MECHA','MECHA T/PALA P/MAD14mm 030072',3,269.54,414.68);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Herramientas','MECHA','MECHA T/PALA P/MAD16mm 030073',10,279.53,430.05);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Maquinaria','MECHA','MECHA T/PALA P/MAD18mm 030074',9,287.01,441.56);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Ferretería','MECHA','MECHA T/PALA P/MAD20mm 030075',5,297.01,456.94);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Electricidad','MECHA','MECHA T/PALA P/MAD22mm 030076',3,311.97,479.95);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Plomería','MECHA','MECHA T/PALA P/MAD25mm 030077',8,336.95,518.39);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Pinturería','MECHA','MECHA T/PALA P/MAD32mm 030078',2,399.31,614.32);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Herramientas','MECHA','MECHA FORSTNER Ø25 CR 030097',10,973.37,1497.49);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Maquinaria','MECHA','MECHA FORSTNER Ø35 CR 030098',9,1197.99,1843.06);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Ferretería','MECHA','MECHA P/MAD DE CR.VA.4mm030204',5,289.49,445.37);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Electricidad','MECHA','MECHA P/MAD DE CR.VA.5mm030205',3,344.42,529.87);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Plomería','MECHA','MECHA P/MAD DE CR.VA.6mm030206',8,376.87,579.8);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Pinturería','MECHA','MECHA P/MAD DE CR.VA.7mm030207',2,436.76,671.94);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Herramientas','MECHA','MECHA P/MAD DE CR.VA.8mm030208',0,484.19,744.9);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Maquinaria','MECHA','MECHA P/MAD DE CR.VA.9mm030209',12,536.61,825.56);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Ferretería','MECHA','MECHA P/MAD DE CR.VA10mm030210',15,566.53,871.58);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Electricidad','BISELADOR','BISELADOR P/TOR 3mm    W151801',10,836.07,1286.26);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Plomería','BISELADOR','BISELADOR P/TOR 4mm   W151802',9,873.54,1343.9);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Pinturería','BISELADOR','BISELADOR P/TOR 5mm    W151803',5,973.37,1497.49);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Herramientas','BISELADOR','BISELADOR P/TOR 6mm    W151804',3,1035.78,1593.5);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Maquinaria','BISELADOR','BISELADOR P/TOR 8mm    W151806',10,1073.17,1651.03);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Ferretería','BROCA','BROCA DIAMANTADA 5 mm',9,1518.77,2336.57);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Electricidad','BROCA','BROCA DIAMANTADA 6 mm',5,1563.44,2405.29);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Plomería','BROCA','BROCA DIAMANTADA 8 mm',3,1623,2496.92);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Pinturería','BROCA','BROCA DIAMANTADA 10 mm',8,1801.68,2771.81);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Herramientas','BROCA','BROCA DIAMANTADA 12 mm',2,2293.04,3527.76);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Maquinaria','BROCA','BROCA DIAMANTADA 14 mm',0,2680.18,4123.35);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Ferretería','SIERRA','SIERRA COPA DIAMANTADA 20 mm',10,2620.62,4031.72);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Electricidad','SIERRA','SIERRA COPA DIAMANTADA 25 mm',9,3275.77,5039.65);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Plomería','SIERRA','SIERRA COPA DIAMANTADA 30 mm',5,3930.93,6047.58);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Pinturería','SIERRA','SIERRA COPA DIAMANTADA 35 mm',3,4600.97,7078.42);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Herramientas','SIERRA','SIERRA COPA DIAMANTADA 40 mm',10,5256.13,8086.35);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Maquinaria','SIERRA','SIERRA COPA DIAMANTADA 50 mm',9,6566.44,10102.21);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Ferretería','SIERRA','SIERRA COPA DIAMANTADA 65 mm',5,7281.15,11201.77);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Electricidad','DISCO','DISCO-TUNGSTENO P/MADERA 115mm',3,1187.83,1827.43);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Plomería','LIMA','LIMA HSS ROT.METC/RED4mm350650',8,1123.21,1728.01);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Pinturería','LIMA','LIMA HSS ROT.MET. 6mm 350651',2,1123.21,1728.01);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Herramientas','LIMA','LIMA HSS ROT.MET.CABEZ CIL.6mm',0,1123.21,1728.01);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Maquinaria','LIMA','LIMA HSS ROT.MET.CABEZ  RED6mm',12,1123.21,1728.01);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Ferretería','LIMA','LIMA HSS ROT.MET.CAB.CONIC 6mm',15,1123.21,1728.01);
INSERT INTO pos.products (type,name,info,stock,cost,price) VALUES ('Electricidad','LIMA','LIMA HSS ROT.MET.CAB CIL PTA.6',3,1123.21,1728.01);