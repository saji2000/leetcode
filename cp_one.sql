SELECT EmpId, Name
FROM EMPLOYEE
WHERE ManagerId = 986

SELECT DISTINCT(Project)
FROM Salary

SELECT COUNT(*) 
FROM Salary
WHERE Project = 'P1'

SELECT MAX(Salary), MIN(Salary), AVG(Salary) FROM Salary

SELECT EmpId
FROM Salary
WHERE Salary >= 3000 AND Salary <= 4000

SELECT *
FROM Employee
WHERE ManagerId = 986 AND City = 'Chennai'

SELECT *
FROM Employee
WHERE ManagerId = 321 OR City = 'Chennai'

SELECT *
FROM Salary
WHERE Project != 'P1'

SELECT EmpId, Salary + Variable as TotalSalary
FROM Salary

SELECT EmpId 
FROM Employee
WHERE Name LIKE '__vi%'

SELECT EmpId 
FROM EMPLOYEE
WHERE COMM is NULL