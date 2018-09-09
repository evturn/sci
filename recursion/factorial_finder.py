def factorial_finder(n):
    if n <= 1:
        return 1

    return n * factorial_finder(n - 1)
