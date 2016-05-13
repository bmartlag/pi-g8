import MySQLdb
db = MySQLdb.connect("localhost", "root", "raspberry", "eyebaby")
cursor = db.cursor()
query = """SELECT * FROM eyebaby"""
lines = cursor.execute(query)
data = cursor.fetchall()
for x in data:
    print x, x[0], x[1], x[2]
db.close()