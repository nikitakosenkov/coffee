import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, coffee):
        coffee.setObjectName("coffee")
        coffee.resize(884, 620)
        self.tableWidget = QtWidgets.QTableWidget(coffee)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 871, 591))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        self.retranslateUi(coffee)
        QtCore.QMetaObject.connectSlotsByName(coffee)

    def retranslateUi(self, coffee):
        _translate = QtCore.QCoreApplication.translate
        coffee.setWindowTitle(_translate("coffee", "Form"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        q = cur.execute("SELECT * FROM sorts").fetchall()
        print(q)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(['id', 'title', 'fry', 'molotyi zerno',
                                                    'description', 'price', 'amount'])
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(list(q)):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(list(row)):
                elem = str(elem)
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
