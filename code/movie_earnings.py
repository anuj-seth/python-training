import sqlite3
import csv 

connection = sqlite3.connect("movies.db")

# a cursor is your temporary work area in memory
# it holds the result of your queries, etc
cursor = connection.cursor()

# delete 
cursor.execute("""DROP TABLE IF EXISTS movie_box_office;""")

create_table_sql = """CREATE TABLE movie_box_office ( 
movie_name VARCHAR(100),
production_company VARCHAR(50),
distributor VARCHAR(100),
genre VARCHAR(20),
worldwide_gross VARCHAR(30),
PRIMARY KEY (movie_name) );"""

cursor.execute(create_table_sql)
movie_data = [['Padmaavat', 'Viacom 18 Motion Pictures', 'Viacom 18 Motion Pictures', 'Period Drama', '564 crore (US$86 million)'],
              ['Padman', 'KriArj Entertainment', 'Columbia Pictures', 'Comedy Drama', '117.94 crore (US$18 million)'],
              ['Sonu Ke Titu Ki Sweety', 'T-Series Films', 'AA Films', 'Romantic Comedy', '95.55 crore (US$15 million)']]

insert_sql = """insert into movie_box_office 
(movie_name, production_company, 
distributor, genre, worldwide_gross) 
values (?, ?, ?, ?, ?);"""

#cursor.execute(insert_sql, movie_data[0])
cursor.executemany(insert_sql, movie_data)

select_sql = "select * from movie_box_office"
cursor.execute(select_sql)
for r in cursor.fetchall():
    print(r)

connection.commit()
connection.close()

with open('2018_movie_earnings.csv') as infile:
    inreader = csv.reader(infile, delimiter=';')
    for row in inreader:
        #print(row)
        pass
