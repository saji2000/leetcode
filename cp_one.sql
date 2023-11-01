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

SELECT *
FROM EMPLOYEE
WHERE DEPARTMENT_ID = 10 AND SALARY > 3500

SELECT EMPLOYEE_ID, LAST_NAME  
FROM EMPLOYEE
ORDER BY SALARY DESC

SELECT DEPARTMENT_ID, COUNT(*) 
FROM EMPLOYEE
GROUP BY DEPARTMENT_ID
HAVING COUNT(*) >= 3

SELECT EMPLOYEE_ID, LAST_NAME
FROM EMPLOYEE
WHERE SALARY = (SELECT MAX(SALARY) FROM EMPLOYEE)

SELECT *
FROM EMPLOYEE AS E, DEPARTMENT AS D
WHERE D.NAME = 'SALES' AND D.DEPARTMENT_ID = E.DEPARTMENT_ID

SELECT *  
FROM EMPLOYEE 
WHERE DEPARTMENT_ID IN (SELECT DEPARTMENT_ID FROM DEPARTMENT WHERE NAME='SALES')

SELECT *
FROM EMPLOYEE AS E, DEPARTMENT AS D, LOCATION_ID AS L  
WHERE L.REGIONAL_GROUP = 'NEW YORK' AND D.LOCATION_ID = L.LOCATION_ID AND E.DEPARTMENT_ID = D.DEPARTMENT_ID

UPDATE EMPLOYEE
SET SALARY = SALARY * (10/100) WHERE JOB_ID = (SELECT JOB_ID FROM JOB WHERE FUNCTION = 'Manager')

DELETE 
FROM EMPLOYEE  
WHERE DEPARTMENT_ID = (SELECT DEPARTMENT_ID FROM DEPARTMENT WHERE NAME='ACCOUNTING')

SELECT MAX(SALARY) 
FROM EMPLOYEE

SELECT MAX(SALARY) 
FROM EMPLOYEE
WHERE SALARY < (SELECT MAX(SALARY) FROM EMPLOYEE)

SELECT SALARY 
FROM (SELECT SALARY FROM EMPLOYEE ORDER BY SALARY DESC LIMIT 2) AS EMP 
ORDER BY SALARY ASC LIMIT 1

SELECT SALARY 
FROM EMPLOYEE 
ORDER BY SALARY DESC 
LIMIT 1 OFFSET 1


SELECT SALARY 
FROM (SELECT SALARY FROM EMPLOYEE ORDER BY SALARY DESC LIMIT N) AS EMP 
ORDER BY SALARY ASC LIMIT 1


SELECT SALARY 
FROM EMPLOYEE 
ORDER BY SALARY DESC 
LIMIT 1 OFFSET N

SELECT *
FROM EMPLOYEE E1
WHERE N-1 = (SELECT DISTINCT(SALARY) FROM EMPLOYEE E2 WHERE E2.SALARY > E1.SALARY)


