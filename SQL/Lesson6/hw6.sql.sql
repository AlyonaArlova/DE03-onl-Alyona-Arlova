--1. Повысить цену аренды всех фильмов категории Comedy на 10 процентов, используя обновление с 
--подзапросом к таблицам film_category и category.
UPDATE film
SET rental_rate = rental_rate * 1.10
WHERE film_id IN (
    SELECT fc.film_id
    FROM film_category fc
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Comedy'
);


--2. Удалить всех клиентов, которые находятся в статусе active = 0 и при этом 
--не имеют ни одной записи в таблице rental.

DELETE FROM customer
WHERE active = 0
  AND customer_id NOT IN (
        SELECT customer_id
        FROM rental
  );

--3. Добавить новую запись в таблицу rental для любого фильма категории Action, 
--при этом арендатором должен быть клиент с наибольшим количеством аренд в истории, используя вставку с подзапросом.
WITH 
action_inventory AS (
    SELECT i.inventory_id
    FROM inventory i
    JOIN film_category fc ON i.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    WHERE c.name = 'Action'
    LIMIT 1
),
top_customer AS (
    SELECT c.customer_id
    FROM customer c
    JOIN rental r ON c.customer_id = r.customer_id
    GROUP BY c.customer_id
    ORDER BY COUNT(r.rental_id) DESC
    LIMIT 1
)
INSERT INTO rental (
    rental_date,
    inventory_id,
    customer_id,
    return_date,
    staff_id,
    last_update
)
SELECT
    NOW(),
    ai.inventory_id,
    tc.customer_id,
    NOW() + INTERVAL '7 days',
    1,          -- staff_id
    NOW()
FROM action_inventory ai, top_customer tc;
