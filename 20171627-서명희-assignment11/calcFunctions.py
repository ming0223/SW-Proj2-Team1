from math import factorial as fact

def factorial(numStr):  #math 모듈이 아닌 for문을 이용한 계산
    try:
        num = int(eval(numStr))  # 숫자 정수로 변환    #eval 함수를 씀으로서 괄호안의 계산이 에러처리 되지 않고 계산 됨
        if num < 0:
            r='Error!'
        else:
            r = 1
            for i in range(1, num + 1):  # 팩토리얼 계산 루프문
                r = i * r
    except:
        r='Error!'
    return str(r)

def decToBin(numStr):
    try:
        n = int(eval(numStr))       #괄호 안의 수도 계산되게 수정
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'
