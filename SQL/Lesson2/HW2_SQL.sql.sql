CREATE TABLE IF NOT EXISTS movies (
    movie_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(255),
    release_year DATE,
    duration INT
);


CREATE TABLE IF NOT EXISTS tickets (
    ticket_id SERIAL PRIMARY KEY,
    movie_id INT REFERENCES movies(movie_id),
    customer_name VARCHAR(255),
    seat_number INT,
    price NUMERIC(10,2)
);

INSERT INTO Movies (title, genre, release_year, duration)
VALUES
('Wednesday', 'Mystery', '2022-11-23', 60),
('Inception', 'Sci-Fi', '2010-07-16', 148),
('The Dark Knight', 'Action', '2008-07-18', 152),
('Interstellar', 'Sci-Fi', '2014-11-07', 169),
('Titanic', 'Romance', '1997-12-19', 195);

INSERT INTO Tickets (movie_id, customer_name, seat_number, price)
VALUES
(1, 'Alice Johnson', 12, 9.99),
(2, 'Bob Smith', 8, 12.50),
(3, 'Charlie Brown', 15, 11.00),
(4, 'Diana Prince', 22, 13.75),
(5, 'Ethan Hunt', 5, 10.00);

-- выбор всех фильмов определённого жанра;
SELECT * 
FROM movies m 
WHERE m.genre = 'Mystery'

--выбор фильмов, выпущенных после определённого года;

SELECT *
FROM movies m 
WHERE m.release_year > '2008-07-18'

-- выбор билетов дороже заданной цены;

SELECT *
FROM tickets t  
WHERE t.price >= 11.00

-- поиск фильмов, в названии которых есть определённое слово (LIKE).

SELECT *
FROM movies m 
WHERE m.title LIKE '__d%'
