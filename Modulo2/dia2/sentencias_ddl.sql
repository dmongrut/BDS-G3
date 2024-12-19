-- Active: 1734576852313@@127.0.0.1@3306@datag3
CREATE TABLE alumno (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento varchar(10) not NULL,
    nombre varchar(255) not null,
    email varchar(100)
);

--Modificar una tabla
alter table alumno add column nota int default 0;

--Eliminar una tabla
drop table alumno;

--Insert de un valor
insert into alumno (nro_documento, nombre) values ("100", "cesar");

--Insert de varios valores
insert into
    alumno (nro_documento, nombre, nota)
values ("200", "ana", 15),
    ("300", "luis", 20),
    ("400", "jose", 11),
    ("500", "raul", 10),
    ("600", "carmen", 13),
    ("700", "jorge", 16),
    ("800", "daniel", 20),
    ("900", "luisa", 17),
    ("1000", "pedro", 15)

--Actualizar datos (update)
update alumno set email = "codigo@gmail.com";

--Actualizar datos con update y con where
update alumno SET email = "ana@gmail.com" where id = 1;

--Actualizar datos con update y con funciones
update alumno set email = concat(nombre, "@gmail.com") where id != 1;

--Eliminar datos (delete)
delete from alumno where id > 5;

--Seleccionar select
select * from alumno;

select nombre, nota from alumno;

select nombre, nota from alumno where nota > 15;