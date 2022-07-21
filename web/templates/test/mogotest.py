from matplotlib import collections
from pymongo import mongo_client
import os
import sys

#  "dnspython" module must be installed to use mongodb+srv:// URIs. To fix this error install pymongo with the srv extra:

conn_str = '''mongodb+srv://ronin:roninrocK1@cluster0.mp1aw.mongodb.net/?retryWrites=true&w=majority'''
client = mongo_client.MongoClient(conn_str)

dbs = client.list_database_names()

login = client['login']

collections = login.list_collection_names()
print(collections)


def insert_user(username, password, id):
    login['users'].insert_one(
        {'id': id, 'username': username, 'password': password})


insert_user('ronin5', 'pattern006', 25)


def inser_note(note, id):
    login['notes'].insert_one({'_id': 3, 'users': id, 'note': note})


def findNote(id):
    res = login['note'].find_one({'note_id': id})

    return res['user_id']


def findAll(nt_us, id):
    res = login[nt_us].find({"_id": id})
    print(list(res))
    # for x in res:
    #     print(x['note_id'], findNote(x['note_id']))
    return list(res)


def del_usr(id):
    login['users'].delete_one({'id': id})


def logger(user, pas):
    usr = login['user'].find_one({'username': user})
    print(usr['password'], usr['username'])
    if usr['username'] == user and usr['password'] == pas:
        return True
    else:
        return False


# inser_note('rober123t', [4, 5, 6])
#
findAll('notes', 3)

# print(findNote(14))

# for x in range(2):
#     del_usr(5)
