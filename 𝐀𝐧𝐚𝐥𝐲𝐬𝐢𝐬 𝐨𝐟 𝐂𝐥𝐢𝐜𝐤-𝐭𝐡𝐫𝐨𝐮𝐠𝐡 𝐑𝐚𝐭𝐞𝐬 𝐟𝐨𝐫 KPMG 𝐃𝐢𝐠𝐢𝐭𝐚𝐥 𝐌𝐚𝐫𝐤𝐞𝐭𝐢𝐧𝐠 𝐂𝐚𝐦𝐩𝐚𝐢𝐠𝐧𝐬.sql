CREATE TABLE #ad_clicks (
    ad_id INT PRIMARY KEY,
    user_id INT,
    click_date smalldatetime,
    platform VARCHAR(50)
);

CREATE TABLE #service_enquiries (
    enquiry_id INT PRIMARY KEY,
    user_id INT,
    enquiry_date smalldatetime
);

INSERT INTO #ad_clicks (ad_id, user_id, click_date, platform) VALUES
(111, 2450, '2022-08-15', 'Google'),
(892, 2658, '2022-08-18', 'Facebook'),
(437, 4800, '2022-08-20', 'LinkedIn'),
(598, 3200, '2022-07-15', 'Google'),
(320, 1700, '2022-07-14', 'LinkedIn');

INSERT INTO #service_enquiries (enquiry_id, user_id, enquiry_date) VALUES
(71, 2450, '2022-08-16 '),
(802, 3200, '2022-07-16 '),
(493, 1550, '2022-06-30 '),
(12, 6700, '2022-07-02 '),
(117, 9800, '2022-05-25 ');

Select * from #ad_clicks
Select * from #service_enquiries

/* Solution 1*/
;WITH clicks AS (
    SELECT platform, COUNT(DISTINCT user_id) AS total_clicks
    FROM #ad_clicks
    GROUP BY platform
),
enquiries AS (
    SELECT ac.platform, COUNT(DISTINCT se.user_id) AS total_enquiries
    FROM #ad_clicks ac
    JOIN #service_enquiries se ON ac.user_id = se.user_id
    GROUP BY ac.platform
)
SELECT 
    c.platform,
    c.total_clicks,
    e.total_enquiries,
    (CAST(e.total_enquiries as FLOAT) / c.total_clicks) AS enquiry_proportion
FROM clicks c
LEFT JOIN enquiries e ON c.platform = e.platform;

/* Solution 2*/
SELECT 
    ac.platform,
    COUNT(DISTINCT ac.user_id) AS total_clicks,
    COUNT(DISTINCT se.user_id) AS total_enquiries,
    (CAST(COUNT(DISTINCT se.user_id) AS FLOAT) / COUNT(DISTINCT ac.user_id)) AS enquiry_proportion
FROM #ad_clicks ac
LEFT JOIN service_enquiries se ON ac.user_id = se.user_id
GROUP BY ac.platform;

Drop table #ad_clicks
Drop Table #service_enquiries
