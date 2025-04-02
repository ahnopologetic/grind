# Write your MySQL query statement below
with stg as (
    select *, ROW_NUMBER() over (partition by customer_id order by order_date) rn, order_date = customer_pref_delivery_date is_immediate
    from delivery
)
select ROUND((sum(if(is_immediate, 1, 0)) / count(distinct customer_id)) * 100.0, 2) immediate_percentage
from stg
where rn = 1
