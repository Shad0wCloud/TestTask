SELECT Author from Books where id = 
(select id from Stock where (Total-Available) = 
 (select max(Total-Available) from Stock))