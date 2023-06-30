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

def query(sql, *params):
    cursor.execute(sql, params)
    return cursor.fetchall()

def get_timeseries_arr(table, column, flight_id, genome_id):
    sql = f"SELECT {column} FROM {table} WHERE flight_id = ? AND genome_id = ?"
    result = query(sql, flight_id, genome_id)

    return [row[0] for row in result]
