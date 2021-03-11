from PyQt5.QtWidgets import *
import  sys
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar=QToolBar()
        self.addToolBar(navbar)
        backbtn=QAction('<-',self)
        backbtn.triggered.connect(self.browser.back)
        navbar.addAction(backbtn)
        forwardbtn=QAction('->',self)
        forwardbtn.triggered.connect(self.browser.forward)
        navbar.addAction(forwardbtn)
        reloadbtn=QAction('(-)',self)
        reloadbtn.triggered.connect(self.browser.reload)
        navbar.addAction(reloadbtn)
        homebtn=QAction('(==)',self)
        homebtn.triggered.connect(self.navigate_home)
        navbar.addAction(homebtn)
        self.url_bar=QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.updateurl)
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))
    def navigate_url(self):
        url=self.url_bar.text()
        self.browser.setUrl(QUrl("https://"+url+".com"))
    def updateurl(self,q):
        self.url_bar.setText(q.toString())
app=QApplication(sys.argv)
QApplication.setApplicationName("Browser")
window=MainWindow()
app.exec()