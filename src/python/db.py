import sqlite3

connection = None
cursor = None
sql = None


def init(database):
    global connection, cursor

    connection = sqlite3.connect(database)
    cursor = connection.cursor()


def set_insert_statement(statement):
    global sql
    sql = statement


# Wrapper for inserting many values
def preset_insert_many(values):
    cursor.executemany(sql, values)
    connection.commit()
