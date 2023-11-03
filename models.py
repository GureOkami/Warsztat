import psycopg2
from connect_db import connect_db
class User:
    def __init__(self, username, _hashed_password):
        _id = -1
        self._id = _id
        self.username = username
        self._hashed_password = _hashed_password
    @property
    def id(self):
        return self._id
    @property
    def hashed_password(self):
        return self._hashed_password
    @property
    def user_name(self):
        return self.username

    def set_username(self, name):
        self.username = name

    def set_password(self, password):
        self._hashed_password = password

    @user_name.setter
    def user_name(self, name):
        self.set_username(name)

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)

    def save_to_db(self, cursor):
        if self._id == -1:
            query = """INSERT INTO Users(username, hashed_password)
                        VALUES (%s, %s) 
                        RETURNING id"""
            values = (self.username, self.hashed_password)
            cursor.execute(query, values)
            self._id = cursor.fetchone()[0]
            return True
        else:
            query ="""UPDATE Users SET username=%s, hashed_password=%s
                        WHERE id=%s"""
            values = (self.username, self.hashed_password, self.id)
            cursor.execute(query, values)
            return True

    @staticmethod
    def load_user_by_username(cursor, username):
        query ="SELECT id, username, hashed_password FROM Users WHERE username = %s"
        cursor.execute(query, (username,))
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username, hashed_password)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None

    @staticmethod
    def load_user_by_id(cursor, id_):
        query = "SELECT id, username, hashed_password FROM Users WHERE id=%s"
        cursor.execute(query, (id_,))
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username, hashed_password)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None
    @staticmethod
    def load_all_users(cursor):
        query = "SELECT id, username, hashed_password FROM Users"
        users = []
        cursor.execute(query)
        for row in cursor.fetchall():
            id_, username, hashed_password = row
            loaded_user = User(username, hashed_password)
            loaded_user._id = id_
            loaded_user.username = username
            loaded_user._hashed_password = hashed_password
            users.append(loaded_user)
        return users
    def delete(self, cursor):
        query = "DELETE FROM Users WHERE id=%s"
        cursor.execute(query, (self.id,))
        self._id = -1
        return True

class Messages_service:
    def __init__(self, from_id, to_id, creation_date, text):
        _id = -1
        self._id = _id
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self.creation_date = creation_date
    @property
    def id(self):
        return self._id
    def save_to_db(self, cursor):
        if self._id == -1:
            query = """INSERT INTO Messages(from_id, to_id, creation_date, text)
                        VALUES (%s, %s, %s, %s) 
                        RETURNING id"""
            values = (self.from_id, self.to_id, self.creation_date, self.text)
            cursor.execute(query, values)
            self._id = cursor.fetchone()[0]
            return True
        else:
            query ="""UPDATE Users SET from_id=%s, to_id=%s, creation_date=%s, text=%s
                        WHERE id=%s"""
            values = (self.from_id, self.to_id, self.creation_date, self.text, self.id)
            cursor.execute(query, values)
            return True

    @staticmethod
    def load_all_messages(cursor):
        query = "SELECT id, from_id, to_id, creation_date, text FROM Messages"
        messages = []
        cursor.execute(query)
        for row in cursor.fetchall():
            id_, from_id, to_id, creation_date, text = row
            loaded_message = Messages_service(from_id, to_id, creation_date, text)
            loaded_message._id = id_
            loaded_message.from_id = from_id
            loaded_message.to_id = to_id
            loaded_message.creation_date = creation_date
            loaded_message.text = text
            messages.append(loaded_message)
        return messages






