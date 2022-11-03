import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://tequiceno:luis0305@mintic4aresultados.jgksgg9.mongodb.net/results_db?retryWrites=true&w=majority",
    tlsCAFile=ca
)

db = client.test
print(db)

data_base = client['results_db']
print(data_base.list_collection_names())
