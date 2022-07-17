---1

--a
SELECT *
FROM client INNER JOIN dealer
ON (client.id NOTNULL) OR (dealer.id NOTNULL);

--b
SELECT f.id deal_id, f.name dealer_name, c.name client_name, c.city, c.priority grade, f.sell_number, f.date, f.amount
FROM client c INNER JOIN (
    SELECT dealer.id, dealer.name, sell.id AS sell_number, sell.date, sell.amount, sell.client_id
    FROM dealer INNER JOIN sell
    ON sell.dealer_id = dealer.id
    ) AS f
ON c.id = f.client_id;

--c
SELECT d.id, d.name, d.location, d.charge, c.id, c.name, c.priority
FROM dealer AS d INNER JOIN client AS c
ON d.location = c.city;

--d
SELECT sell.id, sell.amount, client.name, dealer.location counrty
FROM sell, client, dealer
WHERE 100 < sell.amount AND sell.amount < 500 AND sell.client_id = client.id AND seLL.dealer_id = dealer.id;

--e
SELECT  d.id, d.name, d.location, d.charge
FROM client AS c INNER JOIN dealer AS d
ON c.dealer_id = d.id
GROUP BY d.id;

--f
SELECT  c.name, c.city, d.name, d.charge
FROM client AS c INNER JOIN dealer AS d
ON d.id = c.dealer_id;

--g
SELECT  c.name, c.city, d.name, d.charge
FROM client AS c,dealer AS d
WHERE d.charge > 0.12 AND c.dealer_id = d.id;

--h
SELECT c.name, c.city, s.id, s.date, s.amount, d.name, d.charge
FROM sell s, client c, dealer d
WHERE s.client_id = c.id AND s.dealer_id = d.id;


---2

--a
CREATE VIEW A AS
    SELECT date, COUNT(client_id) AS number_of_clients,
    SUM(amount) AS total_purchases_amount,
    AVG(amount) AS average_purchases_amount
    FROM sell
    GROUP BY date;

SELECT * FROM A;

--b
CREATE VIEW B AS
    SELECT date, COUNT(client_id) AS number_of_clients,
    SUM(amount) AS total_purchases_amount,
    AVG(amount) AS average_purchases_amount
    FROM sell
    GROUP BY date;

SELECT date, total_purchases_amount
FROM B
ORDER BY total_purchases_amount DESC
LIMIT 5;

--c
CREATE VIEW task_c AS
    SELECT dealer_id, COUNT(id) AS number_of_sells,
    SUM(amount) AS total_purchases_amount,
    AVG(amount) AS average_purchases_amount
    FROM sell
    GROUP BY dealer_id;

SELECT d.name, number_of_sells,
total_purchases_amount, average_purchases_amount
FROM dealer AS d INNER JOIN task_c AS c ON d.id = c.dealer_id;

--d
CREATE VIEW task_d AS
    SELECT d.location, (SUM(s.amount*d.charge)) AS earned
    FROM dealer AS d INNER JOIN sell AS s ON d.id = s.dealer_id
    GROUP BY location;

SELECT * FROM task_d;

--e
CREATE VIEW E AS
    SELECT location, COUNT(s.id) AS number_of_sells,
    SUM(amount) AS total_purchases_amount,
    AVG(amount) AS average_purchases_amount
    FROM sell AS s INNER JOIN dealer AS d ON d.id = s.dealer_id
    GROUP BY location;

SELECT * FROM E