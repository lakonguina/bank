CREATE DATABASE frontoffice;

\c frontoffice

CREATE TABLE IF NOT EXISTS countries (
	alpha3 CHAR(3) PRIMARY KEY,
	name VARCHAR(64) NOT NULL
);

CREATE TABLE IF NOT EXISTS users_status (
	id_user_status SERIAL PRIMARY KEY,
	slug VARCHAR(64)
);


CREATE TABLE IF NOT EXISTS users (
	id_user SERIAL PRIMARY KEY,
	id_user_status INT NOT NULL,
	alpha3 CHAR(3) NOT NULL, -- Nationality
	password VARCHAR(64) NOT NULL,
	first_name VARCHAR(64) NOT NULL, 
	last_name VARCHAR(64) NOT NULL,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_user_status FOREIGN KEY(id_user_status) REFERENCES users_status(id_user_status),
	CONSTRAINT fk_country FOREIGN KEY(alpha3) REFERENCES countries(alpha3)
);


CREATE TABLE IF NOT EXISTS addresses (
	id_address SERIAL PRIMARY KEY,
	id_user INT NOT NULL,
	alpha3 CHAR(3) NOT NULL, -- Country of the address
	street VARCHAR(64),
	city VARCHAR(64),
	zip_code VARCHAR(64),
	is_active BOOLEAN NOT NULL DEFAULT TRUE,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_user FOREIGN KEY(id_user) REFERENCES users(id_user),
	CONSTRAINT fk_country FOREIGN KEY(alpha3) REFERENCES countries(alpha3)
);


CREATE TABLE IF NOT EXISTS phones (
	id_phone SERIAL PRIMARY KEY,
	id_user INT NOT NULL,
	phone VARCHAR(16) NOT NULL,
	is_active BOOLEAN NOT NULL DEFAULT TRUE,
	is_valid BOOLEAN NOT NULL DEFAULT FALSE,
	date_validation TIMESTAMP,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_user FOREIGN KEY(id_user) REFERENCES users(id_user)
);

CREATE TABLE IF NOT EXISTS emails (
	id_email SERIAL PRIMARY KEY,
	id_user INT NOT NULL,
	email VARCHAR(320) NOT NULL,
	is_active BOOLEAN NOT NULL DEFAULT TRUE,
	is_valid BOOLEAN NOT NULL DEFAULT FALSE,
	date_validation TIMESTAMP,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_user FOREIGN KEY(id_user) REFERENCES users(id_user)
);

/*
CREATE TABLE IF NOT EXISTS documents_type (
	id_document_type SERIAL PRIMARY KEY,
	slug VARCHAR(32) NOT NULL,
);

CREATE TABLE IF NOT EXISTS documents (
	id_document SERIAL PRIMARY KEY,
	id_user INT NOT NULL,
	id_document_type VARCHAR(320) NOT NULL,
	is_valid BOOLEAN NOT NULL DEFAULT FALSE,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_user KEY(id_user) REFERENCES users(id_user),
	CONSTRAINT fk_document_type KEY(id_document_type) REFERENCES documents_type(id_document_type)
);
*/
