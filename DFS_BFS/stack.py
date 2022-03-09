result = 1


def factorial(n):
    print(n, "* ", n - 1)
    if n <= 1:
        return 1
    return n * factorial(n - 1)
