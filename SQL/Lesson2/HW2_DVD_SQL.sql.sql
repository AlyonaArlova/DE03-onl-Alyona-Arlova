--Вывести клиентов из таблицы customer, указав их имя, фамилию и адрес электронной почты.
SELECT c.first_name , c.last_name, c.email 
FROM customer c

--Выбрать всех актёров из таблицы actor, у которых фамилия начинается с буквы «S».
SELECT *
FROM actor 
WHERE last_name LIKE 'S%'

--Вывести все платежи из таблицы payment, сумма которых (amount) больше 5.00.
SELECT *
FROM payment 
WHERE amount > 5.00