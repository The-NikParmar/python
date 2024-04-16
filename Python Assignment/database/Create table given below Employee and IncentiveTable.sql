 create  database Employee;
 
 CREATE TABLE `employee`.`employee` (
  `employee_id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `salary` VARCHAR(45) NULL,
  `joining_date` DATETIME NULL,
  `deparment` VARCHAR(45) NULL,
  PRIMARY KEY (`employee_id`));

INSERT INTO `employee`.`employee` (`employee_id`, `first_name`, `last_name`, `salary`, `joining_date`, `deparment`) VALUES ('1', 'parmar', 'nikhil', '30000', '2023-4-22', 'banking');
INSERT INTO `employee`.`employee` (`employee_id`, `first_name`, `last_name`, `salary`, `joining_date`, `deparment`) VALUES ('2', 'chauhan', 'smit', '40000', '2024-5-15', 'insurance');
INSERT INTO `employee`.`employee` (`employee_id`, `first_name`, `last_name`, `salary`, `joining_date`, `deparment`) VALUES ('3', 'kurmi', 'purshottam', '50000', '2024-1-12', 'banking');
INSERT INTO `employee`.`employee` (`employee_id`, `first_name`, `last_name`, `salary`, `joining_date`) VALUES ('4', 'jain', 'mohit', '35000', '2020-3-23');
INSERT INTO `employee`.`employee` (`employee_id`, `first_name`, `last_name`, `salary`, `joining_date`, `deparment`) VALUES ('5', 'prajapati', 'ashish', '40000', '2022-6-23', 'services');
UPDATE `employee`.`employee` SET `deparment` = 'services' WHERE (`employee_id` = '4');


CREATE TABLE `employee`.`incentive` (
  `idIncentive` INT NOT NULL AUTO_INCREMENT,
  `Incentive_date` DATETIME NULL,
  `Incentive_amount` INT NULL,
  PRIMARY KEY (`idIncentive`),
  CONSTRAINT `employee_id`
    FOREIGN KEY (`idIncentive`)
    REFERENCES `employee`.`employee` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
COMMENT = '	';


INSERT INTO `employee`.`incentive` (`idIncentive`, `Incentive_date`, `Incentive_amount`, `employee_id`) VALUES ('1', '2022-3-1', '5000', '1');
INSERT INTO `employee`.`incentive` (`idIncentive`, `Incentive_date`, `Incentive_amount`, `employee_id`) VALUES ('2', '2020-3-2', '4500', '2');
INSERT INTO `employee`.`incentive` (`idIncentive`, `Incentive_date`, `Incentive_amount`, `employee_id`) VALUES ('3', '2021-3-2', '5500', '3');
use employee;
# 3. Get First_Name from employee table using Smit name “Employee Name”

SELECT first_name
FROM employee
WHERE last_name = 'smit';

# 4. Get FIRST_NAME, Joining Date, and Salary from employee table.

SELECT first_name, joining_date, salary
FROM employee;

# 5. Get all employee details from the employee table order by First_Name

SELECT *
FROM employee
ORDER BY first_name ASC, salary DESC;

# 6 .Get employee details from employee table whose first name contains ‘J’.

SELECT *
FROM employee
WHERE first_name LIKE '%J%';


/* 7. Select first_name, incentive amount from employee and incentives table
forthose employees who have incentives and incentive amount greater than
3000?*/

SELECT e.first_name, i.Incentive_amount
FROM employee e
JOIN incentive i ON e.employee_id = i.employee_id
WHERE i.Incentive_amount > 3000;










