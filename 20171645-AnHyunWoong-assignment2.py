while (True):
    fac = 1
    num = int(input("Input Number: "))
    if(num == -1):
     break
    elif(num < 0):
     print("REType Number")
    else:
     for i in range (1, num+1):
      fac *= i
     print(str(num) + "!=" + str(fac))
