import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="todoapp_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (UserId serial PRIMARY KEY,'
                                 'email varchar (50) NOT NULL,'
                                 'password varchar (50) NOT NULL);'
                                 )
cur.execute('CREATE TABLE events (EventId serial NOT NULL PRIMARY KEY,'
                                 'event varchar (300) NOT NULL,'
                                 'uid integer REFERENCES users(UserId));'
                                 )

# Insert dummy data to test into the table
cur.execute('INSERT INTO users (email, password)'
            'VALUES (%s, %s)',
            ('abdul@anemail.com',
             'chickenwithrice')
            )

cur.execute('INSERT INTO users (email, password)'
            'VALUES (%s, %s)',
            ('softwareEngenius@rice.com',
             'iCodeAllDay')
            )

# Insert dummy toDoList strings associated with the users above
cur.execute('INSERT INTO events (event, uid)'
            'VALUES (%s, %s)',
            ('take out the rubbish',
             1)
            )
cur.execute('INSERT INTO events (event, uid)'
            'VALUES (%s, %s)',
            ('clean the dishes',
             1)
            )

cur.execute('INSERT INTO events (event, uid)'
            'VALUES (%s, %s)',
            ('program code',
             2)
            )

conn.commit()

cur.close()
conn.close()