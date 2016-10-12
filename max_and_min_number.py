
def find_max_min(input_list):
    """ This function takes a list of numbers, and returns an array containing
    the min and max number, respectively, or its length if all the list items
     are of the same value.
    First the input is confirmed to be list.
    The list is then checked to ensure it is none empty and that all its items
     are numbers.
     An appropriate responce is returned for all these senarios.
    """

    if not isinstance(input_list, list):
        return "The argument should be a list. "
    if not input_list: return [0,]
    checked_list = [item for item in input_list if isinstance(item, (int, float))]
    if not input_list == checked_list:
        return "The argument list contains none digit(s) item(s). "

    if max(input_list)==min(input_list):
        return [len(input_list)]
    return [ min(input_list), max(input_list) ]

print find_max_min([6,8])