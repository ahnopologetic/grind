# Write your MySQL query statement below
with stg as (

select 
    requester_id id
    , count(1) num
from requestAccepted
group by 1
union all
select
    accepter_id id
    , count(1) num
from requestAccepted
group by 1
)
select 
    id
    , sum(num) num
from stg
group by 1
order by 2 desc
limit 1
