create database product;

use product;

# create table product
CREATE TABLE `product`.`product` (
  `pro_od` INT NOT NULL AUTO_INCREMENT,
  `pro_name` VARCHAR(45) NULL,
  `pro_price` INT NULL,
  `pro_com` INT NULL,
  PRIMARY KEY (`pro_od`))
COMMENT = '			';

# insert data into product

INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('101', 'mother board', '3200', '15');
INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('102', 'key board', '450', '16');
INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('103', 'zip drive', '250', '14');
INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('104', 'speakar', '550', '16');
INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('105', 'monitor', '5000', '11');
INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('106', 'dvd', '900', '12');
INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('107', 'cd drive', '800', '12');
INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('108', 'printer ', '2600', '13');
INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('109', 'refile ', '350', '13');
INSERT INTO `product`.`product` (`pro_od`, `pro_name`, `pro_price`, `pro_com`) VALUES ('110', 'mouse', '250', '12');

/*
From the following table, write a SQL query to select a range of
products whose price is in the range Rs.200 to Rs.600. Begin and end
values are included. Return pro_id, pro_name, pro_price, and pro_com.*/

SELECT pro_od, pro_name, pro_price, pro_com
FROM product.product
WHERE pro_price BETWEEN 200 AND 600;

/*
21. From the following table, write a SQL query to calculate the average
price for a manufacturer code of 16. Return avg.
*/

SELECT AVG(pro_price) AS avg_price
FROM product.product
WHERE pro_com = 16;

/*
22. From the following table, write a SQL query to display the pro_name
as 'Item Name' and pro_priceas 'Price in Rs.'
*/

SELECT pro_name AS 'Item Name', pro_price AS 'Price in Rs.'
FROM product.product;


/*
23. From the following table, write a SQL query to find the items whose
prices are higher than or equal to $250. Order the result by product price in
descending*/

SELECT pro_name, pro_price
FROM product.product
WHERE pro_price >= 250
ORDER BY pro_price DESC;

/*
24. From the following table, write a SQL query to calculate average
price of the items for each company. Return average price and company
code.*/

SELECT pro_com AS company_code, AVG(pro_price) AS avg_price
FROM product.product
GROUP BY pro_com;



