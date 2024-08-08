def is_prime(num: int) -> bool:
    """Check if a positive integer is prime

    :param num: positive integer
    :return: Returns True if the number is prime, otherwise returns False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return num != 1