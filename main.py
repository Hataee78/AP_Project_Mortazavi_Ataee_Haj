########################################################################################################################################################################
#################################################### Main Window of Application ########################################################################################
#######################################################****Text Editor App****##########################################################################################
#######################################################****************#################################################################################################
################################################# This App Producted By MAH Group ######################################################################################
###################################### The Authors Are: A. Hajee Sadeghian, H. Ataee, M. Mortazavi #####################################################################
########################################################################################################################################################################
########################################################################################################################################################################
##### This app is for edit of text with beautifull UI that is user friendly.                                                     #######################################
##### Some of feature in Menu Bar:                                                                                               #######################################
##### 1. File: Open File, Make New File, Save File in Directory, Print File, Print Preview, Export to PDF, Exit from App         #######################################
##### 2. Edit: Copy Text, Paste Text, Cut Text, Undo, Redo                                                                       #######################################
##### 3. Format: Set Font for Text, Choose Color of Selected Text                                                                #######################################
##### 4. Style : Bold , Italic and Underline for selected text; set Alignment of text: Left, Center, Right and Justify           #######################################
##### 5. Help: Introduction About Authors                                                                                        #######################################
########################################################################################################################################################################
########################################################################################################################################################################
##### Installation:                                                                                                               ######################################
##### Download AP-TextEditor.rar from https://github.com/Hataee78/AP_Project_Mortazavi_Ataee_Haj                                  ######################################
##### Extraxt .rar file and run .exe                                                                                              ######################################
##### Have Goog Exprience!                                                                                                        ######################################
########################################################################################################################################################################
########################################################################################################################################################################
##### Suppurted operation systems:                                                                                                 #####################################
##### 1. Windows                                                                                                                   #####################################
##### 2. Ubuntu                                                                                                                    #####################################
########################################################################################################################################################################
########################################################################################################################################################################
#### About code:
#### We have two class: MainWindow(for application) in TextEditorWindow module and SplashScreen(for splash before run app) in main
#### For each class, we have one designed file that has converted to python format by this command --> pyuic5 -x .\"filename".ui -o "filename".py
########################################################################################################################################################################


import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from TextEditorWindow import MainWindow


## splash ui
from ui_splash_screen import Ui_SplashScreen


## GLOBALS
counter = 0



# splash screen
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        #####################    ui   ###########################

        ## remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## drap shodaw effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        #### show main window ####
        self.show()
        ## ==> END ##

    ####################   progress   #####################
    def progress(self):

        global counter

        # set value for progress bar
        self.ui.progressBar.setValue(counter)

        # close splash screen and open app
        if counter > 100:

            self.timer.stop() # stop timer

            ### show main window ###
            self.main = MainWindow()
            self.main.show()

            self.close() # close splash screen

        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())
