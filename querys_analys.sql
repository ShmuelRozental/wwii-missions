--query 1
SELECT city, COUNT(*) AS active_missions
FROM missions
WHERE EXTRACT(YEAR FROM mission_date) = :year
GROUP BY city;


--query 2
SELECT country, AVG(bomb_damage_assessment) AS average_damage
FROM missions
WHERE aircraft_count > 5
GROUP BY country;


EXPLAIN ANALYZE
SELECT city, COUNT(*) AS active_missions
FROM missions
WHERE EXTRACT(YEAR FROM mission_date) = :year
GROUP BY city;


# CREATE INDEX IF NOT EXISTS idx_target_type ON target_details (target_type);
# CREATE INDEX IF NOT EXISTS idx_target_industry ON target_details (target_industry);
# CREATE INDEX IF NOT EXISTS idx_location_id ON target_details (location_id);
# CREATE INDEX IF NOT EXISTS idx_coordinates_id ON target_details (coordinates_id);
#
 EXPLAIN ANALYZE SELECT * FROM target_details WHERE target_id = 1;