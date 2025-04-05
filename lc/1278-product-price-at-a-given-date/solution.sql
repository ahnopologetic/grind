-- select product_id, COALESCE(last_value(new_price) over (partition by product_id order by change_date), 10) price
-- from products
-- where change_date <= '2019-08-16'
-- group by 1

select distinct product_id, 10 price
from products
group by 1
having min(change_date) > '2019-08-16'
union
select product_id, new_price price
from products
where (product_id, change_date) in (
    select product_id, max(change_date)
    from products
    where change_date <= '2019-08-16'
    group by 1
)
