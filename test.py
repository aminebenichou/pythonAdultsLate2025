import json
import random
class User:
    name=""
    age=0
    username=""
    email=''

    def __init__(self, name, email):
        self.name=name
        self.email=email

    def __str__(self):
        return self.name
    

    def get_age(self, age_range: list):
         if age_range[0] < self.age <age_range[1]:
              return True
    

users: list[User] =[]
with open('names.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for element in data:
            user=User(name=element['first_name'], email=element['email'])

            user.age=random.randint(15, 100)
            users.append(user)


for user in users:
    if user.get_age([25, 45]):
        print(user.email)