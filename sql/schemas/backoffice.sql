CREATE DATABASE backoffice;

\c backoffice

CREATE TABLE IF NOT EXISTS users_internal (
	id_user_internal SERIAL PRIMARY KEY,
	email VARCHAR(320) NOT NULL, 
	first_name VARCHAR(64) NOT NULL, 
	last_name VARCHAR(64) NOT NULL,
	password VARCHAR(64) NOT NULL,
	date_insert TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
