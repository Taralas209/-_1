import sqlite3

with sqlite3.connect("cities.db") as connection:
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

    sql = """
            CREATE TABLE region(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE           
            );
        """
    cursor.execute(sql)

with open('regions.csv', encoding='utf-8') as region_f:
    regions = set()
    for line in region_f:
        cline = line.strip()
        tline = (cline.replace('"', ''), )
        regions.add(tline)
    with sqlite3.connect("cities.db") as connection:
        cursor = connection.cursor()
        cursor.executemany("""INSERT INTO region ('name') VALUES (?);""", regions)

