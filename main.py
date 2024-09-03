import sys
import getpass
import os

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def button(self):
        qbtn = QPushButton('bbDPI', self)
        qbtn.clicked.connect(self.buttonClicked)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(85, 50)

    def buttonClicked(self):
        user = getpass.getuser()
        path = f"goodbyedpi-0.2.3rc1\\1_russia_blacklist_dnsredir.cmd"
        os.system(path)

    def initUI(self):

        self.button()
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('bbDPI')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())