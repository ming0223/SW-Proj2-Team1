import pickle

dbfilename = 'assignment3_20171633.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
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
    while (True):
        inputstr = (input("Score DB > ")) #입력
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add': #새로운 사람 추가
            try :
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]
            except IndexError:
                print("이름, 나이, 점수 순으로 다시 입력해주세요")
                continue
        elif parse[0] == 'del': #지정한 사람 삭제
            try:
                new = scdb[:]
                for p in new:
                    if p['Name'] == parse[1]:
                         scdb.remove(p)
            except IndexError:
                print("삭제하실 이름을 입력해주세요")
                continue
        elif parse[0] == 'show': #전체 내용
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit': #프로그램 종료
            break
        elif parse[0] == 'find': #주어진 사람 찾기
            try:
                Check = False
                for p in scdb:
                    if p['Name'] == parse[1]:
                        print(p)
                        Check = True
                if Check :
                    print("이름을 찾을 수 없습니다")
            except IndexError:
                print("찾으실 이름을 입력해주세요")
                continue
        elif parse[0] == 'inc': #주어진 사람 찾아서 Score를 amout만큼 더해줌
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        if(p['Score'] + int(parse[2]) < 0) :
                            p['Score'] = "0"
                        else :
                            p['Score'] = str(int(p['Score']) + int(parse[2]))
            except IndexError:
                print("이름과 추가할 점수를 입력해주세요")
                continue
        elif parse[0] == 'FindNA':
            try :
                for p in scdb:
                    if p['Name'] == parse[1] and p['Score'] == parse[2]:
                        print(p)
            except IndexError :
                print("찾을 이름과 나이를 입력해주세요")
                continue
        elif parse[0] == 'Best':
            Max = 0
            for p in scdb:
                if int(p['Score']) > Max :
                    Max = int(p['Score'])
            for p in scdb:
                if int(p['Score']) == Max :
                    print(p)
        else:
            print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)


