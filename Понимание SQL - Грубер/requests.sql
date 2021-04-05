-- SELECT snum, comm
-- FROM Salepeople;
-- SELECT odate, snum, onum, amt
-- FROM Orders;
-- SELECT DISTINCT snum
-- FROM Orders;
-- SELECT sname, city
-- FROM Salepeople
-- WHERE city = "London"
-- SELECT *
-- FROM Customers
-- WHERE rating = 100;

-- Работа с SQL

-- 1 --
-- SELECT onum, amt, odate
-- FROM Orders;

-- 2 --
-- SELECT *
-- FROM Customers
-- WHERE snum = 1001;

-- 3 --
-- SELECT city, sname, snum, comm
-- FROM Salepeople;

-- 4 --
-- SELECT rating, cname
-- FROM Customers
-- WHERE city = "San Jose";

-- 5 --
-- SELECT DISTINCT snum
-- FROM Orders;

-- SELECT *
-- FROM Customers
-- WHERE rating >= 200;

-- SELECT *
-- FROM Customers
-- WHERE city = "San Jose" OR NOT rating > 200;

SELECT *
FROM Orders
WHERE NOT ((odate = "10/03/1990" AND snum > 1002) OR amt > 2000.00);