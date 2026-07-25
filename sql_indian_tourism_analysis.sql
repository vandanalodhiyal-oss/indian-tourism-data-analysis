CREATE DATABASE Indian_Tourism;
USE Indian_Tourism;

SHOW TABLES;
SELECT * FROM `general data 2014-2020`;

SELECT year, noftaii
FROM `general data 2014-2020`
ORDER BY noftaii DESC;

SELECT year, noftaii
FROM `general data 2014-2020`
ORDER BY noftaii ASC;

SELECT AVG(noftaii) AS Average_Foreign_Tourists
FROM `general data 2014-2020`;
