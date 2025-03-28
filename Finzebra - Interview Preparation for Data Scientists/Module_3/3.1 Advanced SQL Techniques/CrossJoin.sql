SELECT 
    s.size_label,
    c.color_name
FROM 
    sizes s
CROSS JOIN 
    colors c;