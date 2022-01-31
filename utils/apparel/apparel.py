from entity import Entity

class Apparel(Entity):
    items = []

    def __init__(self, id, category, name, price, stock):
        self.id = id
        self.category = category
        self.name = name
        self.price = price
        self.stock = stock
    
    def load_items(root):
        Apparel.items = Apparel.load(root)

    def find_item(id):
        return Apparel.find(Apparel.items, int(id))

    def add_item(data):
        Apparel.validate_add(Apparel.items, int(data['id']))

        id = int(data['id'])
        apparel = Apparel(
            id, 
            data['category'], 
            data['name'], 
            int(data['price']), 
            int(data['stock']))
        Apparel.items.append(apparel)

    def update_item(id, data):
        item = Apparel.validate_update(Apparel.items, int(id))
        if 'category' in data:
            item.category = data['category']
        if 'name' in data:
            item.name = data['name']
        if 'price' in data:
            item.price = int(data['price'])
        if 'stock' in data:
            item.stock = int(data['stock'])
        
        return item

    def delete_item(id):
        item = Apparel.validate_delete(Apparel.items, int(id))
        Apparel.items.remove(item)

        return item
