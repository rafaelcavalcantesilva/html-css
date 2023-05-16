import mysql.connector as db

con = db.connect(user="aplicacao", password="12345678", host="localhost", database="escola_curso")

c = con.cursor()
################ Função Select ################
def select(fields, tables, where=None):
    global c
    query = f"SELECT {fields} FROM {tables}"
    if(where):
        query = query + " WHERE " + where
    c.execute(query)

    return c.fetchall()

################ Função Insert ################
def insert (values, table, fields=None):
    global c, con
    
    query = f"INSERT INTO {table}"
    if(fields):
        query = query + f" ({fields}) "
    query = query + " VALUES " + ", ".join([f"({v})" for v in values])

    c.execute(query)
    con.commit()

values = [
    "DEFAULT, 'João Pedro', '2000-01-01', 'Rua da Saudade, 123', 'Campinas', 'SP', '12345678911'",
    "DEFAULT, 'Maria Pedro', '2000-01-01', 'Rua da Saudade, 123', 'Campinas', 'SP', '12345678910'"]

################ Função Update ################
def update(sets, table, where=None):
    global c, con
    query = f"UPDATE {table} SET " + ", ".join([f"{field} = '{value}'" for field, value in sets.items()])
    if(where):
        query = query + f" WHERE {where}"
    c.execute(query)
    con.commit()

# def update(table, fields_values, where=None):
#     global c, con
#     query = f"UPDATE {table} SET"
#     for i in fields_values:
#         query = query + f" {i} = '{fields_values[i]}',"
#     query = query.rstrip(query[-1])
#     if (where):
#       query = query + f" WHERE {where}"
#     c.execute(query)
#     con.commit()

# def update(table, fields_values, where):
#     global c, con
#     for i in fields_values:
#         query = f"UPDATE {table} SET {i} = '{fields_values[i]}' WHERE {where}"
#         c.execute(query)
#         con.commit()

################ Função Delete ################
def delete(table, where):
    global c, con

    query = f"DELETE FROM {table} WHERE {where}"
    
    c.execute(query)

    con.commit()

dic = {"nome": "Rafael", "cidade": "Valinhos"}