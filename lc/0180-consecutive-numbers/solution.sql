# Write your MySQL query statement below
with stg as (
select * 
    , lag(num, 1) over () last_num
    , lag(num, 2) over () second_to_last_num
from logs 
)

select 
    num ConsecutiveNums
    -- *
from stg
where num = last_num and num = second_to_last_num and last_num = second_to_last_num
group by 1

