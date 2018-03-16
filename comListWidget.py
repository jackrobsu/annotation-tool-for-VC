#-*- coding:utf-8 -*-
from utilities import *

class ComListWidget(QMainWindow):
    AddSignal = pyqtSignal(QWidget)
    typedict = {
        WidgetType.VERB:"Verb Forms",
        WidgetType.CONJUNCTION:"Conjunction Forms",
        WidgetType.PREPOSITION:"介词语义形式",
        WidgetType.NOUN:"名词所有格形式",
        WidgetType.PRONOUN:"代词语义形式",
        
    }
    def __init__(self,pWidget,connectedTab,widgetType):
        super(ComListWidget,self).__init__()
        self.splitter = QSplitter(Qt.Vertical)
        self.title = QLabel(self.typedict[widgetType])
        self.listWindow = CommonListWidget(pWidget,connectedTab)
        self.addButton = SignalWithHandleButton(self.AddSignal,self.listWindow)
        self.addButton.setText("Select")
        self.addButton.clicked.connect(self.addButton.mousePressEvent)

        self.AddSignal.connect(TextAddThroughWidget)
        self.splitter.addWidget(self.title)
        self.splitter.addWidget(self.listWindow)
        self.splitter.addWidget(self.addButton)
        self.setCentralWidget(self.splitter)

    def resetWidget(self):
        self.listWindow.clear()
        
class ConstantListWidget(QMainWindow):
    AddSignal = pyqtSignal(QWidget)
    def __init__(self,pWidget):
        super(ConstantListWidget,self).__init__()
        self.splitter = QSplitter(Qt.Vertical)
        self.title = QLabel("Reserved Words")
        self.listWindow = ConstantWidget(pWidget)
        # self.addButton = SignalWithHandleButton(self.AddSignal,self.listWindow)
        # self.addButton.setText("确定")
        # self.addButton.clicked.connect(self.addButton.mousePressEvent)

        # self.AddSignal.connect(TextAddThroughWidget)
        self.splitter.addWidget(self.title)
        self.splitter.addWidget(self.listWindow)
        # self.splitter.addWidget(self.addButton)
        self.setCentralWidget(self.splitter)

    def resetWidget(self):
        self.listWindow.clear()