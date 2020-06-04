'''
https://leetcode.com/problems/not-boring-movies/submissions/
'''

select * 
from cinema c
where c.description NOT LIKE '%boring%'
and c.id & 1
order by c.rating desc
