""" script to test of 'Oportunidade BackEnd RUBY' """
import math

def is_prime_number(number):
    """ check if number is um prime number """
    if number >= 2:
        for i in range(2, number):
            if not number % i:
                return False
    else:
        return False
    return True


def is_square(integer):
    """check if number have square """
    root = math.sqrt(integer)
    return bool(int(root + 0.5) ** 2 == integer)


def count_number_madic(list_number):
    """ Method to count numbers of 'number magic' in interval of two number integer """
    result = []
    for start, end in list_number:
        for number in range(start, end + 1):
            if is_square(number) and is_prime_number(int(math.sqrt(number))):
                result.append(number)

    return len(result)

