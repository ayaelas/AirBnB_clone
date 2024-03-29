#!/usr/bin/python3

"""Define a class"""
from models.base_model import BaseModel

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json


class FileStorage:
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    """
    FileStorage class for serializing and
    deserializing instances to a JSON file.
    """
    __file_path = "youssef.json"
    __objects = {}

    def all(self):
        """
        Returns a dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj is not None:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """
        Serializes `__objects` to the JSON file
        """
        objs = {}
        for k in self.__objects:
            objs[k] = self.__objects[k].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(objs, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key in loaded_objects:
                    self.__objects[key] = FileStorage.classes[
                        loaded_objects[key]["__class__"]](
                            **loaded_objects[key])
        except Exception as e:
            pass
