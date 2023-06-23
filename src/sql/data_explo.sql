SELECT Area, [Average Price]
FROM dbo.all_home_type$
WHERE [Average Price] = (SELECT MAX([Average Price]) FROM dbo.all_home_type$)

SELECT Area, [Average Price]
FROM dbo.all_home_type$

SELECT MIN([Average Price])
FROM dbo.all_home_type$
