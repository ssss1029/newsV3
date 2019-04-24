
import collections
import logging

logger = logging.getLogger(__name__)

def testLogger(string):
    logger.debug(string)

def copy_dict_shallow(d):
    """
    Make a shallow copy of the given dict, while checking if all keys and values are hashable
    """
    result = dict()
    for key, value in d:
        key_hashable = isinstance(key, collections.Hashable)
        value_hashable = isinstance(value, collections.Hashable)

        if not key_hashable or not value_hashable:
            raise ValueError("{0} : {1} is not hashable".format(key, value))
        else:
            result[key] = value

    return result