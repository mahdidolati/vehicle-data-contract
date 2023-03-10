import sqlite3


class DbInterface:
    def __init__(self):
        self.sqliteConnection = sqlite3.connect("database.db")
        self.cursor = self.sqliteConnection.cursor()
        print(f"Database created and Suncessfully connected to SQLite")

    def save(self, k, v):
        insert_query = """INSERT INTO vehicle_data (DATA_ADR, DATA_VAL) VALUES (?, ?)"""
        count = self.cursor.execute(insert_query, (k, v,))
        self.sqliteConnection.commit()
        print(f"Inserted {count.rowcount}.")

    def retrieve(self, k):
        select_query = """SELECT * FROM vehicle_data WHERE DATA_ADR = ? LIMIt 1"""
        self.cursor.execute(select_query, (k,))
        rows = self.cursor.fetchall()
        if len(rows) > 0:
            return rows[0][1]
        return None

    def close(self):
        self.cursor.close()
        self.sqliteConnection.close()