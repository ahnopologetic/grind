# Write your MySQL query statement below
select 
    id
    , CASE
        WHEN id % 2 = 0 then LAG(student) over (order by id)
        ELSE COALESCE(LEAD(student) over (order by id), student)
    END student
from seat
