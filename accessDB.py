import sqlite3

def getUser(user):
    conn = sqlite3.connect('Users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Users WHERE NUSP='%d'" % user)

    return str(c.fetchone())

def getSchedule(user):
    conn = sqlite3.connect('Users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Matches WHERE (Driver='%d' OR Passenger_1='%d' OR Passenger_2='%d' OR Passenger_3='%d' OR Passenger_4='%d')" % (user,user,user,user,user))

    return(str(c.fetchall()))
