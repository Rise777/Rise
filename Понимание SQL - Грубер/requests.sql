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

SELECT *
FROM Salepeople
WHERE (comm BETWEEN .10 AND .12) AND NOT comm IN (.10, .12);

