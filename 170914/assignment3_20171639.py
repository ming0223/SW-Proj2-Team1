import pickle

dbfilename = 'assignment3.dat'

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
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")

        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except IndexError:
                continue

        elif parse[0] == 'find':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in sorted(p):
                            print(attr + "=" + p[attr], end=' ')
                        print()
            except IndexError:
                continue

        elif parse[0] == 'inc':
            try:
                amount = int(parse[2])
                for p in scdb:
                    if p['Name'] == parse[1]:
                    #p[3] = p[3] + amount  #int int 로 더한다음 전체를 str()
                    #p['Score'] = int(p['Score']) + int(amount)
                        p['Score'] = int(p['Score'])
                        p['Score'] = p['Score'] + amount
                        p['Score'] = str(p['Score'])
            except IndexError:
                continue

        elif parse[0] == 'del':
            try:
                new = scdb[:]
                for p in new:

                    if p['Name'] == parse[1]:
                            scdb.remove(p)
            except IndexError:
                continue

        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()
def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()



scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

