import psycopg2
from connect_db import connect_db
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

create_users_table_query = """
create table Users
(   
    id serial Primary key,
    username varchar(255),
    hashed_password varchar(80)
);
"""
create_messages_table_query = """
create table Messages
(
    id serial Primary key,
    from_id int,
    to_id int,
    foreign key(from_id) references users(id),
    foreign key(to_id) references users(id),
    creation_date timestamp,
    text varchar(255)
);
"""

connection_db = connect_db()
try:
    cursor = connection_db.cursor()
    cursor.execute(create_users_table_query)
    connection_db.commit()
except psycopg2.ProgrammingError as e:
    if e.pgcode == "42P07":
        print("tabela users już istnieje")
    else:
        raise
try:
    cursor = connection_db.cursor()
    cursor.execute(create_messages_table_query)
    connection_db.commit()
except psycopg2.ProgrammingError as e:
    if e.pgcode == "42P07":
        print("tabela messages już istnieje")
    else:
        raise

cursor.close()
connection_db.close()


