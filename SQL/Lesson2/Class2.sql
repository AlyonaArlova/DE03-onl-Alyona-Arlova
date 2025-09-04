SELECT *
FROM film f
WHERE rating IN ('PG', 'PG-13') AND length BETWEEN 85 AND 120
ORDER BY length DESC, title ASC
LIMIT 20


SELECT *
FROM film f
WHERE title LIKE 'A%' AND replacement_cost BETWEEN 9.99 AND 19.99
ORDER BY replacement_cost ASC, title ASC


SELECT *
FROM customer
WHERE store_id = 1 AND active = 1 AND email LIKE '%.org'
ORDER BY last_name ASC, first_name ASC
LIMIT 50


SELECT *
FROM payment 
WHERE amount >= 5.00 AND payment_date BETWEEN '2017-06-01' AND '2017-06-30'
ORDER BY amount DESC, payment_date ASC
LIMIT 30 OFFSET 30



