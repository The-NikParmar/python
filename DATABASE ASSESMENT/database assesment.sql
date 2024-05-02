-- Create the Banking database and switch to it
CREATE DATABASE Banking;
USE Banking;

-- Create the Bank table to store bank branch details
CREATE TABLE Bank (
    Branch_id INT PRIMARY KEY,
    Branch_name VARCHAR(30),
    Branch_city VARCHAR(20)
);

-- Create the Loan_table to store loan details
CREATE TABLE Loan_table (
    Loan_no INT PRIMARY KEY,
    Loan_amount INT,
    Loan_type VARCHAR(20),
    Branch_id INT,
    account_holders_id INT
);

-- Create the Account_holder table to store account holder information
CREATE TABLE Account_holder (
    account_holders_id INT PRIMARY KEY,
    account_holders_name VARCHAR(20),
    City TEXT,
    Contact VARCHAR(10),
    Date_of_account_created DATE,
    Account_status VARCHAR(10),
    Account_type VARCHAR(20),
    Balance INT
);

-- Modify Loan_no to be primary key in Loan_table
ALTER TABLE Loan_table MODIFY Loan_no INT PRIMARY KEY;

-- Insert data into the Bank table
INSERT INTO Bank (Branch_id, Branch_name, Branch_city) VALUES
(101, "BOB", "Ahmedabad"),
(102, "SBI", "Baroda"),
(103, "Axis Bank", "Nadiyad"),
(104, "SBI", "Amreli"),
(105, "Kotak Mahindra Bank", "Bhavnagar");

-- Insert data into the Loan_table
INSERT INTO Loan_table (Loan_no, Loan_amount, Loan_type, Branch_id, account_holders_id) VALUES
(10, 100000, 'Student Loan', 101, 1),
(20, 100000, 'Home Equity Loan', 102, 2),
(30, 50000, 'Auto Loan', 102, 2),
(40, 650000, 'Personal Loan', 103, 3),
(50, 350000, 'Small Business Loan', 104, 3);

-- Insert data into the Account_holder table
INSERT INTO Account_holder (account_holders_id, account_holders_name, City, Contact, Date_of_account_created, Account_status, Account_type, Balance) VALUES
(1, "MIHIR", "Ahmedabad", "9506510346", '2013-05-15', "Active", "Savings", 50000),
(2, "ASHISH", "Surat", "9865243687", '2013-04-14', "Terminated", "Current", 60000),
(3, "MOHIT", "Rajkot", "9998676647", '2013-05-02', "Active", "Fixed Deposite", 80000),
(4, "RAJ", "Ahmedabad", "6359452317", '2013-05-15', "Active", "Recurring Deposite", 30000),
(5, "SMIT", "Surat", "9106523346", '2013-05-20', "Terminated", "Savings", 80000);

-- Start a transaction for intra bank transfer
START TRANSACTION;

-- Deduct $100 from account A and add $100 to account B
UPDATE Account_holder
SET Balance = CASE account_holders_id
                WHEN 1 THEN Balance - 100
                WHEN 4 THEN Balance + 100
             END
WHERE account_holders_id IN (1, 4);

-- Commit the transaction
COMMIT;

-- Fetch account holders from Surat and Ahmedabad cities
SELECT *
FROM Account_holder
WHERE City IN ("Surat", "Ahmedabad");

-- Fetch account number and account holder name for accounts created after 15th of any month
SELECT account_holders_id, account_holders_name
FROM Account_holder
WHERE DAY(Date_of_account_created) > 15;

-- Display city name and count the branches in that city
SELECT Branch_city, COUNT(*) AS Count_Branch
FROM Bank
GROUP BY Branch_city;

-- Display account holder’s id, name, branch id, and loan amount for people who have taken loans
SELECT ah.account_holders_id, ah.account_holders_name, lt.Branch_id, lt.Loan_amount
FROM Account_holder ah
JOIN Loan_table lt ON ah.account_holders_id = lt.account_holders_id;
