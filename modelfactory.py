from .base import Base

def ModelFactory(collection, db=None):

    """ Create a new model for the given db.collection.

    The DB is optional but in this case the db MUST be provided
    at the construction of the base class.  This is optional so
    you can shard collections between diffrent dbs

    Arguments:
        collection - The name of the mongo collection
        db - the name of the mongo db

    Returns:
        A new type for this model.
    """

    ## Create the new type and bind support functions
    return type(db+collection, (Base,), {
        #'__init__':__init__,
        '__collection_name__':collection,
        '__db_name__':db,
    })

