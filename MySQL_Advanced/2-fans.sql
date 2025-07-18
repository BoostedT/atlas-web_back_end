-- Query to to rank country origins by total number of (non-unique) fans

SELECT
  origin,
  SUM(fans) AS nb_fans
FROM
  metal_bands
GROUP BY
  origin
ORDER BY
  nb_fans DESC;