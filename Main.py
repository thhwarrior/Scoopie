#################################Dependancies############################################
import requests
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow,QApplication,QStackedWidget,QLabel,QGridLayout
#################################Images#################################################
import Welcome
import redtriangles

#################################Transitions############################################
def GetBack():
    Welcome=WelcomeScreen()
    widget.addWidget(Welcome)
    widget.setCurrentIndex(widget.currentIndex()+1)

def GoToMedia():
    link = "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=1dd2848490a84d188a177541edabfabd"
    f = requests.get(link).json()
    Articles = f["articles"]
    title = []
    description = []
    url = []
    for article in Articles:
        title.append(article["title"])
        url.append(article["url"])
        description.append(article["description"])

    tech=MediaScreen()
    tech.gridlayout = QGridLayout(tech.widget)
    for i in range(len(f["articles"])):
        create(tech,title,url,i)
    widget.addWidget(tech)
    widget.setCurrentIndex(widget.currentIndex()+1)


def GoToScience():
    link = "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=1dd2848490a84d188a177541edabfabd"
    f = requests.get(link).json()
    Articles = f["articles"]
    title = []
    description = []
    url = []
    for article in Articles:
        title.append(article["title"])
        url.append(article["url"])
        description.append(article["description"])

    tech=ScienceScreen()
    tech.gridlayout = QGridLayout(tech.widget)
    for i in range(len(f["articles"])):
        create(tech,title,url,i)
    widget.addWidget(tech)
    widget.setCurrentIndex(widget.currentIndex()+1)

def GoToTech():
    link = "https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=1dd2848490a84d188a177541edabfabd"
    f = requests.get(link).json()
    Articles = f["articles"]
    title = []
    description = []
    url = []
    for article in Articles:
        title.append(article["title"])
        url.append(article["url"])
        description.append(article["description"])

    tech=TechScreen()
    tech.gridlayout = QGridLayout(tech.widget)
    for i in range(len(f["articles"])):
        create(tech,title,url,i)
    widget.addWidget(tech)
    widget.setCurrentIndex(widget.currentIndex()+1)

#################################Classes (Screens)######################################
class WelcomeScreen(QMainWindow):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("Home.ui",self)
        self.tech.clicked.connect(GoToTech)
        self.science.clicked.connect(GoToScience)
        self.media.clicked.connect(GoToMedia)

class TechScreen(QMainWindow):
    def __init__(self):
        super(TechScreen, self).__init__()
        loadUi("Tech.ui",self)
        self.back.clicked.connect(GetBack)

class ScienceScreen(QMainWindow):
    def __init__(self):
        super(ScienceScreen, self).__init__()
        loadUi("Science.ui",self)
        self.back.clicked.connect(GetBack)

class MediaScreen(QMainWindow):
    def __init__(self):
        super(MediaScreen, self).__init__()
        loadUi("Media.ui",self)
        self.back.clicked.connect(GetBack)



#################################Creating News Labels################################################
def create(tech,title,url,i):
    tech.label=QLabel(tech.widget)
    tech.label.setOpenExternalLinks(True)
    text='<a href={0}>{1}</a>'.format(url[i],str(i+1)+":   "+title[i])
    tech.label.setText(text)
    coord = i * 30
    tech.gridlayout.addWidget(tech.label,coord,0,1,1)
    tech.label.setStyleSheet("border:2px solid black;""font: 14pt \"Century\";\n""color: rgb(0, 0, 255);\n""")
    name="label"+str(i)
    tech.label.setObjectName(name)


####Main##########
app=QApplication(sys.argv)
welcome=WelcomeScreen()
widget= QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(801)
widget.setFixedWidth(1025)
widget.show()
sys.exit(app.exec())

