# Write your MySQL query statement below
SELECT SUM(I.TIV_2016) AS TIV_2016
FROM insurance I
WHERE I.TIV_2015 IN (SELECT I1.TIV_2015
                        FROM insurance I1
                        GROUP BY I1.TIV_2015
                        HAVING COUNT(*) > 1)
      AND (I.LAT, I.LON) IN (SELECT I2.LAT, I2.LON
                              FROM insurance I2
                              GROUP BY I2.LAT, I2.LON
                              HAVING COUNT(*) = 1)
