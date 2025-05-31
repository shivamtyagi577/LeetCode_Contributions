-- Write your PostgreSQL query statement below
SELECT *,
    CASE 
        WHEN GREATEST(x, y, z) < (x + y + z - GREATEST(x, y, z)) THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle;