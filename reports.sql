-- Customer Data Reporting Queries

-- 1. View all valid customers
SELECT * FROM ValidCustomers;

-- 2. View all flagged/invalid records and why they might be flagged
SELECT CustomerID, FullName, Email, IsDuplicate, HasValidEmail, HasMissingName 
FROM FlaggedCustomers;

-- 3. Count customers by Account Status
SELECT AccountStatus, COUNT(*) as TotalCustomers
FROM ValidCustomers
GROUP BY AccountStatus
ORDER BY TotalCustomers DESC;

-- 4. Find all Active customers who joined in the last year
SELECT FullName, Email, JoinDate 
FROM ValidCustomers
WHERE AccountStatus = 'Active' 
ORDER BY JoinDate DESC;
