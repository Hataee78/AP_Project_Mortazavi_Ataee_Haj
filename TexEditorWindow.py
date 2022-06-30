from designe import Ui_TextEditor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog ,QMessageBox
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog,QPrintPreviewDialog

class EditorWindow(QtWidgets.QMainWindow, Ui_TextEditor):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.actionNew.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionPrint.triggered.connect(self.printfile)
        self.actionPrint_Preview.triggered.connect(self.printPreview)
        

        self.show()

    def fileNew(self):
        self.textEdit.clear()
    
    def openFile(self):
        filename = QFileDialog.getOpenFileName(self,'Open File','/home')
        
        if filename[0]:
            f= open(filename[0],'r')
            
            with f:
                data = f.read()
                self.textEdit.setText(data)    
                
    def fileSave(self):
        filename = QFileDialog.getSaveFileName(self,'Save File')      
        if filename[0]:
            f=open(filename[0],'w') 
            
            with f:
                text = self.textEdit.toPlainText()
                f.write(text)
                
                QMessageBox.about(self,"Save File","File Saved Successful")     
    
    
    def printfile(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer,self)
        
        if dialog.exec_()== QPrintDialog.Accepted:
            self.textEdit.print_(printer)
                       
                       
    def printPreview(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer,self)
        previewDialog.paintRequested.connect(self.printPreview)
        previewDialog.exec_()
        
        
    def printPreview2(self,printer):
        self.textEdit.print_(printer)     
                        