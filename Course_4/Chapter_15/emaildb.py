import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, "count" INTEGER)''')


fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    org = pieces[1].split('@')[1]

    # ? 表示不指定email, 免得sql injection. (org,) 可以增加 if there is more columns.
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))

    # try to get data from one row, if not, return None
    row = cur.fetchone()

    # check if the name is exist in DB, if not, set initial number = 1
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    # data exist in DB, add one, but use UPDATE to the column
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()  # force everything written to disc

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()