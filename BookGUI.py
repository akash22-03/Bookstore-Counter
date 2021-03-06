from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le1 = QtWidgets.QLineEdit(self.centralwidget)
        self.le1.setStyleSheet("border : 1px solid black;\n"
"border-radius: 4px;")
        self.le1.setObjectName("le1")
        self.gridLayout.addWidget(self.le1, 0, 1, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.clicked.connect(self.setPrice)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.le2 = QtWidgets.QLineEdit(self.centralwidget)
        self.le2.setStyleSheet("color: blue;\n"
"border:none;")
        self.le2.setObjectName("le2")
        self.gridLayout.addWidget(self.le2, 1, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.le3 = QtWidgets.QLineEdit(self.centralwidget)
        self.le3.setObjectName("le3")
        self.gridLayout.addWidget(self.le3, 3, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 3, 2, 1, 1)
        self.btn2.clicked.connect(self.setTotal)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.le4 = QtWidgets.QLineEdit(self.centralwidget)
        self.le4.setStyleSheet("border:none;\n"
"color:blue;")
        self.le4.setObjectName("le4")
        self.gridLayout.addWidget(self.le4, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Book Title :"))
        self.le1.setPlaceholderText(_translate("MainWindow", "Enter Book Name"))
        self.btn1.setText(_translate("MainWindow", "Find Price"))
        self.label_3.setText(_translate("MainWindow", "Price :"))
        self.le2.setPlaceholderText(_translate("MainWindow", "Rs.0.00"))
        self.label_2.setText(_translate("MainWindow", "Quantity :"))
        self.le3.setPlaceholderText(_translate("MainWindow", "Enter Quantity"))
        self.btn2.setText(_translate("MainWindow", "Find Total"))
        self.label_4.setText(_translate("MainWindow", "Total :"))
        self.le4.setPlaceholderText(_translate("MainWindow", "Rs.0.00"))
        
    def setPrice(self):
        Bookstore = sqlite3.connect('bookstore.db')
        cur = Bookstore.cursor()
        name = self.le1.text()
        sql = 'SELECT * FROM booklib WHERE Name = "'+name+'";'
        x = cur.execute(sql)
        if x!=None:
            record = cur.fetchone()
            price = (record[3])
            self.le2.setText("Rs. "+str(price))

    def setTotal(self):
        Bookstore = sqlite3.connect('bookstore.db')
        cur = Bookstore.cursor()
        quan = self.le3.text()
        quant = float(quan)
        name = self.le1.text()
        sql = 'SELECT * FROM booklib WHERE Name = "'+name+'";'
        cur.execute(sql)
        record = cur.fetchone()
        price = (record[3])
        total = quant * price
        self.le4.setText("Rs. "+str(total))
        
        
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
