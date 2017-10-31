import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()
        self.textedit = QTextEdit()
        self.lineedit = QLineEdit()

        self.name = QLineEdit()
        self.age = QLineEdit()
        self.score = QLineEdit()
        self.amount = QLineEdit()
        self.key = QComboBox()
        self.key.addItem("Name")
        self.key.addItem("Age")
        self.key.addItem("Score")

        self.dbfilename = 'assignment6.dat'
        self.scoredb = self.readScoreDB()


        self.initUI()

        def initUI(self):
        name = QLabel("Name: ")
        age = QLabel("Age: ")
        score = QLabel("Score: ")
        amount = QLabel("Amount: ")
        key = QLabel("Key: ")

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.keyCombo = QComboBox()
        self.keyCombo.addItems(["Name", "Age", "Score"])


        addButton = QPushButton("Add", self)
        delButton = QPushButton("Del", self)
        findButton = QPushButton("Find", self)
        incButton = QPushButton("Inc", self)
        showButton = QPushButton("Show", self)

        shbox = QHBoxLayout()
        thbox = QHBoxLayout()
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        tvbox = QVBoxLayout()

        result = self.textedit

        shbox.addStretch(1)
        shbox.addWidget(name)
        shbox.addWidget(self.nameEdit)
        shbox.addWidget(age)
        shbox.addWidget(self.ageEdit)
        shbox.addWidget(score)
        shbox.addWidget(self.scoreEdit)
        thbox.addStretch(1)
        thbox.addWidget(amount)
        thbox.addWidget(self.amountEdit)
        thbox.addWidget(key)
        thbox.addWidget(self.keyCombo)
        hbox.addStretch(1)
        hbox.addWidget(addButton)
        hbox.addWidget(delButton)
        hbox.addWidget(findButton)
        hbox.addWidget(incButton)
        hbox.addWidget(showButton)
        vbox.addWidget(QLabel("Result: "))
        vbox.addWidget(result)

        addButton.clicked.connect(self.buttonClicked)
        delButton.clicked.connect(self.buttonClicked)
        findButton.clicked.connect(self.buttonClicked)
        incButton.clicked.connect(self.buttonClicked)
        showButton.clicked.connect(self.buttonClicked)

        tvbox.addLayout(shbox)
        tvbox.addLayout(thbox)
        tvbox.addLayout(hbox)
        tvbox.addLayout(vbox)

        self.setLayout(tvbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def buttonClicked(self):
        sender = self.sender()

        command = {
            'add': "{0} {1} {2} {3} {4}".format(sender.text().lower(), self.name.text(), self.age.text(),
                                                self.score.text(), self.key.currentText()),
            'del': "{0} {1} {2}".format(sender.text().lower(), self.name.text(), self.key.currentText()),
            'find': "{0} {1} {2}".format(sender.text().lower(), self.name.text(), self.key.currentText()),
            'inc': "{0} {1} {2} {3} {4}".format(sender.text().lower(), self.name.text(), self.age.text(),
                                                self.amount.text(), self.key.currentText()),
            'show': "{0} {1}".format(sender.text().lower(), self.key.currentText())
        }

        user_input = command[sender.text().lower()]

        realCommand = {
            'show': self.showScoreDB,
            'add': self.addDB,
            'inc': self.incDB,
            'find': self.findDB,
            'del': self.delDB
        }

        self.textedit.append(user_input)
        realCommand[sender.text().lower()](user_input)
        pass

    def showScoreDB(self, user_input):
        command, key = user_input.split(" ")
        tmp = sorted(self.scoredb, key=lambda row: row[key])
        for row in tmp:
            strm = ""
            for info in row:
                strm += str(info) + "=" + str(row[info]) + "\t"
                pass
            self.textedit.append(strm)
            pass
        self.textedit.append("\n")
        pass

    def addDB(self, user_input):
        command, name, age, score, key = user_input.split(" ")
        try:
            record = {'Name': name, 'Age': int(age), 'Score': int(score)}

            self.scoredb += [record]

        except:
            print("Please rewrite")

        pass

    def incDB(self, user_input):

        command, name, age, amount, key = user_input.split(" ")

        try:
            for p in self.scoredb:
                if p['Name'] == name:
                    p['Score'] = str(int(p['Score']) + int(amount))
        except:
            print("Please rewrite")

    def findDB(self, user_input):
        command, name, key = user_input.split(" ")
        for i in self.scoredb:
            if i['Name'] == name:
                result = ""
                for attr in sorted(i):
                    result += attr + "=" + str(i[attr]) + "\t"

                self.textedit.append(result)

    def delDB(self, user_input):
        command, name, key = user_input.split(" ")
        del_list = []
        for p in self.scoredb:
            if p['Name'] == name:
                del_list.append(p)

        for count in range(len(del_list)):
            self.scoredb.remove(del_list[count])

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB: ", self.dbfilename)
            return []

        scdb = []
        try:
            scdb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()
        return scdb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
