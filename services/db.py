import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='g_brothels'
)

def insert_item(room_number, facility, available):
    cursor = db.cursor()
    cursor.execute("INSERT INTO tbl_room (room_number, facility, available) VALUES (%s, %s, %s)", (room_number, facility, available))
    db.commit()