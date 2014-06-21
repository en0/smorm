from pymongo import MongoClient

class Client(MongoClient):

    """ Extending functionality of the MongoClient to support ORM models. """

    def find_one(self, model, *args, db=None):

        """ Retrieve the first record in the database that matches the provided args 
        
        Arguments:
            model - The Type of the model being requested.
            *args - Arguments to be sent to MongoCollection.find_one()
            db    - Override the model's definition about what database to search

        Returns:
            If successful, returns an instance of type model populated with the document record.
            else, None
        """

        ## Retrieve the database name
        db = db if db else model.__db_name__

        ## Retrieve the collection name
        collection_name = model.__collection_name__

        ## Retrieve the db.collection from the mongo client
        collection = self[db][collection_name]

        ## Find the document in the given mongo collection
        record = collection.find_one(*args)

        ## On failure, return None
        if not record: return None

        ## Create a instance of type model
        ret = model(db=db, **record)

        ## Set the connection details in the new instance.
        ret.__set_collection__(self)

        return ret

    def find(self, model, *args, db=None):

        """ Retrive a list of records from the database that match the provided args.

        Arguments:
            model - The type of the model being requested
            *args - Arguments to be sent to MongoCollection.find()
            db    - Override the model's defined db location

        Returns:
            If successfull, returns a list of instance models populated with the document records.
            else, an empty list.
        """

        ret = []

        ## Retrieve the database name
        db = db if db else model.__db_name__

        ## Retrieve the collection name
        collection_name = model.__collection_name__

        ## Retrieve the db.collection from the mongo client
        collection = self[db][collection_name]

        ## Find the document in the given mongo collection
        records = collection.find(*args)

        ## Loop through each result, create an instance and add to return
        for record in records:

            ## Create a instance of type model
            instance = model(db=db, **record)

            ## Set the connection details in the new instance.
            instance.__set_collection__(self)

            ## Add to the return list
            ret.append(instance)

        return ret

    def add(self, model):

        """ Associate the given model to the mongo database.

        This function does not save the data, it only associates the model.
        To save call model.save()
        """

        ## Set the connection details in the new instance.
        model.__set_collection__(self)

