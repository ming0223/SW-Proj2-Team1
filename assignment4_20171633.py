def Factorial(n):
	return 1 if n <= 1 else Factorial(n - 1) * n

def Combination(n, m) :
	if n <= m or m == 0 : return 1
	else : return Combination(n - 1, m) + Combination(n - 1, m - 1)

n = 0
m = 0

while(True) :

	try:
		n = int(input("Enter n: "))
		if (n == -1):
			break
		elif (n < -1):
			print("")
			continue
		m = int(input("Enter m: "))
		if (m == -1):
			break
		elif (m < -1):
			continue
		elif (m > n):
			print("m이 n보다 큽니다 다시 입력해 주세요")
			continue
	except IndexError:
		print("숫자로 입력해주세요")

	print("팩토리얼로 구현한 결과 조합의 수: ", (int)(Factorial(n) / (Factorial(m) * Factorial(n - m))))

	print("재귀함수로 구현한 결과 ", n, "중에서 ", m, "개를 고르는 조합의 수는 ", Combination(n, m))

