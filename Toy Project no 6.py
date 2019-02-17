import csv
import sqlite3

conn = sqlite3.connect('about.db')

with open('addfile.csv', 'r') as csv_file:
    c = conn.cursor()
    csv_reader =csv.reader(csv_file)
    next(csv_reader)
    for each in csv_reader:
        name = each[0]
        age = int(each[1].strip())
        address = each[2]
        phone = int(each[3].strip())
        profession = each[-1]

        c.execute(f"INSERT INTO directory_info VALUES ('{name}','{age}','{address}','{phone}','{profession}')")
        conn.commit()



