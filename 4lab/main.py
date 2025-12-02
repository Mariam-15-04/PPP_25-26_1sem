import re
import json
from typing import List, Optional

class User:
    def __init__(self, uid: int, name: str, email: str):
        self.uid = uid
        self.name = name
        self.email = email
    
    def is_valid_email(self) -> bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, self.email) is not None
    
    def __str__(self):
        return f"{self.name} {self.email}"

class UserCollection:
    def __init__(self):
        self.users = []
    
    def add_from_csv(self, data: str):
        parts = data.split(';')
        if len(parts) == 3:
            uid = int(parts[0])
            name = parts[1]
            email = parts[2]
            self.users.append(User(uid, name, email))
    
    def add_from_json(self, data: str):
        obj = json.loads(data)
        uid = obj['uid']
        name = f"{obj['first_name']} {obj['last_name']}"
        email = obj['contacts']['email']
        self.users.append(User(uid, name, email))
    
    def add_from_raw(self, data: str):
        parts = data.split()
        name = ' '.join(parts[:-1])
        email = parts[-1]
        self.users.append(User(hash(data) % 10000, name, email))
    
    def add_user(self, data: str):
        if data.startswith('csv '):
            self.add_from_csv(data[4:])
        elif data.startswith('json '):
            self.add_from_json(data[5:])
        elif data.startswith('raw '):
            self.add_from_raw(data[4:])
    
    def get_emails(self):
        return [user.email for user in self.users]
    
    def find_by_name(self, name):
        return [user for user in self.users if name.lower() in user.name.lower()]
    
    def get_invalid_emails(self):
        return [user for user in self.users if not user.is_valid_email()]

collection = UserCollection()

inputs = [
    "csv 123;Иван Иванов;ivan@example.com",
    "json {\"uid\": 42, \"first_name\": \"Petr\", \"last_name\": \"Petrov\", \"contacts\": {\"email\": \"petr@example.com\"}}",
    "raw Иванов Иван ivanov@example.com"
]

for data in inputs:
    collection.add_user(data)

commands = ["emails", "find name=Иван", "invalid"]

for cmd in commands:
    print(f"\nКоманда: {cmd}")
    
    if cmd == "emails":
        emails = collection.get_emails()
        for email in emails:
            print(email)
    
    elif cmd.startswith("find name="):
        name = cmd.split('=')[1]
        users = collection.find_by_name(name)
        for user in users:
            print(user)
    
    elif cmd == "invalid":
        invalid_users = collection.get_invalid_emails()
        for user in invalid_users:
            print(user)

print(f"\nСтатистика:")
print(f"Всего пользователей: {len(collection.users)}")
valid_emails = len([u for u in collection.users if u.is_valid_email()])
print(f"Валидных email: {valid_emails}")
print(f"Невалидных email: {len(collection.users) - valid_emails}")
