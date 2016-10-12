
def is_prime(number):
    '''A function that determines if a number is a Prime number'''

    for N in range(2, number, 1):
        if (number % N ) == 0:
            return False

    return True

def prime(input_data):
    '''A function that determines all Prime numbers that are less
     than or equal to a given number
     '''
    if not (isinstance(input_data, float)  or isinstance(input_data, int)):
        return "The argument passed to this function must be number"

    if input_data < 2:
        return []

    prime_numbers = []
    for number in range(3, input_data+1, 2):
        if  is_prime(number):
            prime_numbers.append(number)

    return [2] + prime_numbers


