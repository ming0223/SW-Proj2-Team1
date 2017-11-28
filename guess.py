class Guess:

    def __init__(self, word):
        self.numTries = 0
        self.secretWord = word
        self.guessedChars = []

        self.temp = []
        self.temp += "_"*len(self.secretWord)

        self.count = 0 #self.guessedChars의 인덱스 값을 알기 위한 변수
        self.find = 0 #같은 알파벳이 2번이상 쓰이는 단어가 나올 경우
                      # find : 각 알파벳들의 인덱스값을 알기 위한 변수

        self.currentStatus = "_"*len(self.secretWord)


    def display(self):
        print("Current: " + self.currentStatus)
        print("Tries : " + str(self.numTries))



    def guess(self, character):
        alp=character.lower()
        if alp.isalpha():         #알파벳만 입력 가능
            self.guessedChars += alp # self.guessedChars 에 소문자 알파벳 추가

            # 만약 self.guessdChars의 self.count번째 인덱스가 self.secreWord안에 있다면 if문을 통과
            if self.guessedChars[self.count] in self.secretWord:
                self.find = self.secretWord.find(alp) # self.secretWord에서 알파벳의 인덱스 값을 찾음
                self.temp[self.find] = alp # 찾은 self.find의 정수를 더미 리스트의 인덱스 값으로하여 입력받은 알파벳을 삽입
                self.currentStatus = "".join(self.temp) # 더미 리스트를 스트링으로 변환

                # 만약 self.secreWord에 같은 알파벳이 두개 이상 존재하는 단어일시 실행
                # find 메쏘드는 찾는 알파벳이 존재하지 않을 시 -1을 리턴하므로 범위를 아래처럼 함
                while (self.secretWord[self.find + 1:]).find(alp) != -1:
                    self.find = self.secretWord[self.find + 1:].find(alp) + self.find + 1
                    self.temp[self.find] = alp
                    self.currentStatus = "".join(self.temp)
                # 정상적으로 if 문이 실행되었을 때 self.count를 +1 하여 self.guessChars의 인덱스 값을 다음 입력받은 알파벳으로 출력
                self.count += 1
            else:
                self.numTries += 1 # 시도 횟수 1 증가
                self.count += 1 # self.count를 +1 하여 self.guessChars의 인덱스 값을 다음 입력받은 알파벳으로 출력
        else :
            print("Enter a valid alphabet.") # 알파벳이 아닌 문자를 입력 했을 때 처리

        if self.currentStatus == self.secretWord :
            return True

