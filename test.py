import pymongo
client = pymongo.MongoClient("mongodb+srv://faizan:faizFAIZ1219@faizan.fatlcov.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"faizan" ,
    "email":"tauhidfaiz@gmail.com",
    " surname": "tauhid"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
