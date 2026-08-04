start transaction;

select InvoiceNO,
Trim(StockCode) as StockCode,
Trim(Description) as Description,
Trim(Country) as Country
from online_retail;

select stockcode,
case 
when StockCode = 'Null' then null
else trim(StockCode)
end as StockCode
from online_retail;


select Description,
case 
when Description = 'Null' then null
else trim(Description)
end as Description
from online_retail;

select Country,
case 
when Country = 'Null' then null
else trim(Country)
end as Country
from online_retail;

select CustomerID,
case 
when CustomerID = 'Null' then null
else trim(CustomerID)
end as CustomerID
from online_retail;

select InvoiceDate,
case 
when InvoiceDate = 'Null' then null
else trim(InvoiceDate)
end as InvoiceDate
from online_retail;

select *,
Row_number () over(
partition by StockCode,Country, Description, Quantity order by InvoiceDate)
as row_num
FROM
    online_retail;

SELECT *
FROM online_retail
WHERE InvoiceNo IS NULL
OR StockCode IS NULL
OR Description IS NULL
OR Quantity IS NULL
OR InvoiceDate IS NULL
OR UnitPrice IS NULL
OR CustomerID IS NULL
OR Country IS NULL;

UPDATE online_retail
SET Description = NULL
WHERE TRIM(Description)='';

UPDATE online_retail
SET InvoiceNo = TRIM(InvoiceNo),
    StockCode = TRIM(StockCode),
    Description = TRIM(Description),
    Country = TRIM(Country);
    
UPDATE online_retail
SET Country='UNITED KINGDOM'
WHERE UPPER(TRIM(Country))
IN ('UK','U.K.','UNITED KINGDOM');

UPDATE online_retail
SET Country='FRANCE'
WHERE UPPER(TRIM(Country))='FRANCE';

UPDATE online_retail
SET Country='GERMANY'
WHERE UPPER(TRIM(Country))='GERMANY';

UPDATE online_retail
SET Country='SPAIN'
WHERE UPPER(TRIM(Country))='SPAIN';

UPDATE online_retail
SET Country='IRELAND'
WHERE UPPER(TRIM(Country))
IN ('IRELAND','EIRE');

UPDATE online_retail
SET Country='NETHERLANDS'
WHERE UPPER(TRIM(Country))
IN ('NETHERLANDS','THE NETHERLANDS');

SELECT *
FROM online_retail
WHERE Quantity>500;

ALTER TABLE online_retail
ADD COLUMN InvoiceDate_New DATETIME;

SELECT *
FROM online_retail
WHERE CustomerID IS NULL;

SELECT
COUNT(*) AS TotalRows,
COUNT(DISTINCT InvoiceNo) AS TotalInvoices,
COUNT(DISTINCT CustomerID) AS Customers,
COUNT(DISTINCT StockCode) AS Products
FROM online_retail;

