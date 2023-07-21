import sqlite3

dbname = 'app.db'
conn = sqlite3.connect(dbname)

# SQLiteを操作するためのカーソルを作成
cur = conn.cursor()

# テーブルの作成
x = cur.execute(
    'SELECT * FROM User'
)
print(x.fetchall())
conn.close()