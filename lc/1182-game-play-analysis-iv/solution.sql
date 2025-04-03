select ROUND(count(distinct player_id) / (select count(distinct player_id) from activity), 2) fraction
from activity
where (player_id, DATE_SUB(event_date, interval 1 day)) in (
    select player_id, min(event_date) as first_login
    from activity 
    group by 1
)
