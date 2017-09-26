def factorial(n, m):
    if (n == m):
        return result + 1
    elif (m == 0):
        return result +1
    else:
        return factorial(n - 1, m) + factorial(n - 1, m - 1)
        print(factorial(n, m))

def solution(n, m):
    num1 = 1
    num2 = 1
    num3 = 1
    for i in range(1, n+1):
        num1 *= i
    for j in range(1, m+1):
        num2 *= j
    for k  in range(1, n-m+1):
        num3 *= k
    answer = num1 / (num2 * num3)
    return answer
a = int(input("number 1: "))
b = int(input("number 2: "))
c = solution(a,b)
print(c)