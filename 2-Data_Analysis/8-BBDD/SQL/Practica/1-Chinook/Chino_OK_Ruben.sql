--1
SELECT *
FROM customers
WHERE country = 'Brazil';

--2
SELECT *
FROM employees
WHERE title = 'Sales Support Agent';

--3
SELECT *
FROM tracks
WHERE composer = 'AC/DC';

--4
SELECT CustomerId, FirstName, Country
FROM customers
WHERE country <> 'USA';

--5
SELECT FirstName || ' ' || LastName AS Nombre_Completo, Address, Email
FROM employees
WHERE title = 'Sales Support Agent';

SELECT CONCAT(FirstName, ' ', LastName) AS Nombre_Completo, Address, Email
FROM employees
WHERE title = 'Sales Support Agent';

--6
SELECT DISTINCT BillingCountry
FROM invoices;

--7
SELECT State, COUNT(customerID)
FROM customers
WHERE country = 'USA'
GROUP BY state;

--8
SELECT InvoiceId, SUM(Quantity) AS Cantidad
FROM invoice_items
WHERE InvoiceId = '37';

--9
SELECT composer, COUNT(TrackId)
FROM tracks
WHERE composer = 'AC/DC';

--10
SELECT InvoiceId, SUM(Quantity) AS Cantidad
FROM invoice_items
GROUP BY InvoiceId
ORDER BY Cantidad DESC;

--11
SELECT COUNT(InvoiceId), BillingCountry
FROM invoices
GROUP BY BillingCountry;

--12
SELECT
strftime("%Y", invoicedate) AS Año, COUNT(invoiceid)
FROM invoices
WHERE Año IN ("2009","2011")
GROUP BY 1;

--13
SELECT strftime("%Y", invoicedate) AS Año, COUNT(InvoiceId)
FROM invoices
WHERE Año BETWEEN '2009' AND '2011';

--14
SELECT COUNT(CustomerId), Country
FROM customers
WHERE Country IN ('Spain','Brazil')
GROUP BY Country;

--15
SELECT Name
FROM tracks
WHERE Name LIKE 'You%';

-- PARTE 2 --

--1
SELECT customers.CustomerId, invoices.InvoiceId, invoices.InvoiceDate, invoices.BillingCountry
FROM customers
        INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId
WHERE Country = 'Brazil';

--2
SELECT invoices.InvoiceId, E.EmployeeId, E.FirstName || " " || E.LastName AS Nombre_Completo
FROM invoices
        INNER JOIN customers AS C ON invoices.CustomerId = C.CustomerId
        INNER JOIN employees AS E ON C.SupportRepId = E.EmployeeId;
        
--3
SELECT C.FirstName || " " || C.LastName AS Nombre, C.Country, E.FirstName || " " || E.LastName AS Nombre_Agente, total
FROM invoices
         INNER JOIN customers AS C ON invoices.CustomerId = C.CustomerId
         INNER JOIN employees AS E ON C.SupportRepId = E.EmployeeId
GROUP BY Nombre, C.Country, Nombre_Agente;

--4
SELECT ii.trackId, ii.invoiceid, tracks.name
FROM invoice_items AS ii
    INNER JOIN tracks ON ii.trackid = tracks.TrackId;
    
--5
SELECT t.name, t.mediatypeid, t.albumid, t.genreid
FROM tracks AS t
        INNER JOIN albums AS a ON t.albumid = a.albumid
        INNER JOIN genres AS g ON t.genreid = g.GenreId
        INNER JOIN media_types AS mt ON t.MediaTypeId = mt.MediaTypeId;
        
--6
SELECT pt.PlaylistId, p.name, COUNT(pt.TrackId) AS Count
FROM playlist_track AS pt
    INNER JOIN playlists AS p ON pt.PlaylistId = p.PlaylistId
GROUP BY pt.PlaylistId;

--7
SELECT e.firstname || " " || e.lastname AS Nombre_empleado, SUM(i.total)
FROM invoices i
        INNER JOIN customers c ON i.customerid = c.customerid
        INNER JOIN employees e ON c.supportrepid = e.employeeid
GROUP BY 1
ORDER BY 2 DESC;

--8
SELECT e.firstname || " " || e.lastname AS Nombre_empleado, SUM(i.total)
FROM invoices i
        INNER JOIN customers c ON i.customerid = c.customerid
        INNER JOIN employees e ON c.supportrepid = e.employeeid
WHERE strftime("%Y", i.invoicedate) = "2009"
GROUP BY 1
ORDER BY 2 DESC;

--9
SELECT ar.artistid, ar.Name as Nombre_artista, SUM(i.total) AS Ventas_totales
FROM invoices i
        INNER JOIN invoice_items ii ON i.invoiceid = ii.invoiceid
        INNER JOIN tracks t ON ii.trackid = t.trackid
        INNER JOIN albums a ON t.albumid = a.albumid
        INNER JOIN artists ar ON a.artistid = ar.ArtistId
GROUP BY 1,2
ORDER BY 3 DESC;
