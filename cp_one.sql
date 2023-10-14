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