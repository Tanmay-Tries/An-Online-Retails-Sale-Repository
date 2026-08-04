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
