SELECT f.title,
       c.name AS category
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
ORDER BY c.name, f.title;


SELECT cu.first_name,
       cu.last_name,
       f.title AS film_title
FROM customer cu
JOIN rental r ON cu.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
ORDER BY cu.last_name, cu.first_name;


SELECT s.first_name AS staff_first_name,
       s.last_name  AS staff_last_name,
       c.first_name AS customer_first_name,
       c.last_name  AS customer_last_name
FROM staff s
JOIN payment p ON s.staff_id = p.staff_id
JOIN customer c ON p.customer_id = c.customer_id
ORDER BY s.last_name, c.last_name;


SELECT a.first_name,
       a.last_name
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id
WHERE f.title = 'Academy Dinosaur'
ORDER BY a.last_name, a.first_name;




