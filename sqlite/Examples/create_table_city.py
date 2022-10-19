import sqlite3

with sqlite3.connect('loft_school_bank.db') as connection:
    cursor = connection.cursor()

    sql = """
        CREATE TABLE city(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, 
            region_id INTEGER,
            FOREIGN KEY(region_id) REFERENCES region(id)
        );
    """
    cursor.execute(sql)
