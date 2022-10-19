#import operator
#from operator import itemgetter
import sqlite3

fh = open(r'test.txt', encoding="utf8")

lst = list()
for line in fh:
    line = line.strip()
    if line.startswith('city'):
        continue
    cline = line.split(",")
    #tbl = operator.itemgetter(4, 0)(cline)
    citylst = cline[0]
    regionlst = cline[4]

    sql = """
    insert into city
    (city.name )
    VALUES
    (citylst)
    """
    cursor.execute(sql)

    sql = """
        insert into region
        (region.name )
        VALUES
        (regionlst)
        """
    cursor.execute(sql)




