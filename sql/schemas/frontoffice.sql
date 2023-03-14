CREATE DATABASE frontoffice;

\c frontoffice


CREATE TABLE IF NOT EXISTS countries (
	id_country SERIAL PRIMARY KEY,
	alpha2 CHAR(2) NOT NULL,
	alpha3 CHAR(3) NOT NULL,
	name VARCHAR(127) NOT NULL,
	is_active BOOLEAN,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS customers (
	id_customer SERIAL PRIMARY KEY,
	id_country INT NOT NULL,
	first_name VARCHAR(64) NOT NULL, 
	last_name VARCHAR(64) NOT NULL,
	password VARCHAR(64) NOT NULL,
	is_active BOOLEAN,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_country
      		FOREIGN KEY(id_country)
	  	REFERENCES countries(id_country)
);

CREATE TABLE IF NOT EXISTS contacts (
	id_contact SERIAL PRIMARY KEY,
	id_customer INT NOT NULL,
	phone VARCHAR(15) NOT NULL,
	is_phone_active BOOLEAN NOT NULL,
	is_active BOOLEAN NOT NULL,
	date_phone TIMESTAMP,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_customer
      		FOREIGN KEY(id_customer)
	  	REFERENCES customers(id_customer)
);
