import sqlite3
import random

def new_game_id(cursor):
    cursor.execute("Select game_id from dart_game")
    ret = cursor.fetchall()
    if len(ret)>0:
        prev_id = max(ret)[0]
        print(prev_id)
    else:
        prev_id = 0
    return int(prev_id)+1


def new_throw(cursor,game_id):
    cursor.execute("Select throw_id from dart_throw where game_id = {}".format(game_id))
    ret = cursor.fetchall()
    if len(ret)>0:
        throw_id = max(ret)[0]
        print(throw_id)
    else:
        throw_id = 0

    #get values of new throw
    throw = random.randint(1,20)

    return [throw,'S',throw,'T',throw,'D',throw_id+1]

connection = sqlite3.connect("darts.db")

cursor = connection.cursor()
try:
    cursor.execute("CREATE TABLE dart_throw (first_value integer, first_type text, second_value integer, second_type text, third_value integer, third_type text, game_id integer, throw_id integer)")
    cursor.execute("CREATE TABLE dart_game (points integer, game_id integer, type text)")
except:
    pass


game_id = new_game_id(cursor=cursor)
print(game_id)
cursor.execute("INSERT INTO dart_game VALUES (501,{},'DoubleOut')".format(game_id))

connection.commit()

throw = new_throw(cursor,game_id=game_id)

cursor.execute("INSERT INTO dart_throw VALUES ({},'{}',{},'{}',{},'{}',{},{})".format(throw[0],throw[1],throw[2],throw[3],throw[4],throw[5],game_id,throw[6]))

connection.commit()

throw = new_throw(cursor,game_id=game_id)

cursor.execute("INSERT INTO dart_throw VALUES ({},'{}',{},'{}',{},'{}',{},{})".format(throw[0],throw[1],throw[2],throw[3],throw[4],throw[5],game_id,throw[6]))

connection.commit()

cursor.execute("Select * from dart_throw")
print(cursor.fetchone())
for c in cursor.fetchall():
    print(c)

connection.close()

