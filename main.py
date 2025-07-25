def fib(n):
    if n < 0:
        raise ValueError("Input must be a positive number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        grandparent = 0
        parent = 1
        current = 0
        for _ in range(2, n + 1):
            current = grandparent + parent
            parent, grandparent = current, parent
        return current
