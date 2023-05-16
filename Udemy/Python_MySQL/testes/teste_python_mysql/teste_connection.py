import MySQLdb

host = "localhost"
user = "aplicacao"
password = "12345678"
db = "escola_curso"
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)

def select(fields, tables, where=None):
    global c
    query = f"SELECT {fields} FROM {tables}"

    if(where):
        query = query + " WHERE " + where
    
    c.execute(query)

    return c.fetchall()

def insert(table, values, fields=None):
    global c,con

    query = f"INSERT INTO {table}"
    if(fields):
        query = query + f"({fields})"
    query = query + " Values " + ", ".join([f"({v})" for v in values])
    c.execute(query)
    con.commit()
values = [
    "DEFAULT, 'João Pedro', '2000-01-01', 'Rua da Saudade, 123', 'Campinas', 'SP', '12345678911'",
    "DEFAULT, 'Maria Pedro', '2000-01-01', 'Rua da Saudade, 123', 'Campinas', 'SP', '12345678910'"]

def update(table, field_value, where=None):
    global c, con
    query = f"UPDATE {table} SET"
    for i in field_value:
        query = query + f" {i} = '{field_value[i]}',"
    query = query.rstrip(query[-1])
    query = query + f" WHERE {where}"
    c.execute(query)
    con.commit()

def delete(table, where):
    global c, con
    query = f"DELETE FROM {table} WHERE {where}"
    c.execute(query)
    con.commit()

dic = {"nome": "Rafael", "cidade": "Valinhos"}