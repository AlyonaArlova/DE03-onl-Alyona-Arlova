--(база dvdrental)

--1. Создать базу данных library, внутри неё таблицу books с полями:
-- book_id (целое число, первичный ключ, автоинкремент), title (строка до 200 символов, не пустая), 
--author (строка до 100 символов), published_year (целое число, год издания).
-- После этого добавить в таблицу три книги.
CREATE DATABASE LIBRARY;
CREATE TABLE booksy(
book_id serial PRIMARY KEY,
title varchar(200) NOT NULL,
author varchar(100),
published_year int
)

INSERT INTO booksy  (title, author, published_year) 
VALUES
('Война и мир', 'Лев Толстой', 1869),
('Преступление и наказание', 'Фёдор Достоевский', 1866),
('Мастер и Маргарита', 'Михаил Булгаков', 1967);

SELECT *
FROM booksy
--2.В таблице books нужно изменить структуру: добавить новый столбец genre типа VARCHAR(50), 
--переименовать столбец title в book_title, а затем удалить столбец published_year.
ALTER TABLE booksy
ADD genre varchar(50); 

ALTER TABLE booksy
RENAME title TO book_title;

ALTER TABLE booksy
DROP COLUMN published_year;

--3. В таблице books удалить все записи, где автор равен 'Unknown'. 
--Создать таблицу archived_books с теми же полями, что и у books, 
--перенести в неё все книги автора 'J.K. Rowling', после чего полностью удалить таблицу archived_books.
DELETE FROM books
WHERE author = 'Unknown';

CREATE TABLE archived_books (
    book_id serial PRIMARY KEY,
    book_title varchar(200) NOT NULL,
    author varchar(100),
    genre varchar(50)
);

INSERT INTO archived_books (book_title, author, genre)
SELECT book_title, author, genre
FROM books
WHERE author = 'J.K. Rowling';

DROP TABLE archived_books;
