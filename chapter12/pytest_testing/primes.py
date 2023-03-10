def is_prime(number):
    if number < 2:
        return False
    for element in range(2, number):
        if number % element == 0:
            return False

    return True
