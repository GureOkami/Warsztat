import psycopg2
from connect_db import connect_db
from models import User, Messages_service
from datetime import datetime

dt = datetime.now()
ts = datetime.timestamp(dt)


user = User("patryk", 123)
user1 = User("mateusz", 234)


connection = connect_db()
cursor = connection.cursor()
u1 = User.load_user_by_id(cursor, 18)
user.save_to_db(cursor)
user1.save_to_db(cursor)
u = User.load_user_by_username(cursor, "patryk")
u3 = User.load_all_users(cursor)
u4 = User.load_user_by_id(cursor,57)
u4.set_username("kacper")
u4.set_password(567)
u4.save_to_db(cursor)
message = Messages_service(57, 58, dt, "dupa")
message.save_to_db(cursor)
message1 = Messages_service.load_all_messages(cursor)


for x in u3:
    print(x.id)
    print(x.username)
    print(x.hashed_password)
    # x.delete(cursor)
print(u4.username)
for y in message1:
    print(y.text)
    print(y.from_id)
    print(y.to_id)
    print(y.creation_date)

