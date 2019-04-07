import sqlite3

conn = sqlite3.connect('Users.db')  # You can create a new database by changing the name within the quotations
c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved

# Insert a row of data
c.execute("INSERT INTO Users VALUES (9833711,'Victor Chacon','Poli',03121010,100,1, 2, 0, 0, 0, 11995426622)")
c.execute("INSERT INTO Users VALUES (9833534,'Clara Cappatto','Poli',03136040,628,0, 0, 0, 0, 0, 11994315698)")
c.execute("INSERT INTO Users VALUES (9833111,'Felipe Machado','Poli',03121010,300,0, 0, 0, 0, 0, 11995426622)")

c.execute("INSERT INTO Schedule VALUES (9833711, 1,'13:10','16:40',1)")
c.execute("INSERT INTO Schedule VALUES (9833711, 2,'7:30','18:30',1)")
c.execute("INSERT INTO Schedule VALUES (9833711, 4,'7:30','16:40',1)")
c.execute("INSERT INTO Schedule VALUES (9833711, 5,'7:30','16:40',1)")

c.execute("INSERT INTO Schedule VALUES (9833111, 1,'7:30','16:40',0)")
c.execute("INSERT INTO Schedule VALUES (9833111, 2,'13:10','18:30',0)")
c.execute("INSERT INTO Schedule VALUES (9833111, 3,'7:30','13:10',0)")
c.execute("INSERT INTO Schedule VALUES (9833111, 4,'7:30','16:40',0)")
c.execute("INSERT INTO Schedule VALUES (9833111, 5,'7:30','16:40',0)")




conn.commit()

conn.close()
# Note that the syntax to create new tables should only be used once in the code (unless you dropped the table at the end of the code).
# The [generated_id] column is used to set an auto-increment ID for each record
# When creating a new table, you can add both the field names as well as the field formats (e.g., Text)