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
