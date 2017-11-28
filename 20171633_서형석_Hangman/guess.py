class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = ""
        self.numTries = 0
        self.currentStatus = '_' * len(self.secretWord)

    def display(self):

        print("Current: %s" %self.currentStatus)
        print("Tries: " + str(self.numTries))


    def ChangeStr(self, character, place) :
        str = ""

        for i in range(0, len(self.currentStatus)) :
            if(i in place) :
                str += character
            else :
                str += self.currentStatus[i]

        return str

    def guess(self, character):
        try :
            if character in self.secretWord :
                count = 0
                list = []
                findPlace = self.secretWord.find(character, count)
                while(findPlace != -1) :
                    findPlace = self.secretWord.find(character, count)
                    list.append(findPlace)
                    count = findPlace + 1

                self.currentStatus = self.ChangeStr(character, list)

            else :
                self.numTries += 1
        except :
            print("Error!")

        self.guessedChars += character

        if(self.secretWord == self.currentStatus) :
            return True
        else :
            return False
