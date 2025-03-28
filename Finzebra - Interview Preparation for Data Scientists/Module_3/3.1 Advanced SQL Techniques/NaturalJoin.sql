SELECT 
    employee_id,
    employee_name,
    department_name
FROM 
    employees
NATURAL JOIN 
    departments;