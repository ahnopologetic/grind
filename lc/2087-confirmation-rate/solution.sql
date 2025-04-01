# Write your MySQL query statement below
with stg as (
    select s.*, c.time_stamp as confirm_at, c.action
    from signups s
    left join confirmations c using (user_id)
)
, stg_2 as (
select 
    user_id
    , SUM(CASE WHEN action = "confirmed" THEN 1 ELSE 0 END) confirm_count
    , SUM(1) attempt_count
from stg
group by 1
)

select user_id, round(confirm_count / attempt_count, 2) confirmation_rate
from stg_2
group by 1
order by 2
