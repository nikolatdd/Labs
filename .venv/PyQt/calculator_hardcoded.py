import sys
import sys
from PyQt6 import QtWidgets as qtw
from PyQt6 import QtCore as qtc
from PyQt6 import QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Handcoded calculator')
        self.createGridLayout()
        self.addMainLayout()
        self.setFixedSize(300,320)
        self.show()


    def addMainLayout(self):
        le0output = qtw.QLineEdit()
        le0output.setMinimumWidth(260)
        le0output.setMinimumHeight(50)
        le0output.setDisabled(True)

        mainLayout = qtw.QVBoxLayout()
        

        mainLayout.addWidget(le0output)
        mainLayout.addLayout(self.gridLayout)
        self.setLayout(mainLayout)

    def createGridLayout(self):
        btnBackspace = qtw.QPushButton('Backspace')
        btnClear = qtw.QPushButton('Clear')
        btnClearAll = qtw.QPushButton('ClearAll')

        self.gridLayout=qtw.QGridLayout()

        self.gridLayout.addWidget(btnBackspace,0,0,1,2)
        self.gridLayout.addWidget(btnClear,0,2,1,2)
        self.gridLayout.addWidget(btnClearAll,0,4,1,2)

        row2BtnNames = ['MC', '7', '8', '9', '%', 'Sqrt']
        for i,name in enumerate(row2BtnNames):
            btn = qtw.QPushButton(name)
            self.gridLayout.addWidget(btn,1,i)
        row3BtnNames = ['MR', '4','5','6','x','^']
        for i,name in enumerate(row3BtnNames):
            btn = qtw.QPushButton(name)
            self.gridLayout.addWidget(btn,2,i)
        row4BtnNames = ['MS', '1','2','3','-','1/x']
        for i,name in enumerate(row4BtnNames):
            btn = qtw.QPushButton(name)
            self.gridLayout.addWidget(btn,3,i)
        row5BtnNames = ['M+', '0','.','+-','+','=']
        for i,name in enumerate(row5BtnNames):
            btn = qtw.QPushButton(name)
            self.gridLayout.addWidget(btn,4,i)

if __name__ == "__main__": 
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec())


