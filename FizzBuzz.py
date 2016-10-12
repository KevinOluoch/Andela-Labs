def fizz_buzz (input_data):
    """This function checks if a number is divisible by, 3, 5, both 3 and 5,
    or neither 3 or 5, and returns 'Fizz', 'Buzz', 'FizzBuzz', or the
    number it receives, respectively.
    If the argument is not a number. it will return the argument.
    """


    if not (isinstance(input_data, float)  or isinstance(input_data, int)):
        return input_data

    if not (input_data % 3 or input_data % 5):
        return "FizzBuzz"
    elif not (input_data % 3):
        return "Fizz"
    elif not (input_data % 5):
        return "Buzz"
    else: return input_data

