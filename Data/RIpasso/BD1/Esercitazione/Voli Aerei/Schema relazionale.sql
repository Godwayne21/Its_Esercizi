CREATE DOMAIN IntegerGZ AS INTEGER
	CHECK (value > 0);

CREATE DOMAIN IntegerGEZ AS INTEGER
	CHECK (value >= 0);	

CREATE TABLE Aeroporto (
	codice char(3) not null,
	nome varchar not null,
	primary key (codice)
);