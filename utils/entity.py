from jsonpickle import decode
from flask import json

class Entity:
    @classmethod
    def load(cls, root):
        fileName = f"{cls.__name__}/{cls.__name__}.json".lower()
        handle = open(fileName)
        json_data = json.load(handle)

        list_data = []
        clsName = f"{cls.__module__}.{cls.__name__}"
        for item in json_data[root]:
            item.update({"py/object": clsName})
            list_data.append(decode(json.dumps(item)))
        
        return list_data
    
    def find(items, id):
        items_filtered = [item for item in items if item.id == id]
        if(len(items_filtered) == 0):
            return None
        return items_filtered[0]
    
    def validate_add(items, id):
        items_filtered = [item for item in items if item.id == id]
        if(len(items_filtered) > 0):
            raise f"Apparel with id={id} exists!"

    def validate_update(items, id):
        items_filtered = [item for item in items if item.id == id]
        if(len(items_filtered) == 0):
            raise f"Apparel with id={id} not found!"

        return items_filtered[0]

    def validate_delete(items, id):
        items_filtered = [item for item in items if item.id == id]
        if(len(items_filtered) == 0):
            raise f"Apparel with id={id} not found!"

        return items_filtered[0]

