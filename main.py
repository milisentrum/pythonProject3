from fastapi import FastAPI
from models import *
from main_ import *

database: List[People] = []

# вставка данных в "сервер"
def postDB(ppl: People):
    database.append(ppl)
    return database
with con:
    data = con.execute("SELECT * FROM customers")
    for row in data:
        postDB(row)

# todo как-то по-умному сделать добавление названий после '/' в url в другом проекте

app = FastAPI()
mainurl = '/api/database'

#декоратор
# @app.get('/')
# def root():
#      return {'message': 'HI!'}

# todo: печатать каждую строку бд с новой строки
@app.get(mainurl)
def getDB():
    return database

# сортировка по имени, т.к. по value они уже отсортированы, а по id  нет значения сортировать т.к. оно uuid
# todo: мб реализовать возможность сортировки по выбранным полям
@app.get(mainurl+'/sort')
def sortdb():
    return sorted(getDB(), key=lambda people: people[1])

# @app.delete(mainurl)
# def deleteItem(ppl:Dict):
#     for item in database:
#         index = database.index(item)
#         for key in ppl:
#             if(database[index][key]==ppl[key]):
#                 database.pop(index)
#     return database

@app.delete(mainurl)
def deleteItem(ppl:Dict):
    for item in database:
        index = database.index(item)
        for key in ppl:
            if(database[index][key]==ppl[key]):
                database.pop(index)
    return database

# todo: печатать только те данные, что были добавлены
@app.post(mainurl)
def getdata(ppl: People):
    database.append(ppl)
    return database