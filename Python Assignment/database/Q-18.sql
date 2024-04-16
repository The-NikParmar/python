/* 18. Write a SQL statement that displays all the information about all
salespeople*/

create database saling;

CREATE TABLE `saling`.`sales_pepole` (
  `salesman_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `commission` INT NULL,
  PRIMARY KEY (`salesman_id`));

# insert data into sale_pepole

INSERT INTO `saling`.`sales_pepole` (`salesman_id`, `name`, `city`, `commission`) VALUES ('5001', 'james hoog', 'new york', '0.15');
INSERT INTO `saling`.`sales_pepole` (`salesman_id`, `name`, `city`, `commission`) VALUES ('5002', 'nail knite ', 'paris', '0.13');
INSERT INTO `saling`.`sales_pepole` (`salesman_id`, `name`, `city`, `commission`) VALUES ('5005', 'pit alex', 'london', '0.11');
INSERT INTO `saling`.`sales_pepole` (`salesman_id`, `name`, `city`, `commission`) VALUES ('5006', 'mc lyon ', 'paris', '0.14');
INSERT INTO `saling`.`sales_pepole` (`salesman_id`, `name`, `city`, `commission`) VALUES ('5007', 'paul adam ', 'rome', '0.13');
INSERT INTO `saling`.`sales_pepole` (`salesman_id`, `name`, `city`, `commission`) VALUES ('5003', 'lauson hen ', 'san jose ', '0.12');

#customer table
CREATE TABLE `saling`.`customer` (
  `customer_od` INT NOT NULL AUTO_INCREMENT,
  `ord_no` INT NULL,
  `purch_amt` INT NULL,
  `ord_date` DATE NULL,
  `salesman_id` INT NULL,
  PRIMARY KEY (`customer_od`),
  INDEX `salesman_id_idx` (`salesman_id` ASC) VISIBLE,
  CONSTRAINT `salesman_id`
    FOREIGN KEY (`salesman_id`)
    REFERENCES `saling`.`sales_pepole` (`salesman_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
    
# insert into customer
INSERT INTO `saling`.`customer` (`customer_od`, `ord_no`, `purch_amt`, `ord_date`, `salesman_id`) VALUES ('3005', '70001', '150.5', '2012-10-05', '5002');
INSERT INTO `saling`.`customer` (`customer_od`, `ord_no`, `purch_amt`, `ord_date`, `salesman_id`) VALUES ('3001', '70009', '270.65', '2012-09-10', '5005');
INSERT INTO `saling`.`customer` (`customer_od`, `ord_no`, `purch_amt`, `ord_date`, `salesman_id`) VALUES ('3002', '70002', '65.26', '2012-10-05', '5001');
INSERT INTO `saling`.`customer` (`customer_od`, `ord_no`, `purch_amt`, `ord_date`, `salesman_id`) VALUES ('3009', '70004', '110.5', '2012-08-07', '5003');
INSERT INTO `saling`.`customer` (`customer_od`, `ord_no`, `purch_amt`, `ord_date`, `salesman_id`) VALUES ('3006', '70007', '948.5', '2012-09-10', '5002');


/*19. From the following table, write a SQL query to find orders that are
delivered by a salesperson with ID. 5001. Return ord_no, ord_date,
purch_amt.*/

SELECT ord_no, ord_date, purch_amt
FROM saling.customer c
JOIN saling.sales_pepole s ON c.salesman_id = s.salesman_id
WHERE s.salesman_id = 5001;


