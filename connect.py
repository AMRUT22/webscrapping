import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)

    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")
    print("Table Created Successfully...")

    conn.close()

def insert_into_table(dbname, values):
    conn = sqlite3.connect(dbname)
    print("Inserted into table: " + str(values))
    insert_sql = "INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES(?, ?, ?, ?, ?)"
    conn.execute(insert_sql, values)
    print("Table Created Successfully...")

    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn = sqlite3.connect(dbname)
    cur = conn.cursor()

    cur.execute("SELECT * FROM OYO_HOTELS")
    table_data = cur.fetchall()

    for record in table_data:
        print(record)

    conn.close()