CREATE DATABASE IF NOT EXISTS cadastro_db;

USE cadastro_db;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    sobrenome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    sexo VARCHAR(20) NOT NULL
);