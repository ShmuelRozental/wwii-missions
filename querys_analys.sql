--query 1
WITH active_air_forces AS (
    SELECT
        m.air_force,
        l.city,
        COUNT(m.mission_id) AS active_missions
    FROM mission m
    JOIN target_details t ON m.target_id = t.target_id
    JOIN location l ON t.location_id = l.location_id
    WHERE EXTRACT(YEAR FROM m.mission_date) = 1944
    GROUP BY m.air_force, l.city
)

SELECT
    air_force,
    city,
    active_missions
FROM active_air_forces
ORDER BY active_missions DESC;




SELECT
    m.country,
    AVG(CAST(m.bomb_damage_assessment AS NUMERIC)) AS average_damage
FROM mission m
WHERE m.airborne_aircraft > 1
AND m.bomb_damage_assessment IS NOT NULL
AND m.bomb_damage_assessment ~ '^[0-9]+(\.[0-9]+)?$'
GROUP BY m.country;



CREATE INDEX idx_mission_date ON mission (mission_date);
CREATE INDEX idx_target_id ON target_details (target_id);
CREATE INDEX idx_location_id ON location (location_id);


EXPLAIN
WITH active_air_forces AS (
    SELECT
        m.air_force,
        l.city,
        COUNT(m.mission_id) AS active_missions
    FROM mission m
    JOIN target_details t ON m.target_id = t.target_id
    JOIN location l ON t.location_id = l.location_id
    WHERE EXTRACT(YEAR FROM m.mission_date) = 1944
    GROUP BY m.air_force, l.city
)
SELECT
    air_force,
    city,
    active_missions
FROM active_air_forces
ORDER BY active_missions DESC;


EXPLAIN ANALYZE
WITH active_air_forces AS (
    SELECT
        m.air_force,
        l.city,
        COUNT(m.mission_id) AS active_missions
    FROM mission m
    JOIN target_details t ON m.target_id = t.target_id
    JOIN location l ON t.location_id = l.location_id
    WHERE EXTRACT(YEAR FROM m.mission_date) = 1944
    GROUP BY m.air_force, l.city
)
SELECT
    air_force,
    city,
    active_missions
FROM active_air_forces
ORDER BY active_missions DESC;





