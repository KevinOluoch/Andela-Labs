def fibonnacci(max_number):
    '''A function to generate Fibonacci sequence from 0 to a given max Number'''

    if not (isinstance(max_number, float)  or isinstance(max_number, int)):
        return "The argument passed to this function must be number"

    if max_number < 0:
        return "The argument passed to this function must be a positive number"

    if max_number == 0: return [0]

    i=0
    j=1
    fibonnacci_sequence=[0,1]
    while True:
        fibonnacci_sequence.append(i + j)
        (i, j)=(j, j + i)
        if not (j + i) <= max_number:
            break

    return fibonnacci_sequence