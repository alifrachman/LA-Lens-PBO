import mysql.connector

class Connect():
    
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="la_lens"
    )

    def is_connected(self):
        if self.db.is_connected():
            return True