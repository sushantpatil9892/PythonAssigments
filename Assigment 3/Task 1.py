def factorialnew(n):
    if n < 2:
        return 1
    else:
        a= 1
        for i in range(n, 2, -1):
            a = a * i
    return a * 2

factorialnew(10)