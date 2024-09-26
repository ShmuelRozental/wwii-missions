from db.connection import get_db_connection, close_db_connection

def fetch_denormalized_data():
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            SELECT mission_id, target_type, target_industry, target_priority, target_country, target_city, target_latitude, target_longitude 
            FROM mission;
        """)
        rows = cursor.fetchall()

        denormalized_data = [
            {
                'mission_id': row[0],
                'target_type': row[1],
                'target_industry': row[2],
                'target_priority': row[3],
                'target_country': row[4],
                'target_city': row[5],
                'target_latitude': row[6],
                'target_longitude': row[7]
            }
            for row in rows
        ]

        return denormalized_data

    except Exception as e:
        print(f"An error occurred while fetching mission data: {e}")
        return []

    finally:
        cursor.close()
        close_db_connection(connection)
