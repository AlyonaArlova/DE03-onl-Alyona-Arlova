--1. Найти все фильмы, продолжительность которых больше средней продолжительности всех фильмов в базе.
SELECT f.film_id, f.title, f.length
FROM film f
WHERE f.length > (SELECT AVG(length) FROM film)
ORDER BY f.length 


WITH avg_len AS (
    SELECT AVG(length) AS avg_length
    FROM film
)
SELECT 
    f.film_id,
    f.title,
    f.length
FROM film f, avg_len
WHERE f.length > avg_len.avg_length
ORDER BY f.length

--2. Найти сотрудников (staff), которые работают в том же магазине, что и клиент с фамилией SMITH.
SELECT s.staff_id, s.first_name, s.last_name
FROM staff s 
JOIN customer c ON s.store_id =c.store_id 
WHERE upper(c.last_name) ='SMITH'


WITH smith_stores AS (
    SELECT DISTINCT store_id
    FROM customer
    WHERE last_name = 'SMITH'
)
SELECT 
    s.staff_id,
    s.first_name,
    s.last_name,
    s.store_id
FROM staff s, smith_stores ss
WHERE s.store_id = ss.store_id;


--3. Найти клиентов, которые заплатили больше, чем средняя сумма платежа по всей базе.
SELECT DISTINCT  c.customer_id, c.first_name, c.last_name
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
WHERE p.amount > (SELECT AVG(amount)FROM payment)
ORDER BY c.customer_id

WITH avg_amount AS (
    SELECT AVG(amount) AS avg_amt
    FROM payment
)
SELECT DISTINCT 
    c.customer_id, 
    c.first_name, 
    c.last_name
FROM customer c, payment p, avg_amount
WHERE c.customer_id = p.customer_id
  AND p.amount > avg_amount.avg_amt
ORDER BY c.customer_id;
