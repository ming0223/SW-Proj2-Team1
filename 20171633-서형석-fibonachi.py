import time

def iterfibo(n) :
    f1 = 0
    f2 = 1
    switch = False
    count = 2

    while(count <= n) :

        if(switch) :
            f2 = f1 + f2
            switch = False
        else :
            f1 = f1 + f2
            switch = True
        count = count + 1

    if(switch) :
        return f1
    else :
        return f2

def fibo(n):
    if(n <= 1) : return n
    return fibo(n - 1) + fibo(n - 2)

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() - ts
    print("IterFibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() - ts
    print("Fibo(%d) = %d, time %.6f" %(nbr, fibonumber, ts))
