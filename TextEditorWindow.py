import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from design import Ui_TextEditor
from googletrans import Translator



class MainWindow(QtWidgets.QMainWindow, Ui_TextEditor):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.font = QFont()

        self.actionNew.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.openFile)

        self.actionSave.triggered.connect(self.fileSave)
        self.actionExport.triggered.connect(self.exportPdf)

        self.actionPrint.triggered.connect(self.printfile)
        self.actionPrint_Preview.triggered.connect(self.printPreview)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCopy_Paste.triggered.connect(self.paste)
        self.actionCut.triggered.connect(self.cut)
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


        self.actionAbout.triggered.connect(self.aboutus)



        ###### set window Title and Icon ####
        self.setWindowTitle("Text Editor App")
        self.setWindowIcon(QIcon("./Icons/app-icon2"))
        self.show()
        

    def fileNew(self):
        try:
            self.textEdit.clear()
        except:
            message = QErrorMessage(self)
            message.showMessage("New File Not Possible")

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, caption="Open File", filter="*.txt") # get file that user can open
        if filename[0]:
            with open(filename[0], 'r', encoding="utf-8") as file:
                data = file.read()
                self.textEdit.setText(data)

    def fileSave(self):
        filename = QFileDialog.getSaveFileName(self, caption="Save File", filter="*.txt") # by default, will save file as text
        if filename[0]:
            with open(filename[0], 'w', encoding="utf-8") as file: # you should encoding by utf-8, otherwise you take Error for persian language
                text = self.textEdit.toPlainText()
                file.write(text)
            QMessageBox.about(self, "Save File", "File Saved Successful") # show massage that save was successfull

    def exportPdf(self):
        filename = QFileDialog.getSaveFileName(self, caption="Export to PDF", filter="*.pdf") # by default, will save file as pdf
        if filename[0]:
            if QFileInfo(filename[0]).suffix() == "":
                filename[0] += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(filename[0])
            self.textEdit.document().print_(printer)



    def printfile(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if (dialog.exec_() == QPrintDialog.Accepted): # notice: you should write Accepted with captal A
            self.textEdit.print_(printer)

    def printPreview(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(lambda printer: self.textEdit.print_(printer) ) # if recieved paintRequested signal, we call slot to print text
        previewDialog.exec_()
            

    def exitApp(self):
        ret = QMessageBox.question(self, 'your file has not been saved', "do you want to save", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel) # get answer of question for exit
        if ret == QMessageBox.Yes:
            self.fileSave() # save file
            self.close() # close file

        elif ret == QMessageBox.No:
            self.close() # close file

    def copy(self):
        cursor = self.textEdit.textCursor()
        textselected = cursor.selectedText() # it is selected text
        self.copiedText = textselected # save in variable of class

    def paste(self):
        self.textEdit.append(self.copiedText) # paste copied text

    def cut(self):
        self.copy()
        self.textEdit.cut()

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

        if text != "":
            try:
                if name == 'fa':
                    #### translating ######
                    trans = translator.translate(text, src='auto', dest='fa') # its type is googletrans.models.Translated
                elif name == 'en':
                    #### translating ######
                    trans = translator.translate(text, src='auto', dest='en') # its type is googletrans.models.Translated
            
                translated = trans.text # convert googletrans.models.Translated to string
                self.lineEdit.setText(translated) # set Text to lineEdit
            except:
                message = QErrorMessage(self)
                message.showMessage("Accured a Mistake in Translation")

        else:
            message = QErrorMessage(self)
            message.showMessage("Select Text")

    def aboutus(self):
        QMessageBox.about(self, "about us", "created by: \n Seyed Mousa Mortazavi \n Hossein Ataee \n Ali Haj Sadeghian")


    
                


