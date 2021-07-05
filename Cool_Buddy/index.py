import sys
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import cv2
import os
import webbrowser as wb
import pyautogui as py
import time
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie  # for gif
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvis__ui import Ui_MainWindow


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
command = 'b'


# function that take text input by user and  output the speech of the text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# function to search anything on wikipedia
def wiki(p):
    person = p.replace('who  is', '')
    info = wikipedia.summary(person)
    # 1 after represents the person is the limit of words in info
    print(info)
    speak(info)


# function to type something in notepad file by speaking
def notepad():
    print("bgr")
    py.press('win', interval=0.2)
    # press to automatically press the key
    py.typewrite('Notepad', interval=0.2)
    # typewrite
    py.press('enter', interval=0.2)
    speak("Please tell your content sir")

    time.sleep(3)
    while True:
        x = take_command()
        if "QUIT" in x:
            break
        py.typewrite(x, interval=0.2)
        py.typewrite('\n', interval=0.2)

    speak("Would you like to save it")
    time.sleep(3)
    x = take_command()
    if "YES" in x:
        print('vt')
        py.press('ctrl + s', interval=0.2)


#function to open camera
def camera():
    cap = cv2.VideoCapture(0)
    while True:
        res, frame = cap.read()
        cv2.imshow('cam_star', frame)
        if cv2.waitKey(10) == ord('q'):
            break


# function to open Google crome
def chrome():

    speak("Please say what do you want to search")
    x = take_command()
    time.sleep(3)
    path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    wb.get(path).open_new_tab(x)



#Main thread class to execute run alexa function
class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.run_alexa()


# function to take command through microphone and convert to text
    def take_command(self):
        try:
            with sr.Microphone() as source:
                print('listening...')

                listener.adjust_for_ambient_noise(source)
                voice = listener.listen(source)
                voice.pause_threshold = 3000
                self.command = listener.recognize_google(voice)
                self.command = self.command.upper()
                if 'alexa' in self.command:
                    self.command = self.command.replace('alexa', '')
                    print(self.command)
        except:
            pass
        return self.command



# Main function that does work after recognizing the command given by user
    def run_alexa(self):
        speak('Hello i am jarvis how can i help you')
        while True:
            self.p = self.take_command()
            print(command)

            if 'PLAY' in self.p:
                song = self.p.replace('play', '')
                speak('playing ' + song)
                print(song)
                pywhatkit.playonyt(song)


            elif 'TIME' in self.p:
                time = datetime.datetime.now().strftime('%I:%M %p')
                speak('Current time is ' + time)

            elif 'WHO IS' in self.p:
                wiki(self.p)



            elif ('SELFIE' in self.p) or ('CAMERA' in self.p):
                camera()


            elif ("GOOGLE" in self.p) or ("SEARCH" in self.p) or ("CHROME" in self.p) or ("BROWSER" in self.p):
                speak("Opening")
                speak("GOOGLE CHROME")
                print(".")
                print(".")
                chrome()



            elif ("IE" in self.p) or ("MSEDGE" in self.p) or ("EDGE" in self.p):
                speak("Opening")
                speak("MICROSOFT EDGE")
                print(".")
                print(".")
                os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")

            elif ("NOTEPAD" in self.p) or ("NOTES" in self.p) or ("NOTEPAD" in self.p):
                speak("Opening")
                speak("NOTEPAD")
                print(".")
                print(".")
                i = 0
                notepad()


            elif ("VLCPLAYER" in self.p) or ("PLAYER" in self.p) or ("VIDEO PLAYER" in self.p):
                speak("Opening")
                speak("VLC PLAYER")
                print(".")
                print(".")
                os.startfile("C:\Program Files (x86)\VideoLAN\VLC\vlc.exe")

            elif ("ILLUSTRATOR" in self.p) or ("AI" in self.p):
                speak("Opening")
                speak("ADOBE ILLUSTRATOR")
                print(".")
                print(".")
                os.system("illustrator")



            elif ("WORD" in self.p) or ("MSWORD" in self.p):
                speak("Opening")
                speak("MICROSOFT WORD")
                print(".")
                print(".")
                os.system("C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")


            elif "QUIT" in self.p:
                speak("Thank you for using me sir!")
                break


            else:
                speak("please Type Again")
                print(".")
                print(".")
                continue


startExecution = MainThread()



# class to show gui when program is executed and run the alexa on click of start button
# And end the task on clicking end button
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # To display the ui by itself
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie('Iron Man Jarvis Live Wallpaper This jarvis boot animation (1).gif')
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie('Jarvis_Loading_Screen.gif')
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()

        startExecution.start()



# function to show the time and date
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



# creating objects of class and calling the functions in them
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
