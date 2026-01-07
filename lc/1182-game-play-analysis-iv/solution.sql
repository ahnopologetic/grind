-- Write your PostgreSQL query statement below
with prev as (
    select *
        , lag(event_date) over (partition by player_id order by event_date) prev_event_date
        , row_number() over (partition by player_id order by event_date) rn
    from activity
)
, consec as (
    select *
        , event_date - prev_event_date = 1 is_consec
    from prev
)

select 
    round((count(distinct player_id) filter (where is_consec is true and rn = 2))::decimal / count(distinct player_id), 2) fraction
from consec


