# Write your MySQL query statement below
with stg as (

select *
    , SUM(weight) over (order by turn) cum_weight
from queue 
)
select person_name
from stg
where cum_weight <= 1000
order by cum_weight desc
limit 1
