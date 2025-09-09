--1. Вывести названия фильмов жанра Action, которые сняты на английском языке. 
--Отсортировать по году выпуска (от новых к старым) и вывести первые 20 строк.
-- 1. Вывести названия фильмов жанра Action, которые сняты на английском языке. 
-- Отсортировать по году выпуска (от новых к старым) и вывести первые 20 строк.
SELECT f.title, 
       f.release_year
FROM film f 
JOIN film_category fc 
     ON f.film_id = fc.film_id 
JOIN category c 
     ON c.category_id = fc.category_id
JOIN language l 
     ON f.language_id = l.language_id
WHERE lower(c.name) = 'action' 
  AND lower(l.name) = 'english'
ORDER BY f.release_year DESC
LIMIT 20;



--2. Показать клиентов и города магазинов, к которым они относятся. 
--Вывести только тех клиентов, у которых город начинается на букву A. 
--Отсортировать по фамилии клиента, ограничить результат 25 строками.
SELECT c.first_name, 
       c.last_name, 
       ci.city 
FROM customer c 
JOIN address a 
     ON c.address_id = a.address_id
JOIN city ci 
     ON ci.city_id = a.city_id 
WHERE lower(ci.city ) LIKE 'a%'
ORDER BY c.last_name 
LIMIT 25

--3. Показать список клиентов, фильмов и сумм платежей, где сумма оплаты больше 5. 
--Отсортировать по сумме (по убыванию), затем по дате платежа (по убыванию). Ограничить результат 30 строками.
SELECT 
    c.first_name, 
    c.last_name, 
    f.title AS film_title, 
    p.amount, 
    p.payment_date
FROM payment p
JOIN customer c 
    ON p.customer_id = c.customer_id
JOIN rental r 
    ON p.rental_id = r.rental_id
JOIN inventory i 
    ON r.inventory_id = i.inventory_id
JOIN film f 
    ON i.film_id = f.film_id
WHERE p.amount > 5.00
ORDER BY p.amount DESC, p.payment_date DESC
LIMIT 30;


--4. Вывести все фильмы, в которых снимался актёр или актриса с фамилией MONROE.
--Отсортировать по названию фильма.
 SELECT f.title, 
        a.last_name
 FROM film f 
 JOIN film_actor fa 
      ON f.film_id = fa.film_id
 JOIN actor a 
      ON fa.actor_id = a.actor_id
WHERE LOWER(a.last_name)='monroe'
ORDER BY f.title


--5. Показать список клиентов и фильмов, которые они арендовали и ещё не вернули (return_date IS NULL). 
--Отсортировать по дате аренды (от новых к старым) и вывести 20 строк.
SELECT c.first_name,
       c.last_name, 
       f.title, 
       r.rental_date 
FROM customer c 
JOIN rental r 
     ON c.customer_id = r.customer_id
JOIN inventory i 
     ON r.inventory_id = i.inventory_id 
JOIN film f 
     ON i.film_id = f.film_id 
WHERE r.return_date IS NULL 
ORDER BY r.rental_date desc
LIMIT 20
