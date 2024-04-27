/*Creando una BD con comandos SQL*/
CREATE DATABASE database2;

/*Pasar a usar una DB ya creada*/
USE database1;

/*Creacion de un tabla con SQL*/
CREATE TABLE usuarios (id INT(10) PRIMARY KEY,nombre VARCHAR(50), apellido VARCHAR(50), correo VARCHAR(100)); 

/*Mostrar todos los datos de una tabla*/
SELECT * FROM usuarios;

/*Insertar datos en una tabla*/
INSERT INTO usuarios VALUES (1,"Arley","Pinchao","pinchao@gmial.com");
INSERT INTO usuarios VALUES (2,"Sandra","Ramirez","ramirez@gmail.com");
INSERT INTO usuarios VALUES (3,"Danilo","Calpa","calpa@gmail.com");

USE sakila;
/*NOTA: en las tbalas es buena practica agregar fechas de registro, actualizacion y estado, para no eliminar datos de una tabla*/
SELECT * FROM actor;

/*Cosultrando columnas especificas de una tabla*/
SELECT first_name, last_name FROM actor;

/*Poniendo alias a una columna para consultar las tablas*/
SELECT first_name AS nombre, last_name AS apellido FROM actor;

/*Condiciones y/o filtrados de informacion*/
SELECT * FROM country WHERE country = 'Colombia';

select * from film;

/*En BD el diferente de, es distinto al de programacion, se utiliza "<>" */
SELECT * FROM film WHERE release_year <> 2006;

/*DISTINCT: filtra un solo campo de varios repetidos y los muestra, nos puede servir para ver que tipo de campos hay llenos en esa columna*/
SELECT special_features FROM film; 
SELECT DISTINCT (special_features) FROM film;

/*Ordenando campos con ORDER BY ( ASC: menor a mayor) y (DESC: mayor a menor)*/
SELECT * FROM film ORDER BY rental_duration ASC;
SELECT * FROM actor ORDER BY last_name DESC;

/*Consultas con 2 condiciones*/
SELECT * FROM film; 
SELECT * FROM film WHERE rating = 'G' AND special_features = 'Trailers';
SELECT * FROM film WHERE rating = 'G' OR special_features = 'Trailers';
SELECT * FROM film WHERE rating = 'G' AND (special_features = 'Trailers' OR special_features = 'Deleted Scenes');
SELECT * FROM film WHERE rating = 'G' AND NOT(special_features = 'Trailers' OR special_features = 'Deleted Scenes');

SELECT * FROM film WHERE rental_duration IN (3,5);
SELECT * FROM film WHERE special_features IN ('Trailers','Commentaries,Deleted Scenes');

/*Consultas con rango de informacion*/
SELECT * FROM  film WHERE replacement_cost BETWEEN 22.99 AND 30.99 ORDER BY replacement_cost ASC;

/*Filtros de string con like, para filtrar por particiones*/
/*Inicia con S*/
SELECT * FROM film WHERE title LIKE 'S%';
/*Termina con O*/
SELECT * FROM film WHERE title LIKE '%O';
/*Busqueda por porcion de string*/
SELECT * FROM film WHERE title LIKE '%MAN%';
/*Consulta de titulos que inician con F y termian en L*/
SELECT * FROM film WHERE title LIKE 'F%L';

/*Conteo de registros de una tabla*/
SELECT count(*) FROM film;

/*Max, Min y promedio*/
SELECT MIN(rental_duration) FROM film;
SELECT MAX(rental_duration) FROM film;
SELECT AVG(rental_duration) FROM film;

/*Agrupamiento de campos por datos*/
SELECT special_features, count(*) FROM film GROUP BY special_features;

/*Pasar todo a mayusculas*/
SELECT UCASE(description) FROM film;

/*Pasar todo a minusculas*/
SELECT LCASE(title) FROM film;

/*contar caracteres de un campo*/
SELECT title, char_length(title) FROM film;

/*Casos en BD similar a un match en PYTHON, entre mayor las condiciones se usen en BD, mas se optimiza el codigo*/
/*OJO CON LA ESTRUCTUTA Y SU TABULACION*/
SELECT replacement_cost,
CASE
	WHEN replacement_cost < 20 THEN 'El costo de reemplazo es menor a 20'
    WHEN replacement_cost > 20 THEN 'El costo de reemplazo es mayor a 20'
    ELSE 'El costo de reemplazo es 20'
END AS condiciones
FROM film;

/*Actualizacion de campos de la BD con UPDATE*/

UPDATE film 
SET title  = 'DINOSAURIO 1'
WHERE  film_id = 1;
/*Verificando cambios*/
SELECT * FROM film WHERE  film_id = 1;





