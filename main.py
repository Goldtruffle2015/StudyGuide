"""
Title: Study Guide
Author: John Yu
Date: 2019-07-05
"""

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0, 0, 1900, 980)
    win.setWindowTitle("Study Guide")

    win.show()
    sys.exit(app.exec_())


# --- Code Starts Here --- #
window()

