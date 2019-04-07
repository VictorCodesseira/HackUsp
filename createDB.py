import sqlite3

conn = sqlite3.connect('Users.db')  # You can create a new database by changing the name within the quotations
c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved

# Create table - Users
c.execute('''CREATE TABLE Users
             ([NUSP] INTEGER PRIMARY KEY,
              [Name] text, 
              [Institute] text, 
              [CEP] integer, 
              [Number] integer,
              [Car] bool,
              [Rodizio] integer, 
              [CreditCard] integer, 
              [Bank_Agency] integer, 
              [Bank_Account] integer, 
              [Cellphone] integer)''')

# Create table - Schedule
c.execute('''CREATE TABLE Schedule
             ([NUSP] integer,
              [WeekDay] integer, 
              [Departure] time,
              [Return] time,
              [Car] bool,
              PRIMARY KEY(NUSP, WeekDay))''')

# Create table - Matches
c.execute('''CREATE TABLE Matches
             ([generated_key] INTEGER PRIMARY KEY,
              [WeekDay] integer, 
              [Departure] time,
              [Return] time,
              [Driver] integer,
              [Passenger_1] integer,
              [Passenger_2] integer,
              [Passenger_3] integer,
              [Passenger_4] integer)''')

conn.commit()

conn.close()
# Note that the syntax to create new tables should only be used once in the code (unless you dropped the table at the end of the code).
# The [generated_id] column is used to set an auto-increment ID for each record
# When creating a new table, you can add both the field names as well as the field formats (e.g., Text)
