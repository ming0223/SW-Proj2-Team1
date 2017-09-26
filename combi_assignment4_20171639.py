n = int(input("Enter n: "))
m = int(input("Enter m: "))
sum = 0
def factorial(n):
    answer = 1
    for i in range(1,n+1):
        answer = answer*i
    return answer

while ((n>0) or (m>=0)):
    def C(n,m):
        if m == 0:
            return 1
        if n == m:
            return 1
        else:
            return C(n-1,m) + C(n-1,m-1)

    def CF(n,m):
        sum = factorial(n)/(factorial(m)*factorial(n-m))
        return sum

    print("CF(%d,%d) = %d" %(n,m, CF(n,m)))
    print("C(%d,%d) = %d" %(n, m, C(n,m)))

    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

