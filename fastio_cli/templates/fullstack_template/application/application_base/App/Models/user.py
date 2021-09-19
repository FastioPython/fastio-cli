from orator import Model
from orator.orm import has_many

from App.Database.db import Model

class UserObserver(object):

    def creating(self, model):
        pass

    def saving(self, model):
        pass

    def saved(self, model):
        pass


class User(Model):

    __fillable__ = [
        'email',
        'firstName',
        'id',
        'lastName',
        'password',
        'phone',
        'userStatus',
        'username',
        
    ]

    __dates__ = [
        
    ]

    __hidden__ = []

    __casts__ = {
        'email': 'str',
        'firstName': 'str',
        'id': 'int',
        'lastName': 'str',
        'password': 'str',
        'phone': 'str',
        'userStatus': 'int',
        'username': 'str',
        
    }


User.observe(UserObserver())