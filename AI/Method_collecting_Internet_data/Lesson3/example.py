from bson import ObjectId
from pprint import pprint
from pymongo import MongoClient

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'posts'
MONGO_COLLECTION = 'news'

def print_MongoDoc(cursor):
    for doc in cursor:
        pprint(doc)

# client = MongoClient(MONGO_HOST, MONGO_PORT)
# # ...
# client.close()
#
# with MongoClient(MONGO_HOST, MONGO_PORT) as client:
#     pass

# CRUD
# Create
# Read
# Update
# Delete


with MongoClient(MONGO_HOST, MONGO_PORT) as client:
    post_doc = {
        'title': 'Using MongoDB',
        'rating': 1
    }

    posts = [
        {
            'title': 'Using SQL',
            'rating': 9
        },
        {
            'title': 'Example of BeutifulSoup4'
        }
        ]

    post_doc_id = {
        'title': 'How to scrape',
        'rating': -1,
        '_id': ObjectId('622f8f01e34ed5748f9feb83')
    }


    db = client[MONGO_DB]
    news = db[MONGO_COLLECTION]
    # Create
    # news.insert_one(post_doc)
    # news.insert_many(posts)
    # news.insert_one(post_doc_id)
    # Read
    # cursor = news.find({})
    # cursor = news.find({
    #     'rating': {'$lt': 2}
    # })
    # print()
    # print_MongoDoc(cursor)
    # print()

    # cursor = news.find({
    #     'rating': {'$lt': 2}
    # }).limit(2)

    # cursor = news.find({
    #     'rating': {'$lt': 10}
    # }).sort('rating', direction=1)

    # Update
    find_condition = {
        'rating': 9,

    }

    # update_data = {
    #     '$set': {
    #         'title': 'New Title rating 9',
    #         'number views': 100
    #     }
    update_data = {
        '$unset': {
            'title': None
        }
    }

    news.update_one(find_condition, update_data)


    # Delete
    find_condition = {
        'number_of_views': 999
    }
    news.delete_one(find_condition)


    # print_MongoDoc(cursor)