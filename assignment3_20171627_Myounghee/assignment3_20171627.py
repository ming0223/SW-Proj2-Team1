import pickle

dbfilename = 'assignment3_20171627.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "":
            continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':	#정보 수 잘못 입력 했을 때의 오류 해결
                try:
                    record = {'Name':parse[1], 'Age':int(parse[2]), 'Score':int(parse[3])}
                    scdb += [record]
                except IndexError as e:                     #예외처리
                    print("추가할 정보를 모두 입력해 주세요.")
                except ValueError as e:                         #예외처리
                    print("Age와 Score는 정수로 입력해주세요.")
                else :                           #정상 작동
                    print("추가되었습니다!")

        elif parse[0] == 'del':
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            findScoreDB(scdb, parse[1])
        elif parse[0] == 'inc':
            for p in scdb:
                if p['Name'] == parse[1]:
                    incScoreDB(scdb, parse[1], parse[2])
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])

#show
def showScoreDB(scdb, keyname):
    try:
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + str(p[attr]), end=' ')
            print()
    except KeyError as e:               # 예외처리
        print("show만 입력 하세요!")

#find
def findScoreDB(scdb, pname):
      for p in scdb:
            if p['Name'] == pname:
                for attr in p:
                    print( attr + "=" + str(p[attr]), end=' ')
                print()

#inc
def incScoreDB(scdb, pname, amount):
    try:
        for p in scdb:
            if p['Name']==pname:
                p['Score']=int(p['Score'])+int(amount)
                p['Score']=str(p['Score'])
    except ValueError as e:                             #예외처리
        print("추가하려는 Score는 정수로 입력해주세요!")

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

