def calfib(r):
    n = 1
    x = 0
    p = x
    for i in range(r):
        x = n
        n = (n + p)
        p = x
    return n



