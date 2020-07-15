import pymongo

def mongodb_connection(config):
    maxSevSelDelay = 5
    print("Checking MongoDB server connection.")
    try:
        client = pymongo.MongoClient(config.MONGODB_URI, serverSelectionTimeoutMS=maxSevSelDelay)
        client.server_info()
        print("SUCCESS. Connected to MongoDB at [{}]".format(config.MONGODB_URI))

    except:
        print("FAILURE. MongoDB at [{}] is unavailable.".format(config.MONGODB_URI))