import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class coffeeInfo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('coffee')
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.fillTable()

    def fillTable(self):
        result = self.cur.execute("""SELECT name, degree, type,
                                            description, price, volume from coffee
                                            """).fetchall()
        self.table.setRowCount(len(result))
        if result:
            self.table.setColumnCount(len(result[0]))
            self.table.setHorizontalHeaderLabels(
                ['название сорта', 'степень обжарки', 'молотый/в зернах',
                 'описание вкуса', 'цена', 'объем упоковки'])
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.table.setItem(i, j, QTableWidgetItem(str(val)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = coffeeInfo()
    widget.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
