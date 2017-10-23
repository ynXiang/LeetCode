# Write your MySQL query statement below
select Temp.question_id as survey_log
from (select Temp1.question_id, Temp2.answered / Temp1.total as ratio
     from (select S1.question_id, count(*) as total
          from survey_log S1
          group by S1.question_id) as Temp1,
          (select S2.question_id, count(*) as answered
                from survey_log S2
                where action = 'answer'
                group by S2.question_id) as Temp2
     where Temp1.question_id = Temp2.question_id) as Temp
order by Temp.ratio desc
limit 1
