n=int(input("Enter a number: "))
mul=1
if n >= 0 :
	for i in range(1,1+n):
		mul=mul*i
	print("%d! = %d"%(n,mul))
