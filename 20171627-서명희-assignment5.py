import time
import random

def iterfibo(n):
    if n<= 1:
        return n
    else:
        a=0; b=1
        for i in range(1, n):
            k=b
            b=a+b
            a=k
        return b
def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)


while True:
	nbr = int(input("Enter a number: "))
	if nbr == -1:
		break
	ts = time.time()
	fibonumber = iterfibo(nbr)
	ts = time.time() - ts
	print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
	ts = time.time()
	fibonumber = fibo(nbr)
	ts = time.time() - ts
	print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
