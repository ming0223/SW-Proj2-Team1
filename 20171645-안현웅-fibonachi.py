import time

def fibonachi(n):
    if n == 1:
        return 0
    elif n == 0:
        return 0
    else:
        return fibonachi(n-1) + fibonachi(n-2)

def iterfibonachi(n):
    if n <= 1:
        return n
    else:
        current = 1
        last = 0
        for i in range(1, n):
            tmp = current
            current += last
            last = tmp
        return current



while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break

    ts = time.time()
    fibonumber = iterfibonachi(nbr)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibonachi(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
