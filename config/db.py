from pymongo import MongoClient
# MONGO_URI="mongodb+srv://kneha5489:rdslJF2rCMp8PqCM@cluster0.dwxshzd.mongodb.net"
MONGO_URI="mongodb+srv://kneha5489:rdslJF2rCMp8PqCM@cluster0.dwxshzd.mongodb.net"

conn=MongoClient(MONGO_URI)

print(conn)