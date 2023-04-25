import sqlite3

db = sqlite3.connect('try.db')
cursor = db.cursor()

db.execute('''CREATE TABLE IF NOT EXISTS try
( id INTEGER PRIMARY KEY AUTOINCREMENT,
user_name VARCHAR(15) NOT NULL,
emeil VARCHAR(354) NOT NULL ,
phon_number INTEGER NOT NULL ,
is_merried BOOLEAN DEFAULT FALSE
)''')

# db.execute("""INSERT INTO try (user_name, emeil, phon_number, is_merried) VALUES ('aslan', 'ascaln@.com', 01212, False)""")
db.commit()
# for all_try in db.execute("""SELECT * FROM try"""):
#     print(all_try)
# db.execute("""UPDATE try SET phon_number = 770121212 """)
# db.execute("""DELETE  FROM try WHERE id = 1""")
# db.commit()