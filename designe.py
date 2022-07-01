# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextEditor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(979, 594)
        MainWindow.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.483, y1:0, x2:0.483, y2:1, stop:0 rgba(227, 255, 221, 255), stop:0.761194 rgba(224, 152, 152, 255), stop:0.98 rgba(127, 0, 0, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 961, 491))
        self.textEdit.setStyleSheet("QTextEdit { background-color: rgb(255, 255, 255)}")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 61, 21))
        self.label.setStyleSheet("QLabel { background-color: white}")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(28, 20, 871, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FontSize = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.FontSize.setStyleSheet("QAbstractSpinBox { background-color: rgb(255, 255, 255); }\n"
"")
        self.FontSize.setObjectName("FontSize")
        self.horizontalLayout.addWidget(self.FontSize)
        self.Persian_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Persian_pushButton.setStyleSheet("QPushButton { color: black; background-color:rgb(255, 172, 176)}\n"
"")
        self.Persian_pushButton.setObjectName("Persian_pushButton")
        self.horizontalLayout.addWidget(self.Persian_pushButton)
        self.English_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.English_pushButton.setStyleSheet("QPushButton { color: black; background-color:rgb(255, 172, 176)}")
        self.English_pushButton.setObjectName("English_pushButton")
        self.horizontalLayout.addWidget(self.English_pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet("QLineEdit { background-color: white} ")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        self.menuStyle = QtWidgets.QMenu(self.menubar)
        self.menuStyle.setObjectName("menuStyle")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons/icons8-open-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionNew = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\icons/icons8-new-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon1)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\icons/icons8-save-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\icons/icons8-print-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon3)
        self.actionPrint.setObjectName("actionPrint")
        self.actionPrint_Preview = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\icons/print preview.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint_Preview.setIcon(icon4)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")
        self.actionExport = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\icons/icons8-pdf-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExport.setIcon(icon5)
        self.actionExport.setObjectName("actionExport")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\icons/exit.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\icons/icons8-copy-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon7)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCopy_Paste = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(".\\icons/icons8-paste-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy_Paste.setIcon(icon8)
        self.actionCopy_Paste.setObjectName("actionCopy_Paste")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(".\\icons/icons8-undo-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon9)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(".\\icons/icons8-redo-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon10)
        self.actionRedo.setObjectName("actionRedo")
        self.actionFont = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(".\\icons/icons8-choose-font-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFont.setIcon(icon11)
        self.actionFont.setObjectName("actionFont")
        self.actionColor = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(".\\icons/icons8-color-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionColor.setIcon(icon12)
        self.actionColor.setObjectName("actionColor")
        self.actionBold = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(".\\icons/icons8-bold-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon13)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(".\\icons/icons8-italic-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon14)
        self.actionItalic.setObjectName("actionItalic")
        self.actionLeft = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(".\\icons/alignLeft.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLeft.setIcon(icon15)
        self.actionLeft.setObjectName("actionLeft")
        self.actionCenter = QtWidgets.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(".\\icons/icons8-align-center-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCenter.setIcon(icon16)
        self.actionCenter.setObjectName("actionCenter")
        self.actionRight = QtWidgets.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(".\\icons/icons8-align-right-16.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRight.setIcon(icon17)
        self.actionRight.setObjectName("actionRight")
        self.actionJusstify = QtWidgets.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(".\\icons/icons8-align-justify-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJusstify.setIcon(icon18)
        self.actionJusstify.setObjectName("actionJusstify")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionUnderline = QtWidgets.QAction(MainWindow)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(".\\icons/icons8-underline-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon19)
        self.actionUnderline.setObjectName("actionUnderline")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionPrint_Preview)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCopy_Paste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuFormat.addAction(self.actionFont)
        self.menuFormat.addAction(self.actionColor)
        self.menuStyle.addAction(self.actionBold)
        self.menuStyle.addAction(self.actionItalic)
        self.menuStyle.addAction(self.actionUnderline)
        self.menuStyle.addSeparator()
        self.menuStyle.addAction(self.actionLeft)
        self.menuStyle.addAction(self.actionCenter)
        self.menuStyle.addAction(self.actionRight)
        self.menuStyle.addAction(self.actionJusstify)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuStyle.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", " Font Size"))
        self.Persian_pushButton.setText(_translate("MainWindow", "Translater to Persian"))
        self.English_pushButton.setText(_translate("MainWindow", " Translater to English"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.menuStyle.setTitle(_translate("MainWindow", "Style"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint_Preview.setText(_translate("MainWindow", "Print Preview"))
        self.actionExport.setText(_translate("MainWindow", "Export PDF"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy_Paste.setText(_translate("MainWindow", "Paste"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionFont.setText(_translate("MainWindow", "Font"))
        self.actionColor.setText(_translate("MainWindow", "Color"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionItalic.setText(_translate("MainWindow", "Italic"))
        self.actionLeft.setText(_translate("MainWindow", "Left"))
        self.actionCenter.setText(_translate("MainWindow", "Center"))
        self.actionRight.setText(_translate("MainWindow", "Right"))
        self.actionJusstify.setText(_translate("MainWindow", "Justify"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionUnderline.setText(_translate("MainWindow", "Underline"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_TextEditor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
