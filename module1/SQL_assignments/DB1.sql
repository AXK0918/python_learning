# SELECT COUNT(DISTINCT City) AS Count, City FROM Customers GROUP BY City;
#SELECT MIN(Quantity) AS LeastQuantity, MAX(Quantity) AS HighestQuantity FROM Order_Details;
#SELECT SUM(Quantity) AS TotalQuantity, AVG(Quantity) AS AvgQuantity FROM Order_Details
#SELECT ProductName FROM Products LIMIT 4, 10;
#SELECT * FROM Suppliers WHERE SupplierName LIKE '_A%';
#SELECT * FROM Customers WHERE Country NOT IN ('USA', 'Canada');
#SELECT * FROM order_details WHERE YEAR(OrderDate) BETWEEN 2020 AND 2021 ORDER BY OrderDate DESC;
#SELECT City, COUNT(*) AS Count FROM Customers GROUP BY City;
#SELECT * FROM employees WHERE FirstName NOT IN ('Sanjay', 'Sonia');
#CREATE TABLE `SupplierDetail` LIKE `Suppliers`;
#DELETE FROM `customers` WHERE `Country` = 'Venezuela';