-- Работа с SQL 2
-- 1 --
-- SELECT amt
-- FROM Orders
-- WHERE amt > 1000

-- 2 --
-- SELECT sname, city
-- FROM Salepeople
-- WHERE city = "London" AND comm > .10;

-- 3 --
-- SELECT cname
-- FROM Customers
-- WHERE NOT city = "Rome" AND rating <= 100;

-- 4 --
-- SELECT *
-- FROM Orders
-- WHERE ( amt < 1000 OR NOT (odate = 10/03/1990 AND cnum > 2003 ));

-- 5 --
-- SELECT *
-- FROM Orders
-- WHERE NOT (( odate = 10/03/1990 OR snum > 1006 ) AND amt >= 1500);

-- 6 --
-- SELECT snum, sname, city, comm
-- FROM Salepeople
-- WHERE ( comm > 0.12 AND comm < 0.14 );

-- SELECT *
-- FROM Customers
-- WHERE snum IN (1001, 1007, 1004);

-- SELECT *
-- FROM Salepeople
-- WHERE comm BETWEEN .10 AND .12;

-- SELECT *
-- FROM Salepeople
-- WHERE (comm BETWEEN .10 AND .12) AND NOT comm IN (.10, .12);

-- SELECT *
-- FROM Customers
-- WHERE cname BETWEEN 'A' AND 'G';

-- SELECT *
-- FROM Customers
-- WHERE cname LIKE 'G%';

-- SELECT *
-- FROM Salepeople
-- WHERE sname LIKE 'P__l%';

-- SELECT *
-- FROM Customers
-- WHERE city IS NULL;
-- 
-- SELECT *
-- FROM Customers
-- WHERE city NOT NULL;

-- SELECT *
-- FROM Customers
-- WHERE NOT city IS NULL;
-- 
-- SELECT *
-- FROM Customers
-- WHERE city NOT IN ( 'London', 'San Jose' );
-- 
-- SELECT *
-- FROM Customers
-- WHERE city NOT IN ( 'London', 'San Jose' );

-- 1 --
-- SELECT odate
-- FROM Orders
-- WHERE odate IN ('10/03/1990', '10/04/1990');

-- 2 --
-- SELECT DISTINCT Customers.cname
-- FROM Salepeople, Customers
-- WHERE Salepeople.sname IN ('Peel', 'Motika') AND Customers.snum IN (1001, 1004);

-- 3 --
-- SELECT cname
-- FROM Customers
-- WHERE cname BETWEEN 'A' AND 'G';

-- 4 --
-- SELECT Customers.cname
-- FROM Customers
-- WHERE cname LIKE 'C%';

-- 5 --
-- SELECT *
-- FROM Orders
-- WHERE amt IS NULL OR amt = 0;

-- SELECT sum (amt)
-- From Orders;

-- SELECT avg (amt)
-- FROM Orders;

-- SELECT count (DISTINCT snum)
-- From Orders;
-- 
-- SELECT count (*)
-- From Customers;

-- SELECT count (ALL)
-- FROM Orders;

-- SELECT max ( blnc + amt )
-- FROM Orders;

-- SELECT snum, MAX (amt)
-- FROM Orders
-- GROUP BY snum;

SELECT snum, odate, MAX (amt)
FROM Orders
GROUP BY snum, odate;