# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TicTacToe.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMaximumSize(314,304)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 4
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.btn4.clicked.connect(lambda: self.btnclicked(4))
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 9
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.btn9.clicked.connect(lambda: self.btnclicked(9))
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 8
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.btn8.clicked.connect(lambda: self.btnclicked(8))
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 3
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.btn3.clicked.connect(lambda: self.btnclicked(3))
        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 5
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.btn5.clicked.connect(lambda: self.btnclicked(5))
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 6
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.btn6.clicked.connect(lambda: self.btnclicked(6))
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 7
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.btn7.clicked.connect(lambda: self.btnclicked(7))
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 1
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(lambda: self.btnclicked(1))
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   btn 2
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(lambda: self.btnclicked(2))
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        #   reset button
        self.reset.setFont(font)
        self.reset.setObjectName("reset")
        self.reset.clicked.connect(lambda: self.resetall())
        self.verticalLayout.addWidget(self.reset)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 317, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.startgame()
        

    def resetall(self):
        self.label.setText(" ")
        
        self.btn4.setEnabled(True)
        self.btn4.setText( " ")
        
        self.btn9.setEnabled(True)
        self.btn9.setText( " ")
        
        self.btn8.setEnabled(True)
        self.btn8.setText( " ")
        
        self.btn3.setEnabled(True)
        self.btn3.setText( " ")
        
        self.btn5.setEnabled(True)
        self.btn5.setText( " ")
        
        self.btn6.setEnabled(True)
        self.btn6.setText( " ")
        
        self.btn7.setEnabled(True)
        self.btn7.setText( " ")
        
        self.btn1.setEnabled(True)
        self.btn1.setText( " ")
        
        self.btn2.setEnabled(True)
        self.btn2.setText( " ")
        
        #it begin from start resetting all things 
        self.startgame()

    #this will check for game completion
    def checkgamestate(self,user):

        #checking rows
        if self.ar[0][0] == self.ar[0][1] and self.ar[0][1] == self.ar[0][2] and self.ar[0][0] == user:
            self.finalstate(self.ar[0][0])
            return "Done"
        if self.ar[1][0] == self.ar[1][1] and self.ar[1][1] == self.ar[1][2] and self.ar[1][0] == user:
            self.finalstate(self.ar[1][0])
            return "Done"
        if self.ar[2][0] == self.ar[2][1] and self.ar[2][1] == self.ar[2][2] and self.ar[2][0] == user:
            self.finalstate(self.ar[2][0])
            return "Done"

        # checking columns
        if self.ar[0][0] == self.ar[1][0] and self.ar[1][0] == self.ar[2][0] and self.ar[0][0] == user:
            self.finalstate(self.ar[0][0])
            return "Done"
        if self.ar[0][1] == self.ar[1][1] and self.ar[1][1] == self.ar[2][1] and self.ar[0][1] == user:
            self.finalstate(self.ar[0][1])
            return "Done"
        if self.ar[0][2] == self.ar[1][2] and self.ar[1][2] == self.ar[2][2] and self.ar[0][2] == user:
            self.finalstate(self.ar[0][2])
            return "Done"

        # checking diagonals
        if self.ar[0][0] == self.ar[1][1] and self.ar[1][1] == self.ar[2][2] and self.ar[0][0] == user:
            self.finalstate(self.ar[0][0])
            return "Done"
        if self.ar[0][2] == self.ar[1][1] and self.ar[1][1] == self.ar[2][0] and self.ar[0][2] == user:
            self.finalstate(self.ar[0][2])
            return "Done"
        return None
    
    #this will start the game
    def startgame(self):
        self.user_id = 0
        self.count = 0
        self.choice = ['X','O']
        self.winner = None
        self.ar = [[' ',' ',' '],
                   [' ',' ',' '],
                   [' ',' ',' ']]

    #this function is called everytime when a button is clicked
    def btnclicked(self,i):
        self.count += 1
        ar = [0,self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9]
        ar[i].setEnabled(False)
        ar[i].setText(self.choice[self.user_id])
        self.edit_state(i,self.user_id)
        self.winner = self.checkgamestate(self.choice[self.user_id])
        self.user_id = (self.user_id + 1) % 2
        if self.winner is None:
            self.label.setText("Ongoing !")
        if self.count>=9:
            self.label.setText("Draw !")
            
    def finalstate(self,ch):
        self.label.setText(ch + " Wins!")
        ar = [self.btn1,self.btn2,self.btn3,self.btn4,self.btn5,self.btn6,self.btn7,self.btn8,self.btn9]
        for p in ar:
            p.setEnabled(False)
        
    def edit_state(self,i,user):
        if i == 1:
            self.ar[0][0] = self.choice[user]
        elif i == 2:
            self.ar[0][1] = self.choice[user]
        elif i == 3:
            self.ar[0][2] = self.choice[user]
        elif i == 4:
            self.ar[1][0] = self.choice[user]
        elif i == 5:
            self.ar[1][1] = self.choice[user]
        elif i == 6:
            self.ar[1][2] = self.choice[user]
        elif i == 7:
            self.ar[2][0] = self.choice[user]
        elif i == 8:
            self.ar[2][1] = self.choice[user]
        elif i == 9:
            self.ar[2][2] = self.choice[user]
        else:
            pass
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TicTacToe"))
        self.btn4.setText(_translate("MainWindow", " "))
        self.btn9.setText(_translate("MainWindow", " "))
        self.btn8.setText(_translate("MainWindow", " "))
        self.btn3.setText(_translate("MainWindow", " "))
        self.btn5.setText(_translate("MainWindow", " "))
        self.btn6.setText(_translate("MainWindow", " "))
        self.btn7.setText(_translate("MainWindow", " "))
        self.btn1.setText(_translate("MainWindow", " "))
        self.btn2.setText(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", " "))
        self.reset.setText(_translate("MainWindow", "RESET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
