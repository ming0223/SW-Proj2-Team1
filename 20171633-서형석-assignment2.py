while(1) :
	n = int(input("Enter a number: "))

	if(n == -1) : break	

	answer = 1

	for i in range(1, n+1):
		answer = answer * i;

	print(str(n)+"! = "+str(answer))
