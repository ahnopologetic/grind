# Write your MySQL query statement below
select customer_id
from customer c
group by 1
-- left join product p on c.product_key = p.product_key
having count(distinct c.product_key) = (select count(1) from product)
