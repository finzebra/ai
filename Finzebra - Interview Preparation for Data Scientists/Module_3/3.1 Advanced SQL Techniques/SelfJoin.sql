SELECT 
    e1.employee_name AS employee,
    e2.employee_name AS manager
FROM 
    employees e1
LEFT JOIN 
    employees e2 ON e1.manager_id = e2.employee_id;