
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
    for key, value in d.items():
        key_hashable = isinstance(key, collections.Hashable)
        value_hashable = isinstance(value, collections.Hashable)

        if not key_hashable or not value_hashable:
            raise ValueError("{0} : {1} is not hashable".format(key, value))
        else:
            result[key] = value

    return result

def copy_dict_deep(d):
    """
    Recursively make a deep copy of the given dictionary. All keys and values must be hashable
    """
    result = dict()
    for key, value in d.items():
        key_hashable = isinstance(key, collections.Hashable)
        value_hashable = isinstance(value, collections.Hashable)

        if isinstance(value, dict) and key_hashable:
            result[key] = copy_dict_deep(d[key])
        elif key_hashable and value_hashable:
            result[key] = value
        else:
            raise NotImplementedError("{0} : {1} is not implemented".format(key, value ))
    
    return result