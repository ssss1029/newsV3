
import collections
import logging
import sys

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

def query_yes_no(question, default=None):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
