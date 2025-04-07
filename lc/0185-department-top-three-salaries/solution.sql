# Write your MySQL query statement below
with stg as (
    select 
        d.name Department
        , e.name Employee
        , e.salary Salary
        , dense_rank() over (partition by departmentId order by salary desc) rnk
    from employee e
    left join department  d on e.departmentId = d.id
    )
select Department, Employee, Salary
from stg
where rnk <= 3
