from entity import Entity
from dateutil import parser

class User(Entity):
    items = []

    def __init__(self, id, name, username, email, company, lat, long, apiKey, role, lastUpdate):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.company = company
        self.lat = lat
        self.long = long
        self.apiKey = apiKey
        self.role = role
        self.lastUpdate = lastUpdate

    def load_items(root):
        User.items = User.load(root)

    def find_item(id):
        return User.find(User.items, id)

    def add_item(data):
        User.validate_add(User.items, data['id'])

        id = data['id']
        user = User(
            id,
            data['name'],
            data['username'],
            data['email'],
            data['company'],
            float(data['lat']),
            float(data['long']),
            data['apiKey'],
            data['role'],
            None)
        User.items.append(user)

    def update_item(id, data):
        item = User.validate_update(User.items, id)
        if 'name' in data:
            item.name = data['name']
        if 'username' in data:
            item.username = data['username']
        if 'email' in data:
            item.email = data['email']
        if 'company' in data:
            item.company = data['company']
        if 'lat' in data:
            item.lat = float(data['lat'])
        if 'long' in data:
            item.long = float(data['long'])
        if 'apiKey' in data:
            item.apiKey = data['apiKey']
        if 'role' in data:
            item.role = data['role']
        
        return item

    def delete_item(id):
        item = User.validate_delete(User.items, id)
        User.items.remove(item)

        return item
