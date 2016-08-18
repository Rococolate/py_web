import sqlite3 as sql


def initDB(filename=None):
    """
    :param filename:
    :return:
    """
    global db, cursor
    if not filename:
        filename = 'contact.db'
    try:
        db = sql.connect(filename)
        cursor = db.cursor()
        # cursor.execute('PRAGMA Foreign_Keys=TRUE')
    except:
        print("Error connecting to", filename)
        cursor = None
        raise


def create_table():
    """
    
    :return:
    """
    query = '''create TABLE contact(
name VARCHAR(255) not null,phone VARCHAR(255) not null,qq VARCHAR(255) not null,address VARCHAR(255) not null,marriage
VARCHAR(255) not null
)'''
    cursor.execute(query)


def update_person(name, phone, qq, address, marriage):
    """
    :param name:
    :param phone:
    :param qq:
    :param address:
    :param marriage:
    :return:
    """
    query = '''insert into contact values ('%s','%s','%s','%s','%s')''' % (name, phone, qq, address, marriage)
    cursor.execute(query)
    # print(query)


def closeDB():
    """
    :return:
    """
    try:
        cursor.close()
        db.commit()
        db.close()
    except:
        print("problem closing database...")
        raise


def select_date():
    query = '''select * from contact'''
    return cursor.execute(query).fetchall()


if __name__ == "__main__":
    initDB()
    # update_person("张三",16355466773,475883,"广州湛江","单身")
    # closeDB()
    # el = select_date()
    # for i in el:
    #     print(*i)
