/* Write your T-SQL query statement below */
Select distinct author_id as id from Views
where author_id = viewer_id
order by 1 asc