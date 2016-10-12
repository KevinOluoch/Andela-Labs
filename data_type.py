
def data_type(data):
    """A Function that takes one argument. Compares and returns results, based
    on the argument supplied to the function.
        -For strings, it returns its length.
        -For None, it returns the string 'no value'
        -For booleans, it returns the boolean given as the argument
        -For integers, it  returns a string showing how it compares
         to one hundred e.g. For 67 it returns 'less than 100'
         for 4034 it returns 'more than 100'
         and for 100 it returns 'equal to 100'.
        -For lists it returns the 3rd item, or None if the lenght of
         the list is less than 3.
    """


    if type(None) == type(data):
         return "no value"

    elif isinstance(data, str):
         return len(data)

    elif isinstance(data, bool):
         return data

    elif isinstance(data, int):
        if data < 100 :
             return "less than 100"
        elif data > 100 :
             return "more than 100"
        else:
            return "equal to 100"

    elif isinstance(data, list):
        if len(data) < 3 :
            return None
        else:
            return data[2]

    else: pass


