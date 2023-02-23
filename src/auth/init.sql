CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'auth123';

CREATE DATABASE IF NOT EXISTS `auth`;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
   id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   email VARCHAR(255) NOT NULL UNIQUE,
   password VARCHAR(255) NOT NULL
);

INSERT INTO user (email, password) VALUES ('123456@qq.com', 'admin123');

/*
mysql -uroot -e "DROP DATABASE auth" -h localhost -p
mysql -uroot -e "DROP USER auth_user@localhost" -h localhost -p
mysql -uroot -p -h localhost < init.sql
*/