import sqlite3

con = sqlite3.connect('control.db')
cur = con.cursor()

def getProfiles():
    a = cur.execute("SELECT * FROM profiles")
    profiles = a.fetchall()
    return profiles
