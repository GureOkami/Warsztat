import psycopg2
setings = {
    'host' : 'localhost',
    'user' : 'postgres',
    'password' : 'coderslab',
    'database' : 'warsztat_db',
}
def connect_db():
    connection = psycopg2.connect(**setings)
    connection.autocommit = True
    return connection