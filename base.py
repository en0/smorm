
class Base(object):

    """ Base class for all mongo ORM Models. """

    def __init__(self, db=None, **kwargs):

        """ Fill base with data provided in kwargs.

        Arguments:
            kwargs - The key/value pairs of the document
        """

        if db:
            self.__db_name__ = db

        for k,v in kwargs.items():
            setattr(self, k, v)


    def save(self):

        """ Write changes back to the database """

        if hasattr(self, '_id'):
            value = self.__strip__()
            self.__collection__.update({'_id':self._id}, value)
        else:
            value = self.__strip__()
            self._id = self.__collection__.insert(value)

    def remove(self):

        """ Remove the document for the database """

        if hasattr(self, '_id'):
            print('would remove')

    def __get_collection__(self):

        """ Retrieve the connection to the collection used by this model. """

        return self.__collection__

    def __set_collection__(self, client):

        """ Set the connection to the collection used by this model. """

        db = client[self.__db_name__]
        self.__collection__ = db[self.__collection_name__]

    def __strip__(self):

        """ Return only the mongo document portion of this model """

        ref = self.__dict__
        return dict((k,ref[k]) for k in ref if not k.startswith('__') and not k.endswith('__'))

