-- Part 1 Data Retrieval Task
--1.1 Comedy Movies filter: List all comedy movies released between 2000 and 2004. The output should be sorted alphabetically by title.

SELECT 
     f.title, f.release_year, c.name
FROM film f JOIN  film_category fc
ON f.film_id = fc.film_id 
JOIN category c ON fc.category_id = c.category_id 
WHERE LOWER(c.name) = 'comedy' AND f.release_year BETWEEN 2000 AND 2004
ORDER BY f.title 

--1.2 Store Revenue (2017): Calculate the total revenue for every rental store for the year 2017.
--Requirement: Display the store address (merging address and address2 into a single column) and the total revenue.
SELECT 
   CONCAT(a.address, ' ', a.address2) AS store_address, SUM(p.amount) AS total_revenue
FROM store s
JOIN staff st ON s.store_id = st.store_id
JOIN payment p ON p.staff_id = st.staff_id
JOIN address a ON s.address_id = a.address_id
WHERE p.payment_date BETWEEN '2017-01-01' AND '2017-12-31'
GROUP BY CONCAT(a.address, ' ', a.address2);

--1.3 Top 3 Prolific Actors: Find the top 3 actors based on the number of movies they have appeared in.
--Requirement: Display first_name, last_name, and number_of_movies, sorted by the count in descending order.
SELECT a.first_name, a.last_name, COUNT(fa.film_id)
FROM actor a JOIN film_actor fa ON a.actor_id = fa.actor_id 
GROUP BY a.first_name, a.last_name  
ORDER BY COUNT(fa.film_id) DESC
LIMIT 3


--1.4 Genre Trends by Year: Calculate the number of Comedy, Horror, and Action movies released per year.
--Requirement: Output columns for release_year, number_of_action_movies, number_of_horror_movies, and number_of_comedy_movies. 
--Sort the result by release year in descending order.
SELECT f.release_year,
    COUNT(*) FILTER (WHERE LOWER(c.name) = 'action') AS number_of_action_movies,
    COUNT(*) FILTER (WHERE LOWER(c.name) = 'horror') AS number_of_horror_movies,
    COUNT(*) FILTER (WHERE LOWER(c.name) = 'comedy') AS number_of_comedy_movies
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON c.category_id = fc.category_id
GROUP BY f.release_year
ORDER BY f.release_year DESC;

--Part 2: Analytical & Business Problems
--2.1 Staff Performance (Bonus eligibility): 2.1 Which staff members made the highest revenue for each store and deserve a bonus for 2017 year?
SELECT 
    s.store_id,
    s.first_name,
    s.last_name,
    SUM(p.amount) AS total_revenue
FROM staff s
JOIN payment p ON s.staff_id = p.staff_id
WHERE p.payment_date BETWEEN '2017-01-01' AND '2017-12-31'
GROUP BY s.store_id, s.staff_id, s.first_name, s.last_name
ORDER BY s.store_id, total_revenue DESC;


--2.2 Popularity & Audience Demographics: Which 5 movies were rented more than others and what's expected audience age for those movies?
--Requirement: List the film ID, title, and MPAA rating (to determine the expected audience age) for these top 5 films.
SELECT f.film_id, f.title, f.rating
FROM film f 
JOIN inventory i  ON f.film_id = i.film_id 
JOIN rental r ON i.inventory_id = r.inventory_id 
GROUP BY f.film_id, f.title, f.rating
ORDER BY COUNT(f.film_id) DESC 
LIMIT 5


--2.3 Career Gaps: Which actors/actresses didn't act for a longer period of time than others?
SELECT a.first_name, a.last_name, (MAX(f.release_year) - MIN(f.release_year )) AS career_gap
FROM actor a 
JOIN film_actor fa ON a.actor_id = fa.actor_id 
JOIN film f ON f.film_id = fa.film_id 
GROUP BY a.first_name , a.last_name
ORDER BY career_gap  DESC
LIMIT 1

--Part 3: Advanced Geographic & Customer Analytics
--3.1 Top US Categories: Find the Top 3 best-selling movie categories of all time, but only for customers located in the USA.
--Requirement: Display the category name and the total rental income.
--Challenge: Requires joining payment all the way to country via customer, address, and city.
SELECT c.name AS category_name, SUM(p.amount) AS total_rental_income
FROM payment p JOIN rental r ON p.rental_id = r.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
JOIN customer cu ON p.customer_id = cu.customer_id
JOIN address a ON cu.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
WHERE lower(co.country) = 'united states'
GROUP BY c.name
ORDER BY total_rental_income DESC
LIMIT 3;

--3.2 Customer Horror History: For every client, generate a personalized summary of their horror movie rentals.
--Requirement: Display the customer's name, a comma-separated list of all Horror films they have ever rented (in a single column), and the total amount of money they paid for these horror rentals.
--Challenge: Requires using STRING_AGG() (or similar) and filtering by the 'Horror' category.
SELECT c.first_name, c.last_name, STRING_AGG(DISTINCT f.title, ', '), SUM(p.amount )
FROM customer c 
JOIN rental r ON c.customer_id = r.customer_id 
JOIN inventory i ON r.inventory_id = i.inventory_id 
JOIN film f ON i.film_id = f.film_id 
JOIN film_category fg ON f.film_id = fg.film_id
JOIN category ca ON fg.category_id = ca.category_id 
JOIN payment p ON r.rental_id = p.rental_id 
WHERE LOWER(ca."name" )='horror'
GROUP BY c.first_name, c.last_name

