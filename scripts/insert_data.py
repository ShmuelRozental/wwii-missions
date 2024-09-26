from db.connection import get_db_connection, close_db_connection
from scripts.fetch_denormalized_data import fetch_denormalized_data

def insert_normalized_data(denormalized_data):
    connection = get_db_connection()
    cursor = connection.cursor()
    i =0

    try:
        for mission in denormalized_data:
            cursor.execute("""
                SELECT location_id FROM location 
                WHERE country = %s AND city = %s;
            """, (mission['target_country'], mission['target_city']))
            location_result = cursor.fetchone()

            if location_result:
                location_id = location_result[0]  # Location exists, get the ID
            else:
                cursor.execute("""
                    INSERT INTO location (country, city) 
                    VALUES (%s, %s) RETURNING location_id;
                """, (mission['target_country'], mission['target_city']))
                location_id = cursor.fetchone()[0]


            cursor.execute("""
                SELECT coordinates_id FROM coordinates 
                WHERE latitude = %s AND longitude = %s;
            """, (mission['target_latitude'], mission['target_longitude']))
            coordinates_result = cursor.fetchone()

            if coordinates_result:
                coordinates_id = coordinates_result[0]  # Coordinates exist, get the ID
            else:
                cursor.execute("""
                    INSERT INTO coordinates (latitude, longitude) 
                    VALUES (%s, %s) RETURNING coordinates_id;
                """, (mission['target_latitude'], mission['target_longitude']))
                coordinates_id = cursor.fetchone()[0]

            cursor.execute("""
                SELECT target_id FROM target_details 
                WHERE location_id = %s AND coordinates_id = %s;
            """, (location_id, coordinates_id))
            target_details_result = cursor.fetchone()

            if target_details_result:
                target_id = target_details_result[0]
            else:
                cursor.execute("""
                    INSERT INTO target_details (target_type, target_industry, target_priority, location_id, coordinates_id)
                    VALUES (%s, %s, %s, %s, %s) RETURNING target_id;
                """, (mission['target_type'], mission['target_industry'], mission['target_priority'], location_id,
                      coordinates_id))
                target_id = cursor.fetchone()[0]


            cursor.execute("""
                UPDATE mission
                SET target_id = %s
                WHERE mission_id = %s;
            """, (target_id, mission['mission_id']))


        connection.commit()
        print("Data normalized and inserted successfully!")

        cursor.execute("""
                       ALTER TABLE mission
                           DROP COLUMN IF EXISTS target_country,
                           DROP COLUMN IF EXISTS target_city,
                           DROP COLUMN IF EXISTS target_latitude,
                           DROP COLUMN IF EXISTS target_longitude, 
                           DROP COLUMN IF EXISTS target_type,
                           DROP COLUMN IF EXISTS target_industry,
                           DROP COLUMN IF EXISTS target_priority;
                   """)

    except Exception as e:
        print(f"An error occurred while inserting normalized data: {e}")
        connection.rollback()

    finally:
        cursor.close()
        close_db_connection(connection)

if __name__ == "__main__":
    denormalized_data = fetch_denormalized_data()
    if denormalized_data:
        insert_normalized_data(denormalized_data)
    else:
        print("No data found in the mission table.")