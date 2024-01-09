#!/usr/bin/python3
import uuid
from datetime import datetime

dt_format = "%Y-%m-%dT%H:%M:%S"
"""
till we finish the class
"""


class BaseModel:
    """define the attributes and methods"""
    def __init__(self, *args, **kwargs):
        """
        """
        if kwargs: 
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['updated_at', 'created_at']:
                        setattr(self, key, datetime.strptime(value, dt_format))
                    else:
                        setattr(self, key, value)
        else:
            """
            these are the attributes for the basemodel
            """
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """updates the public instance attribute,
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the object to a dictionary representation.
        Returns:
            dict: A dictionary containing the object's attributes,
            class name, and ISO-formatted date strings.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

        return obj_dict

    def __str__(self):
        """Custom string representation of the object"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))
