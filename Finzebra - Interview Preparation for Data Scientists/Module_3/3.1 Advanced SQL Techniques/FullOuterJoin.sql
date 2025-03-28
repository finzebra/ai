SELECT 
    e.employee_name,
    p.project_name
FROM 
    employees e
FULL OUTER JOIN 
    projects p ON e.employee_id = p.lead_employee_id;