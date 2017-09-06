n = -1

while(n < 0) :
	n = int(input("Enter a number: "))

answer = 1

for i in range(1, n+1):
	answer = answer * i;

print(str(n)+"! = "+str(answer))
