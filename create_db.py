import psycopg2
settings = {
    'host': 'localhost',
    'user': 'postgres',
    'password': 'coderslab',
    }
connection = psycopg2.connect(**settings)
connection.autocommit = True
query = "CREATE DATABASE warsztat_db;"
try:
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
except psycopg2.ProgrammingError as e:
    if e.pgcode == "42P04":
        print("baza danych już istnieje")
    else:
        raise
cursor.close()
connection.close()

