def fac(n):         #factorial 계산
    f=1
    for i in range(1, n+1):
        f=f*i
    return f

def Cf(n, m):           #factorial을 이용한 조합의 수 계산
    answer = int(fac(n)/(fac(m)*fac(n-m)))
    return answer

def C(n, m):        #재귀함수를 이용한 조합의 수 계산
    if n==m:
        return 1
    elif m==0:
        return 1
    elif m<0:
        return 0
    answer= C(n-1, m-1)+ C(n-1, m)
    return answer

#main 함수    
n=int(input("Enter n:"))
m=int(input("Enter m:"))

if (n>=m and m>=0):
	print("Cf(%d,%d)=" %(n, m), Cf(n,m))
	print("C(%d,%d)=" %(n, m), C(n,m))
else:
	print("다시 입력해주세요!")
