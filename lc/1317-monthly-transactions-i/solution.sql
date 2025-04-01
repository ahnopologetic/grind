# Write your MySQL query statement below
SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') month,
    country
    , count(1) trans_count
    , sum(if(state = 'approved', 1, 0)) approved_count
    , sum(amount) trans_total_amount
    , sum(if(state = 'approved', amount, 0)) approved_total_amount
    from transactions 
group by 1, 2
