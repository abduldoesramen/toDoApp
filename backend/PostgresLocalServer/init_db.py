import os
import psycopg2
from dotenv import load_dotenv
import shortuuid

load_dotenv()

# Env private attributes
username=os.getenv('username')
password=os.getenv('password')
database=os.getenv('database')

conn = psycopg2.connect(
        host="localhost",
        database="todoapp_db",
        user=username,
        password=password)

# Open a cursor to perform database operations
cur = conn.cursor()

userone = shortuuid.uuid()
usertwo = shortuuid.uuid()


# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS events;')
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (UserId varchar (100) PRIMARY KEY,'
                                 'email varchar (50) NOT NULL UNIQUE,'
                                 'password varchar (50) NOT NULL);'
                                 )
cur.execute('CREATE TABLE events (EventId varchar (100) NOT NULL PRIMARY KEY,'
                                 'event varchar (300) NOT NULL,'
                                 'uid varchar REFERENCES users(UserId));'
                                 )

# Insert dummy data to test into the table
cur.execute('INSERT INTO users (UserId, email, password)'
            'VALUES (%s, %s, %s)',
            (
             userone,
             'abdul@anemail.com',
             'chickenwithrice')
            )

cur.execute('INSERT INTO users (UserId, email, password)'
            'VALUES (%s, %s, %s)',
            (
             usertwo,
             'softwareEngenius@rice.com',
             'iCodeAllDay')
            )

# Insert dummy toDoList strings associated with the users above
cur.execute('INSERT INTO events (EventId, event, uid)'
            'VALUES (%s, %s, %s)',
            (shortuuid.uuid(),
             'take out the rubbish',
             userone)
            )
cur.execute('INSERT INTO events (EventId, event, uid)'
            'VALUES (%s, %s, %s)',
            (shortuuid.uuid(),
             'clean the dishes',
             userone)
            )

cur.execute('INSERT INTO events (EventId, event, uid)'
            'VALUES (%s, %s, %s)',
            (shortuuid.uuid(),
             'program code',
             usertwo)
            )

conn.commit()

cur.close()
conn.close()