#final Project Mousa Mortazavi-Ali Haj Sadeghian- Hossein Ataee
from designe import Ui_TextEditor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox , QFontDialog ,QColorDialog
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo , Qt
from PyQt5.QtGui import QFont

class EditorWindow(QtWidgets.QMainWindow, Ui_TextEditor):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.actionNew.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionPrint.triggered.connect(self.printfile)
        self.actionPrint_Preview.triggered.connect(self.printPreview)
        self.actionExport.triggered.connect(self.exportPdf)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCopy_Paste.triggered.connect(self.paste)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionFont.triggered.connect(self.fontDialog)
        self.actionColor.triggered.connect(self.colorDialog)
        self.actionBold.triggered.connect(self.textBold)
        self.actionItalic.triggered.connect(self.italic)
        self.actionUnderline.triggered.connect(self.underline)
        self.actionJusstify.triggered.connect(self.justify)
        self.actionRight.triggered.connect(self.allignRight)
        self.actionLeft.triggered.connect(self.allignLeft)
        self.actionCenter.triggered.connect(self.allignCenter)
        
        self.FontSize.setValue(24)
        self.textEdit.setFontPointSize(24)
        self.FontSize.valueChanged.connect(self.setFontSize)
        
        
        

      


        self.show()

    def fileNew(self):
        self.textEdit.clear()

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', "/home")

        if filename[0]:
            f = open(filename[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def fileSave(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        if filename[0]:
            f = open(filename[0], 'w')

            with f:
                text = self.textEdit.toPlainText()
                f.write(text)

                QMessageBox.about(self, "Save File", "File Saved Succuessful")

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
        fn,_=QFileDialog.getSaveFileName(self,"Export PDF",None,"PDF files(.pdf);;All Files")
        if fn !="":
            if QFileInfo(fn).suffix() == "":fn +='.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)
    
    
    
    def exitApp(self):
        self.close()
    
    
    
    
    def copy(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected
       
       
    def paste(self):
        self.textEdit.append(self.copiedText)         
          
          
          
    # def cut(self):
    #     cursor = self.textEdit.textCursor()
    #     textSelected = cursor.selectedText()
    #     self.copiedText = textSelected
    #     self.textEdit.cut()
    
    
    
    def fontDialog(self):
        font , ok = QFontDialog.getFont()
        
        if ok:
            self.textEdit.setFont(font)
               
    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)    
        
        
    def textBold(self):
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)
                        
     
     
    def italic(self):
        font = QFont()
        font.setItalic(True)
        self.textEdit.setFont(font)      
        
    def underline(self):
        font = QFont()
        font.setUnderline(True)
        self.textEdit.setFont(font)
        
    def allignLeft(self):
        self.textEdit.setAlignment(Qt.AlignLeft)
    
    
    def allignCenter(self):
        self.textEdit.setAlignment(Qt.AlignCenter)
                                  
                                  
    def allignRight(self):
        self.textEdit.setAlignment(Qt.AlignRight)
        
        
    def justify(self):
        self.textEdit.setAlignment(Qt.AlignJustify)  
        
    
    
    
    def setFontSize(self):
        value = self.FontSize.value()
        self.textEdit.setFontPointSize(value)                                    