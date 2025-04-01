# Write your MySQL query statement below
WITH stg as (
    select managerId, count(1) `count`
    from employee
    group by 1
)

select name
from employee
where id in (
    select managerId
    from stg
    where `count` >= 5
)

