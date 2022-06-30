from designe import Ui_TextEditor
from PyQt5 import QtWidgets

class EditorWindow(QtWidgets.QMainWindow, Ui_TextEditor):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.actionNew.triggered.connect(self.fileNew)

        self.show()

    def fileNew(self):
        self.textEdit.clear()