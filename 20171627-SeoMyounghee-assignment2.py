num=0
while num!= -1:
    num= int(input("Enter a number:"))
    if num==-1:
        break
    elif num<0:
        print("다시 입력하세요")
    else:
        fac=1
        for i in range(1, num+1):
            fac=i*fac
        print(str(num)+"!="+str(fac))

