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

CREATE TABLE IF NOT EXISTS users_status (
	id_user_status SERIAL PRIMARY KEY,
	slug VARCHAR(64)
);


CREATE TABLE IF NOT EXISTS users (
	id_user SERIAL PRIMARY KEY,
	id_user_status INT NOT NULL,
	password VARCHAR(64) NOT NULL,
	first_name VARCHAR(64) NOT NULL, 
	last_name VARCHAR(64) NOT NULL,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_user_status FOREIGN KEY(id_user_status) REFERENCES users_status(id_user_status)
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
	id_user INT NOT NULL,
	phone VARCHAR(16) NOT NULL,
	is_active BOOLEAN NOT NULL DEFAULT TRUE,
	is_phone_active BOOLEAN NOT NULL DEFAULT FALSE,
	date_validation TIMESTAMP,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_user FOREIGN KEY(id_user) REFERENCES users(id_user)
);

CREATE TABLE IF NOT EXISTS emails (
	id_email SERIAL PRIMARY KEY,
	id_user INT NOT NULL,
	email VARCHAR(320) NOT NULL,
	is_active BOOLEAN NOT NULL DEFAULT TRUE,
	is_email_active BOOLEAN NOT NULL DEFAULT FALSE,
	date_validation TIMESTAMP,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT fk_user FOREIGN KEY(id_user) REFERENCES users(id_user)
);
