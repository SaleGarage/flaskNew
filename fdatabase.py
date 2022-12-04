import sqlite3




def create_db():
    db = connect_db()
    with app.open_resource('sql_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

class FdataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def addMenu(self, title, url):
        try:
            self.__cur.execute('INSERT INTO mainmenu VALUES (NULL, ?, ?)', (title, url))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления в БД', str(e))
            return False
        return True

    def delMenu(self, id=0):
        try:
            if id == 0:
                pass
            else:
                self.__cur.execute(f"DELETE FROM mainmenu WHERE id=={id}")
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка удаления из БД', str(e))
            return False
        return True

    def getMenu(self):
        try:
            sql = """SELECT * FROM mainmenu"""
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res: return res
        except:
            print("Ошибка чтения из БД")
            return []

if __name__ == '__main__':
    from app import connect_db, app
    print(create_db.__doc__)
    db = connect_db()
    db = FdataBase(db)
    for i in db.getMenu():
        print(i['url'])
    print(*db.getMenu())
    #print(db.addMenu('Логин2', 'login2'))