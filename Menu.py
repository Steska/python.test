class Menu:
    def __init__(self, db):
        self.__db = db
        self.__cursor = db.cursor()


    def getMenus(self):
        sql = '''select * from mainmenu'''
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except:
            print('Error')
        return []