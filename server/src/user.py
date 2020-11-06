from flask_login import UserMixin
import json
import threading
from os import path

class User(UserMixin):
    def __init__(self, id, *, signup=False, name = None, email = None, profile_pic = None):
        if not path.exists(f"data/users/{id}.json"):
            user_doc = {
                "id" : id,
                "name" : name,
                "email": email,
                "profile_pic" : profile_pic
            }
        else:
            with open(f"data/{id}.json", "r") as f:
                user_doc = json.load(f)
            self.premium = True
            self.solved = user_doc["solved"]
        self.id = user_doc['id']
        self.name = user_doc['name']
        self.email = user_doc['email']
        self.profile_pic = user_doc['profile_pic']
        with open(f"data/{id}.json", "w") as f:
            json.dump(user_doc, f)

    @staticmethod
    def get(user_id):
        with open("data/students.json", "r") as f:
            users = json.load(f)
        user = next(filter(lambda user: user["id"] == user_id, users), "")

        return User(user['id'])

if __name__ == "__main__":
    with open(f"data/{id}.json", "r") as f:
        users = json.load(f)