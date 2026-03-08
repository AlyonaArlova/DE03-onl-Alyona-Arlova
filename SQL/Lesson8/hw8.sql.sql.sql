--1. Составные ключи и связи в цепочке таблиц
--Создайте три таблицы:
--departments(dept_id, dept_name) — первичный ключ dept_id.
--employees(emp_id, dept_id, full_name) — первичный ключ emp_id, внешний ключ dept_id ссылается на departments.
--projects(project_id, dept_id, project_name) — первичный ключ project_id, внешний ключ dept_id ссылается на departments.
--Теперь создайте таблицу employee_projects, где хранится назначение сотрудников на проекты.
--В ней должен быть составной первичный ключ (emp_id, project_id) и два внешних ключа, ссылающихся на employees(emp_id) и projects(project_id).
--Вставьте корректные данные и попробуйте вставить запись с несуществующим emp_id или project_id.

CREATE TABLE IF NOT EXISTS departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS employeesa (
    emp_id SERIAL PRIMARY KEY,
    dept_id INT REFERENCES departments(dept_id),
    full_name VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS projects (
    project_id SERIAL PRIMARY KEY,
    dept_id INT REFERENCES departments(dept_id),
    project_name VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS employee_projects (
    emp_id INT,
    project_id INT,
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employeesa (emp_id),
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);
INSERT INTO departments (dept_name) VALUES
('IT'), ('Account'), ('HR');

INSERT INTO employeesa (dept_id, full_name) VALUES
(1, 'Kate Spade'),
(1, 'Test Bob'),
(2, 'Captian Test');

INSERT INTO projects (dept_id, project_name) VALUES
(1, 'SAP project'),
(2, 'Salesforce Project');

INSERT INTO employee_projects (emp_id, project_id) VALUES
(1, 1),
(2, 1),
(3, 2),
(10,20);


--2. Каскадное удаление и ограничение ссылочной целостности
--В таблицах из задачи 1 добавьте правило: при удалении отдела (departments) должны автоматически удаляться все его сотрудники и проекты, но записи в employee_projects при этом не должны удаляться автоматически — база должна выдавать ошибку при попытке удаления.
--Проверьте поведение каскадов (ON DELETE CASCADE, ON DELETE RESTRICT).
DROP TABLE IF EXISTS employee_projects;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS employeesa;
DROP TABLE IF EXISTS departments;


CREATE TABLE IF NOT EXISTS departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS employees (
    emp_id SERIAL PRIMARY KEY,
    dept_id INT NOT NULL,
    full_name VARCHAR(200),
    CONSTRAINT fk_emp_dept
        FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        ON DELETE CASCADE  
);

CREATE TABLE IF NOT EXISTS projects (
    project_id SERIAL PRIMARY KEY,
    dept_id INT NOT NULL,
    project_name VARCHAR(200),
    CONSTRAINT fk_proj_dept
        FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        ON DELETE CASCADE 
);

CREATE TABLE IF NOT EXISTS employee_projects (
    emp_id INT NOT NULL,
    project_id INT NOT NULL,
    PRIMARY KEY (emp_id, project_id),
    CONSTRAINT fk_ep_emp
        FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        ON DELETE RESTRICT,  
    CONSTRAINT fk_ep_proj
        FOREIGN KEY (project_id) REFERENCES projects(project_id)
        ON DELETE RESTRICT 
);

--3.Оптимизация поиска с индексами
--Для таблицы employees создайте три индекса:
--по dept_id;
--по full_name;
--составной по (dept_id, full_name).
--С помощью EXPLAIN ANALYZE сравните выполнение запросов:
--SELECT * FROM employees WHERE dept_id = 10;
--SELECT * FROM employees WHERE full_name = 'Ivan Ivanov';
--SELECT * FROM employees WHERE dept_id = 10 AND full_name = 'Ivan Ivanov';
--Объясните, в каких случаях используется один индекс, составной индекс или оба сразу.

CREATE INDEX idx_employees_dept_id
    ON employees(dept_id);

CREATE INDEX idx_employees_full_name
    ON employees(full_name);

CREATE INDEX idx_employees_dept_fullname
    ON employees(dept_id, full_name);

EXPLAIN ANALYZE SELECT * FROM employees WHERE dept_id = 10;

EXPLAIN ANALYZE SELECT * FROM employees WHERE full_name = 'Ivan Ivanov';

EXPLAIN ANALYZE SELECT *
FROM employees
WHERE dept_id = 10 AND full_name = 'Ivan Ivanov';



--4. Избыточное индексирование и производительность
--Добавьте в таблицу employees ещё один индекс по full_name и сравните результаты вставки 100 000 строк с и без него.
--Используйте EXPLAIN ANALYZE INSERT INTO ... SELECT ... для оценки.
--Объясните, почему большое количество индексов замедляет операции вставки и обновления, и в каких случаях это оправдано.

CREATE INDEX idx_employees_full_name_2 ON employees(full_name);


--5. Реальный сценарий выбора оптимального индекса
--В таблице projects добавьте поля start_date и budget.
--Проанализируйте три типа запросов:
--1. фильтр по start_date (диапазон за год),
--2. фильтр по budget > 1000000,
--3. фильтр одновременно по дате и бюджету.
--Создайте подходящие индексы (B-tree или составной) и объясните, какой из них эффективнее для каждого случая и почему.

ALTER TABLE projects
ADD COLUMN start_date DATE,
ADD COLUMN budget NUMERIC(15,2);

SELECT * FROM projects
WHERE start_date BETWEEN '2024-01-01' AND '2024-12-31';

CREATE INDEX idx_projects_start_date
ON projects(start_date);

SELECT * FROM projects
WHERE budget > 1000000;

CREATE INDEX idx_projects_budget
ON projects(budget);

SELECT * FROM projects
WHERE start_date BETWEEN '2024-01-01' AND '2024-12-31'
  AND budget > 1000000;

CREATE INDEX idx_projects_date_budget
ON projects(start_date, budget);


