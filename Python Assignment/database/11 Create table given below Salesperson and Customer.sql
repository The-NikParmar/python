create database sc;

use sc;

CREATE TABLE `sc`.`sales_person` (
  `s_no` INT NOT NULL AUTO_INCREMENT,
  `sname` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `comm` VARCHAR(45) NULL,
  PRIMARY KEY (`s_no`));
  
# data insert into salse_person
INSERT INTO `sc`.`sales_person` (`s_no`, `sname`, `city`, `comm`) VALUES ('10001', 'Peel', 'London', '.12');
INSERT INTO `sc`.`sales_person` (`s_no`, `sname`, `city`, `comm`) VALUES ('10002', 'serres', 'san jose', '.13');
INSERT INTO `sc`.`sales_person` (`s_no`, `sname`, `city`, `comm`) VALUES ('10003', 'motika', 'london', '.11');
INSERT INTO `sc`.`sales_person` (`s_no`, `sname`, `city`, `comm`) VALUES ('10007', 'rafkin', 'barcelona', '.15');
INSERT INTO `sc`.`sales_person` (`s_no`, `sname`, `city`, `comm`) VALUES ('10003', 'axelrod', 'new york', '.1');

# create table customer

CREATE TABLE `sc`.`customer` (
  `customer_id` INT NOT NULL AUTO_INCREMENT,
  `cname` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `ratting` INT NULL,
  `s_no` INT NULL,
  PRIMARY KEY (`customer_id`),
  INDEX `s_no_idx` (`s_no` ASC) VISIBLE,
  CONSTRAINT `s_no`
    FOREIGN KEY (`s_no`)
    REFERENCES `sc`.`sales_person` (`s_no`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
COMMENT = '	';

# salses_person data insert
INSERT INTO `sc`.`customer` (`customer_id`, `cname`, `city`, `ratting`, `s_no`) VALUES ('201', 'hoffman', 'london', '100', '10001');
INSERT INTO `sc`.`sales_person` (`s_no`, `sname`, `city`, `comm`) VALUES ('10005', 'rafkin', 'barcelona', '.15');
UPDATE `sc`.`sales_person` SET `s_no` = '10004' WHERE (`s_no` = '10003');
INSERT INTO `sc`.`sales_person` (`s_no`, `sname`, `city`, `comm`) VALUES ('10007', 'axelrod', 'new york', '.1');

#customer data insert
INSERT INTO `sc`.`customer` (`customer_id`, `cname`, `city`, `ratting`, `s_no`) VALUES ('202', 'giovanne', 'roe', '200', '10004');
INSERT INTO `sc`.`customer` (`customer_id`, `cname`, `city`, `ratting`, `s_no`) VALUES ('203', 'liu', 'san jose', '300', '10002');
INSERT INTO `sc`.`customer` (`customer_id`, `cname`, `city`, `ratting`, `s_no`) VALUES ('204', 'grass', 'barcelona', '100', '10005');
INSERT INTO `sc`.`customer` (`customer_id`, `cname`, `city`, `ratting`, `s_no`) VALUES ('206', 'clemens', 'london', '300', '10007');

# Retrieve the below data from above table
SELECT customer_id, cname, city, ratting FROM sc.customer;

# 13 All orders for more than $1000.

SELECT *
FROM sc.customer
WHERE ratting > 1000;

/* 14.Names and cities of all salespeople in London with commission
above 0.1215.All salespeople either in Barcelona or in London*/

SELECT sname, city
FROM sc.sales_person
WHERE city = 'London' AND comm > 0.1215;

# 16.All salespeople with commission between 0.10 and 0.12. (Boundary valuesshould be excluded).
SELECT sname, city
FROM sc.sales_person
WHERE comm > 0.10 AND comm < 0.12;

# 17 All customers excluding those with rating <= 100 unless they are located inRome

SELECT *
FROM sc.customer
WHERE ratting > 100 OR city = 'Rome';






