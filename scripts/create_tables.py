from db.connection import get_db_connection, close_db_connection
from db.models import target_table, location_table, coordinate_table



def create_tables():
    """Create tables in the database."""
    connection = get_db_connection()
    cursor = connection.cursor()

    try:

        cursor.execute(location_table)
        cursor.execute(coordinate_table)
        cursor.execute(target_table)


        connection.commit()
        print("Tables created successfully!")

    except Exception as e:
        print(f"An error occurred while creating tables: {e}")
        connection.rollback()

    finally:
        cursor.close()
        close_db_connection(connection)


if __name__ == "__main__":
    create_tables()
