# Write your MySQL query statement below
with nc as (
    select num, count(1) cnt
    from MyNumbers
    group by 1
)
select num
from nc 
where cnt = 1
UNION ALL 
SELECT NULL
order by num desc
limit 1
