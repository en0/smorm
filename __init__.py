
""" Simple Mongo ORM.

This module creates a simple Model class for use with mongodb.
You can define your own models using the ModelFactory or 
deriving from ModelBase and manage them using the Client
object which is a MongoClient extention.

Examples: 

## Create Document Example:
from smorm import Client, ModelFactory

## Create a new model backed by mydb.mycollection.
MyDocument = ModelFactory('mycollection', 'mydb')

if __name__ == "__main__":

    ## Connect to a local mongodb instance
    client = Client()

    ## create a new document
    new_document = MyDocument(
        name='message', 
        data='This is a new document create by smorm
    )

    ## Associate the document with the client
    client.add(new_document)

    ## Sve the document
    new_document.save()

----------------------------------------------------

## Find Document Example
from smorm import Client, ModelFactory

## Create a new model backed by mydb.mycollection.
MyDocument = ModelFactory('mycollection', 'mydb')

if __name__ == '__main__':

    ## Connect to a local mongodb instance
    client = Client()

    ## Find a document
    message = client.find_one(MyDocument, {'name' : 'message'})

    ## Update a value
    message.data = "This message has been modified"

    ## Save the changes
    message.save()

----------------------------------------------------

## Without ModelFactory Example

## This is supported so you can add business logic to your models
## NOTE: the property names cannot be the same as the attribute names.

from smorm import ModelBase

class MyDocument(ModelBase):

    __collection_name__ = 'mycollection'
    __db_name__ = 'mydb'

    @property
    def Name(self):
        return self.name

    @Name.setter
    def Name(self, val):
        self.name = val.title()

    @property
    def Data(self):
        return self.data

    @Data.setter
    def Data(self, val):
        self.data = val

----------------------------------------------------
"""

from .client import Client
from .modelfactory import ModelFactory
from .base import Base as ModelBase

__all__ = [ 'Client', 'ModelFactory', 'ModelBase' ]

