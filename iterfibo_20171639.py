import time
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1) + fibo(n-2)
def iterfibo(n): #재귀함수 쓰지말고
    before =0
    current = 1

    if n ==0:
        return 0
    elif n ==1:
        return 1
    else:
        for i in range(1,n):
            temp = current
            current = before + current
            before = temp
        return current

while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber = iterfibo(nbr)
    ts = time.time() -ts
    print("IterFibo (%d) = %d, time %.6f" % (nbr, fibonumber, ts))
    ts = time.time()
    fibonumber = fibo(nbr)
    ts = time.time() -ts
    print("Fibo(%d) = %d, time %.6f" % (nbr, fibonumber, ts))
