import pymongo
import cerftifi


me = {
    "name": "Jake",
    "last_name": "Gulotta",
    "age": 31,
    "hobbies": ["Jiu Jitsu"],
    "address": {
        "street": "dalehaven",
        "city": "San Diego",
        "zip": 92105
    }
}

con_str = "mongodb+srv://jakegulotta:Test1234@cluster0.oh0sfmg.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("tritone")