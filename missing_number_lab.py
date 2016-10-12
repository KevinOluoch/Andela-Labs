def find_missing( list1, list2 ):
    """When presented with two arrays, all containing positive integers,
    with one of the arrays having one extra number, it returns the extra number
    as shown in examples below:
        [1,2,3] and [1,2,3,4] will return 4
        [4,66,7] and [66,77,7,4] will return 77
    """
    #The lists are checked to ensure none of them is empty and if they are equal
    if list1 == list2 or not (list1 or list2):
        return 0

    #If list1 is the larger one, the process of checking for the extra number is reversed
    if len(list1) > len (list2):
        return [ x for x in list1 if x not in list2 ][0]

    return [ x for x in list2 if x not in list1 ][0]

print find_missing ( [66,77,7,4], [4,66,7]  )
print find_missing ( [1,2,3], [1,2,3,4] )