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
    fibonumber = iterfibo(nbr)
    print("재귀로 구한 것이 아닌 피보나치 값 : %d" %(fibonumber))
    fibonumber = fibo(nbr)
    print("재귀로 구한 피보나치 값 : %d" %(fibonumber))
