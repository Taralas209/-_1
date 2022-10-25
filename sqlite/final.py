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

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()
    regdic = cursor.execute("""SELECT name, id FROM region;""")
    regions = dict(regdic.fetchall())

with open('towns.csv', encoding='utf-8') as city_f:
    lst = list()
    for line in city_f:
        line = line.strip()
        if line.startswith('city'):
            continue
        cline = line.split(",")
        citylst = cline[0]
        regionlst = cline[4]
        region_id = regions.get(regionlst)
        if region_id:
            lst.append((citylst, region_id))
        else:
            print(citylst, regionlst)

with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()
    cursor.executemany("""INSERT INTO city ('name', 'region_id') VALUES (?, ?);""", lst)


search_key = 'Архангельская область'

search_region_id = regions[search_key]
with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()
    result = cursor.execute('SELECT name FROM city WHERE region_id=?', (search_region_id, ))
    for city in result.fetchall():
        print(city[0])


with sqlite3.connect("cities.db") as connection:
    cursor = connection.cursor()
    result = cursor.execute("""
        SELECT region.name, count(city.id) 
        FROM city, region 
        WHERE city.region_id = region.id 
        GROUP BY city.region_id
        ORDER BY count(city.id) DESC;
    """)
    for row in result.fetchall():
        print(row[0],row[1])
