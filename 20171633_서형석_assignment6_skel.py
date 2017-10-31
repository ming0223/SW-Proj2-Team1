import pickle
import sys
from operator import itemgetter
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt

class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 550, 300)
        self.lblname = QLabel("Name:", self)
        self.lblname.move(30, 30)
        self.lblAge = QLabel("Age:", self)
        self.lblAge.move(190, 30)
        self.lblScore = QLabel("Score:", self)
        self.lblScore.move(340, 30)
        self.lblAmount = QLabel("Amount:", self)
        self.lblAmount.move(230, 60)
        self.lblKey = QLabel("Key:", self)
        self.lblKey.move(400, 60)
        self.lblResult = QLabel("Result:", self)
        self.lblResult.move(30, 120)

        self.editname = QLineEdit(self)
        self.editname.move(75, 27)
        self.editage = QLineEdit(self)
        self.editage.move(225, 27)
        self.editscore = QLineEdit(self)
        self.editscore.move(385, 27)
        self.editAmount = QLineEdit(self)
        self.editAmount.move(285, 57)

        self.textResult = QTextEdit(self)
        self.textResult.move(30, 142)
        self.textResult.resize(465, 150)

        add_button = QPushButton("Add", self)
        add_button.move(75, 87)
        del_button = QPushButton("Del", self)
        del_button.move(160, 87)
        find_button = QPushButton("Find", self)
        find_button.move(245, 87)
        inc_button = QPushButton("Inc", self)
        inc_button.move(330, 87)
        show_button = QPushButton("show", self)
        show_button.move(415, 87)

        add_button.clicked.connect(self.buttonClicked)
        del_button.clicked.connect(self.buttonClicked)
        find_button.clicked.connect(self.buttonClicked)
        inc_button.clicked.connect(self.buttonClicked)
        show_button.clicked.connect(self.buttonClicked)

        self.key_Box = QComboBox(self)
        self.key_Box.addItem("Name")
        self.key_Box.addItem("Score")
        self.key_Box.addItem("Age")
        self.key_Box.move(432, 57)

        self.setWindowTitle('Assignment6')    
        self.show()

    def buttonClicked(self):
        sender = self.sender()

        if sender.text() == "Add" :
            self.Add()
        elif sender.text() == "Del" :
            self.Delete()
        elif sender.text() == "Find" :
            self.Find()
        elif sender.text() == "Inc" :
            self.Increase()
        elif sender.text() == "show" :
            self.Show()

    def Add(self):
        self.dict = {"Age" : int(self.editage.text()), "Name" : self.editname.text(), "Score" : int(self.editscore.text())}
        self.scoredb.append(self.dict)

        self.str = ""

        for i in range(0, self.scoredb.__len__()):
            self.str += "Age=" + self.scoredb[i].get("Age").__str__() + \
                        ((20 - self.scoredb[i].get("Age").__str__().__len__()) * " ") \
                        + "Name=" + self.scoredb[i].get("Name").__str__() + \
                        ((30 - self.scoredb[i].get("Name").__len__()) * " ") + \
                        "Score=" + self.scoredb[i].get("Score").__str__() + "\n"

        self.textResult.setText(self.str)

    def Delete(self):

        self.str = ""

        for i in range(0, self.scoredb.__len__()):
            if (self.scoredb[i].get("Name") == self.editname.text()):
                self.scoredb.pop(i)
            else :
                self.str += "Age=" + self.scoredb[i].get("Age").__str__() + \
                        ((20 - self.scoredb[i].get("Age").__str__().__len__()) * " ") \
                        + "Name=" + self.scoredb[i].get("Name").__str__() + \
                        ((30 - self.scoredb[i].get("Name").__len__()) * " ") + \
                        "Score=" + self.scoredb[i].get("Score").__str__() + "\n"

        self.textResult.setText(self.str)

    def Find(self):
        self.str = ""

        for i in range(0, self.scoredb.__len__()):
            if (self.scoredb[i].get("Name").__str__() == self.editname.text()):
                self.str += "Age=" + self.scoredb[i].get("Age").__str__() + \
                    ((20 - self.scoredb[i].get("Age").__str__().__len__()) * " ") \
                    + "Name=" + self.scoredb[i].get("Name").__str__() + \
                    ((30 - self.scoredb[i].get("Name").__len__()) * " ") + \
                    "Score=" + self.scoredb[i].get("Score").__str__() + "\n"

        self.textResult.setText(self.str)

    def Increase(self):

        self.str = ""

        for i in range(0, self.scoredb.__len__()):

            if (self.scoredb[i].get("Name").__str__() == self.editname.text()):
                self.scoredb[i].update({"Score" : self.scoredb[i].get("Score") + int(self.editAmount.text())})

            self.str += "Age=" + self.scoredb[i].get("Age").__str__() + \
                        ((20 - self.scoredb[i].get("Age").__str__().__len__()) * " ") \
                        + "Name=" + self.scoredb[i].get("Name").__str__() + \
                        ((30 - self.scoredb[i].get("Name").__len__()) * " ") + \
                        "Score=" + self.scoredb[i].get("Score").__str__() + "\n"

        self.textResult.setText(self.str)

    def Show(self):
        self.str = ""

        if (self.key_Box.currentText() == "Age"):
            self.scoredb.sort(key=itemgetter("Age"))
        elif (self.key_Box.currentText() == "Name"):
            self.scoredb.sort(key=itemgetter("Name"))
        elif (self.key_Box.currentText() == "Score"):
            self.scoredb.sort(key=itemgetter("Score"))


        for i in range(0, self.scoredb.__len__()) :
            self.str += "Age=" + self.scoredb[i].get("Age").__str__() + \
                        ((20 - self.scoredb[i].get("Age").__str__().__len__()) * " ") \
                        + "Name=" + self.scoredb[i].get("Name").__str__() + \
                        ((30 - self.scoredb[i].get("Name").__len__()) * " ") +\
                        "Score=" + self.scoredb[i].get("Score").__str__() + "\n"

        self.textResult.setText(self.str)

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





