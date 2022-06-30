import os
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QMainWindow
from TexEditorWindow import EditorWindow

# Form = uic.loadUiType(os.path.join(os.getcwd(), "designe.ui"))[0]

# class MainWindow(QMainWindow, Form):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setupUi(self)
#         self.textEdit.textChanged.connect(self.type)
    
#     def type(self):
#         """PyQt5 SLOT"""
#         print("Your are now typing")
#         # self.textEdit.setText(self, text)
#         ##### it is my branch #######






# app = QApplication(sys.argv)

# w = MainWindow()
# w.show()
# sys.exit(app.exec_())

app = QApplication(sys.argv)
app.setStyle("Fusion")
textEditor = EditorWindow()
sys.exit(app.exec_())

