drop database if exists etecbd;
create database etecbd;
use etecbd;

CREATE TABLE Clientes (
  IDCliente INT AUTO_INCREMENT PRIMARY KEY,
  Cliente VARCHAR(50),
  Estado VARCHAR(2),
  Sexo CHAR(1),
  Status VARCHAR(50)
);

CREATE TABLE Vendas (
  IDVenda INT AUTO_INCREMENT PRIMARY KEY,
  IDVendedor INT,
  IDCliente INT,
  data_ DATE,
  Total DECIMAL(10,2),
  FOREIGN KEY (IDVendedor) REFERENCES Vendedores(IDVendedor),
  FOREIGN KEY (IDCliente) REFERENCES Clientes(IDCliente)
);

CREATE TABLE ItensVenda (
  IDProduto INT,
  IDVenda INT,
  Quantidade INT,
  ValorUnitario DECIMAL(10,2),
  ValorTotal DECIMAL(10,2),
  Desconto DECIMAL(10,2),
  PRIMARY KEY (IDProduto, IDVenda),
  FOREIGN KEY (IDProduto) REFERENCES Produtos(IDProduto) ON DELETE RESTRICT,
  FOREIGN KEY (IDVenda) REFERENCES Vendas(IDVenda) ON DELETE CASCADE
);