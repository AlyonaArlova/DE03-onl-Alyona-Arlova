--1. Выведите сводку по семейным фильмам (жанр Family), выпущенным начиная с 2007 года. 
--Для каждого года выпуска определите количество фильмов, среднюю, минимальную и максимальную продолжительность.
--Результат отсортируйте по году выпуска в порядке убывания.--
SELECT 
    f.release_year,
    COUNT(*) film_cnt,
    AVG(f.length) avg_length,
    MIN(f.length) min_length,
    MAX(f.length) max_length
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE lower(c.name) = 'family'
  AND f.release_year >= 2007
GROUP BY f.release_year
ORDER BY f.release_year DESC;



--2. Определите суммарную выручку и количество транзакций за 2007 год по каждой стране проживания клиентов.
-- Отсортируйте результат по выручке в порядке убывания и выведите только первые 10 стран.

SELECT
    ctr.country,
    SUM(p.amount) sum,
    COUNT(p.payment_id) cnt
FROM payment p
JOIN customer c  ON p.customer_id = c.customer_id
JOIN address a   ON c.address_id = a.address_id
JOIN city ct     ON a.city_id = ct.city_id
JOIN country ctr ON ct.country_id = ctr.country_id
WHERE p.payment_date >= '2005-01-01'
  AND p.payment_date < '2008-01-01'
GROUP BY ctr.country
ORDER BY sum DESC
LIMIT 10;



--3. Найдите пять категорий фильмов с наибольшим количеством фильмов. 
--Для каждой категории выведите количество фильмов и среднюю стоимость аренды. 
--Результат отсортируйте по числу фильмов в порядке убывания, а при равенстве — по названию категории.

SELECT 
    c.name ctgry,
    COUNT(f.film_id) film_cnt,
    AVG(f.rental_rate) avg_rental_rate
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
ORDER BY film_cnt DESC, c.name
LIMIT 5;
