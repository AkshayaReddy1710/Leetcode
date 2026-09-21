select e.name
from employee as e join
employee as m
on e.id = m.managerid
group by e.id
having count(m.managerid) >= 5