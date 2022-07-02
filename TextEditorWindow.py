import sys
import platform
from googletrans import Translator
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from design import Ui_TextEditor

class MainWindow(QtWidgets.QMainWindow, Ui_TextEditor):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.textEdit.textChanged.connect(self.change)

        self.actionNew.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionPrint.triggered.connect(self.printfile)
        self.actionPrint_Preview.triggered.connect(self.printPreview)
        self.actionExport.triggered.connect(self.exportPdf)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCopy_Paste.triggered.connect(self.paste)
        # self.actionCut.triggered.connect(self.cut)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionFont.triggered.connect(self.fontDialog)
        self.actionColor.triggered.connect(self.colorDialog)

        self.actionBold.triggered.connect(lambda: self.formatText("bold"))
        self.actionItalic.triggered.connect(lambda: self.formatText("italic"))
        self.actionUnderline.triggered.connect(lambda: self.formatText("underline"))

        self.actionLeft.triggered.connect(lambda: self.align("Left"))
        self.actionCenter.triggered.connect(lambda: self.align("Center"))
        self.actionRight.triggered.connect(lambda: self.align("Right"))
        self.actionJusstify.triggered.connect(lambda: self.align("Justify"))

        self.FontSize.setValue(24)
        self.textEdit.setFontPointSize(24)
        self.FontSize.valueChanged.connect(self.setFontSize)

        self.Persian_pushButton.clicked.connect(lambda : self.trans("fa")) # we defined lambda function to recognize which signal was called slot by send function to another function
        self.English_pushButton.clicked.connect(lambda : self.trans("en"))

        self.thread = None



        ###### set window Title and Icon ####
        self.setWindowTitle("Text Editor App")
        self.setWindowIcon(QIcon("./Icons/app-icon2"))
        self.show()
        

    def change(self):
        return True

    def fileNew(self):
        self.textEdit.clear()

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', "/home") # get file that user can open
        if filename[0]:
            with open(filename[0], 'r') as file:
                data = file.read()
                self.textEdit.setText(data)

    def fileSave(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        if filename[0]:
            with open(filename[0], 'w', encoding="utf-8") as file: # you should encoding by utf-8, otherwise you take Error for persian language
                text = self.textEdit.toPlainText()
                file.write(text)

            QMessageBox.about(self, "Save File", "File Saved Successful") # show massage that save was successfull

    def printfile(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.accepted:
            self.textEdit.print_(printer)

    def printPreview(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.printPreview2)
        previewDialog.exec_()

    def printPreview2(self, printer):
        self.textEdit.print_(printer)

    def exportPdf(self):
        fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf) ;; All Files")
        print(fn)
        if fn != "":
            if QFileInfo(fn).suffix()  == "":fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)

    def exitApp(self):
        
        ret = QMessageBox.question(self, 'your file has not been saved', "do you want to save", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        if ret == QMessageBox.Yes: 
            filename = QFileDialog.getSaveFileName(self, 'Save File')
            if filename[0]:
                f = open(filename[0], 'w',encoding="utf-8")

                with f:
                    text = self.textEdit.toPlainText()
                    f.write(text)

                    QMessageBox.about(self, "Save File", "File Saved Succuessful")
        if ret == QMessageBox.No: self.close()

    def copy(self):
        cursor = self.textEdit.textCursor()
        textselected = cursor.selectedText() # it is selected text
        self.copiedText = textselected # save in variable of class

    def paste(self):
        self.textEdit.append(self.copiedText) # paste copied text

    # def cut(self):
    #     cursor = self.textEdit.textCursor()
    #     textSelected = cursor.selectedText()
    #     self.copiedText = textSelected
    #     self.textEdit.cut()

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

    def colorDialog(self): 
            color = QColorDialog.getColor() 
            self.textEdit.setTextColor(color)

    ####### format Text: Bold, Italic and Underline #####
    def formatText(self, type):
        if type == 'bold':
            self.textEdit.setFontWeight(QFont.Bold)
        elif type == 'italic':
            self.textEdit.setFontItalic(True)
        elif type == 'underline':
            self.textEdit.setFontUnderline(True)


    ######## set align of text: Left, Center , Right and Justify #######
    def align(self, type):
        if type == 'Left':
            self.textEdit.setAlignment(Qt.AlignLeft)
        elif type == 'Center':
            self.textEdit.setAlignment(Qt.AlignCenter)
        elif type == 'Right':
            self.textEdit.setAlignment(Qt.AlignRight)
        elif type == 'Justify':
            self.textEdit.setAlignment(Qt.AlignJustify)



    def setFontSize(self):
        value = self.FontSize.value()
        self.textEdit.setFontPointSize(value)

    def trans(self, name):
        #### create object of Translator #####
        translator = Translator()
        #### selected text ###
        cursor = self.textEdit.textCursor()
        text = cursor.selectedText()

        if name == 'fa':
            #### translating ######
            trans = translator.translate(text, src='auto', dest='fa') # its type is googletrans.models.Translated
        elif name == 'en':
            #### translating ######
            trans = translator.translate(text, src='auto', dest='en') # its type is googletrans.models.Translated
        
        translated = trans.text # convert googletrans.models.Translated to string
        self.lineEdit.setText(translated) # set Text to lineEdit


