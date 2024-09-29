from db.connection import get_db_connection, close_db_connection
from db.models import mission_table


def create_mission_tables():

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(mission_table)
        connection.commit()
        print("mission Table created successfully!")

    except Exception as e:
        print(f"An error occurred while creating table: {e}")
        connection.rollback()

    finally:
        cursor.close()
        close_db_connection(connection)


if __name__ == "__main__":
    create_mission_tables()
