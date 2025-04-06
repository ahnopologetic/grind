# Write your MySQL query statement below
with users as (
    select name, RANK() over (order by count(1)) rnk
    from movierating
    left join users using (user_id)
    group by 1
    order by 2 desc, 1
    limit 1
)
, movies as (
    select title, avg(rating)
    from movierating
    left join movies using (movie_id)
    where created_at between '2020-02-01' and '2020-02-29'
    group by 1
    order by 2 desc, 1
    limit 1
)

select name results
from users
union all
select title results
from movies

