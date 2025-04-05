select 
    'Low Salary' category
    , SUM(IF(income < 20000, 1, 0)) accounts_count
from accounts
union
select
    'Average Salary' category
    , SUM(IF(income >= 20000 and income <= 50000, 1, 0)) accounts_count
from accounts
union
select
    'High Salary' category
    , SUM(IF(income > 50000, 1, 0)) accounts_count
from accounts
