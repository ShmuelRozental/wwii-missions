mission_table = """

CREATE TABLE IF NOT EXISTS mission (
    mission_id INTEGER PRIMARY KEY,
    mission_date DATE,
    theater_of_operations VARCHAR(100),
    country VARCHAR(100),
    air_force VARCHAR(100),
    unit_id VARCHAR(100),
    aircraft_series VARCHAR(100),
    callsign VARCHAR(100),
    mission_type VARCHAR(100),
    takeoff_base VARCHAR(255),
    takeoff_location VARCHAR(255),
    takeoff_latitude VARCHAR(15),
    takeoff_longitude NUMERIC(10, 6),
    target_id VARCHAR(100),
    target_country VARCHAR(100),
    target_city VARCHAR(100),
    target_type VARCHAR(100),
    target_industry VARCHAR(255),
    target_priority VARCHAR(5),
    target_latitude NUMERIC(10, 6),
    target_longitude NUMERIC(10, 6),
    altitude_hundreds_of_feet NUMERIC(7, 2),
    airborne_aircraft NUMERIC(4, 1),
    attacking_aircraft INTEGER,
    bombing_aircraft INTEGER,
    aircraft_returned INTEGER,
    aircraft_failed INTEGER,
    aircraft_damaged INTEGER,
    aircraft_lost INTEGER,
    high_explosives VARCHAR(255),
    high_explosives_type VARCHAR(255),
    high_explosives_weight_pounds VARCHAR(25),
    high_explosives_weight_tons NUMERIC(10, 2),
    incendiary_devices VARCHAR(255),
    incendiary_devices_type VARCHAR(255),
    incendiary_devices_weight_pounds NUMERIC(10, 2),
    incendiary_devices_weight_tons NUMERIC(10, 2),
    fragmentation_devices VARCHAR(255),
    fragmentation_devices_type VARCHAR(255),
    fragmentation_devices_weight_pounds NUMERIC(10, 2),
    fragmentation_devices_weight_tons NUMERIC(10, 2),
    total_weight_pounds NUMERIC(10, 2),
    total_weight_tons NUMERIC(10, 2),
    time_over_target VARCHAR(8),
    bomb_damage_assessment VARCHAR(255),
    source_id VARCHAR(100)
);
"""





target_table = """
CREATE TABLE IF NOT EXISTS target_details (
    target_id SERIAL PRIMARY KEY,              
    target_type VARCHAR(100),                  
    target_industry VARCHAR(255),         
    target_priority VARCHAR(5),                
    location_id INTEGER REFERENCES location(location_id),  
    coordinates_id INTEGER REFERENCES coordinates(coordinates_id)        
);
"""

location_table = """
CREATE TABLE IF NOT EXISTS location (
    location_id SERIAL PRIMARY KEY,  
    country VARCHAR(100),            
    city VARCHAR(100)               
);
"""

coordinate_table = """
CREATE TABLE IF NOT EXISTS coordinates (
    coordinates_id SERIAL PRIMARY KEY,  
    latitude NUMERIC(10, 6),          
    longitude NUMERIC(10, 6)         
);
"""


