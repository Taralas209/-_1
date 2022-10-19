with open('regions.csv', encoding='utf-8') as region_f:
    regions = set()
    for line in region_f:
        cline = line.strip()
        tline = (cline )
        regions.add(tline)
    print(regions)
    #with sqlite3.connect("cities.db") as connection:
        #cursor = connection.cursor()
        #cursor.executemany("""INSERT INTO region ('name') VALUES (?);""", regions)