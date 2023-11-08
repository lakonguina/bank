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

CREATE TABLE IF NOT EXISTS customers_status (
	id_customer_status SERIAL PRIMARY KEY,
	slug VARCHAR(64)
);


CREATE TABLE IF NOT EXISTS customers (
	id_customer SERIAL PRIMARY KEY,
	id_customer_status INT NOT NULL,
	login VARCHAR(64) NOT NULL,
	password VARCHAR(64) NOT NULL,
	first_name VARCHAR(64) NOT NULL, 
	last_name VARCHAR(64) NOT NULL,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_customer_status FOREIGN KEY(id_customer_status) REFERENCES customers_status(id_customer_status)
);

CREATE TABLE IF NOT EXISTS addresses (
	id_address SERIAL PRIMARY KEY,
	id_country INT NOT NULL,
	street VARCHAR(64),
	city VARCHAR(64),
	zip_code VARCHAR(64),
	CONSTRAINT fk_country FOREIGN KEY(id_country) REFERENCES countries(id_country)
);

CREATE TABLE IF NOT EXISTS phones (
	id_phone SERIAL PRIMARY KEY,
	id_customer INT NOT NULL,
	phone VARCHAR(16) NOT NULL,
	is_active BOOLEAN NOT NULL DEFAULT TRUE,
	is_phone_active BOOLEAN NOT NULL DEFAULT FALSE,
	date_validation TIMESTAMP,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_customer FOREIGN KEY(id_customer) REFERENCES customers(id_customer)
);

CREATE TABLE IF NOT EXISTS emails (
	id_email SERIAL PRIMARY KEY,
	id_customer INT NOT NULL,
	email VARCHAR(320) NOT NULL,
	is_active BOOLEAN NOT NULL DEFAULT TRUE,
	is_email_active BOOLEAN NOT NULL DEFAULT FALSE,
	date_validation TIMESTAMP,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_customer FOREIGN KEY(id_customer) REFERENCES customers(id_customer)
);
