import pymongo
from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client['pymongo_test']
    posts = db.posts
    post_1 = {
        'title': 'Python and MongoDB',
        'content': 'PyMongo is fun, you guys',
        'author': 'Scott'
    }
    post_2 = {
        'title': 'Virtual Environments',
        'content': 'Use virtual environments, you guys',
        'author': 'Scott'
    }
    post_3 = {
        'title': 'Learning Python',
        'content': 'Learn Python, it is easy',
        'author': 'Bill'
    }
    new_result = posts.insert_many([post_1, post_2, post_3])
    print('Multiple posts: {0}'.format(new_result.inserted_ids))


if __name__ == '__main__':
    main()