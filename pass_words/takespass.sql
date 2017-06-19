select pass , count(*) as cp from passdata
where length(pass) >=4 and length(pass) <= 12
group by pass
order by cp desc