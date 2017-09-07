while (True):   
    num= int(input("Enter a number:"))      # 숫자입력받기
    if num==-1:     #-1을 넣으면 프로그램이 꺼짐
        break
    elif num<0:        #음수일 때 예외처리
        print("다시 입력하세요")
    else:       
        fac=1       
        for i in range(1, num+1):       #팩토리얼 계산 루프문
            fac=i*fac
        print(str(num)+"!="+str(fac))
