def is_prime(num):
    if num == 2:
        return True
    for i in range(2, num):
        if num % i != 0:
            continue
        else:
            return False
    return True

print(is_prime(11))