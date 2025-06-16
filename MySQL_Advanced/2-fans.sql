-- Query to to rank country origins by total number of (non-unique) fans

SELECT
  bands.origin AS origin,
  COUNT(fans.id) AS nb_fans
FROM
  bands
JOIN
  fans ON fans.band_id = bands.id
GROUP BY
  bands.origin
ORDER BY
  nb_fans DESC;