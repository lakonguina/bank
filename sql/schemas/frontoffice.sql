CREATE DATABASE frontoffice;

\c frontoffice

CREATE TABLE IF NOT EXISTS countries (
	id_country SERIAL PRIMARY KEY,
	alpha2 CHAR(2) NOT NULL,
	alpha3 CHAR(3) NOT NULL,
	indicative VARCHAR(3) NOT NULL,
	name VARCHAR(127) NOT NULL,
	birth BOOLEAN DEFAULT TRUE,
	nationality BOOLEAN DEFAULT FALSE,
	residence BOOLEAN DEFAULT FALSE,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS customers (
	id_customer SERIAL PRIMARY KEY,
	login VARCHAR(10) NOT NULL,
	password VARCHAR(64) NOT NULL,
	is_active BOOLEAN DEFAULT TRUE,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS persons (
	id_person SERIAL PRIMARY KEY,
	id_country_nationality INT NOT NULL,
	id_address_birth INT NOT NULL,
	id_address_residence INT NOT NULL,
	id_contact INT NOT NULL,
	first_name VARCHAR(64) NOT NULL, 
	last_name VARCHAR(64) NOT NULL,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

/*
CREATE TABLE IF NOT EXISTS adresses (
	id_address SERIAL PRIMARY KEY,
	street VARCHAR(64) NOT NULL,
	city VARCHAR(64) NOT NULL,
);

CREATE TABLE IF NOT EXISTS contacts (
	id_contact SERIAL PRIMARY KEY,
	id_customer INT NOT NULL,
	phone VARCHAR(16) NOT NULL,
	is_phone_active BOOLEAN NOT NULL,
	email VARCHAR(320) NOT NULL,
	is_email_active BOOLEAN NOT NULL,
	is_active BOOLEAN NOT NULL,
	date_phone TIMESTAMP,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_customer
      		FOREIGN KEY(id_customer)
	  	REFERENCES customers(id_customer)
);
*/
