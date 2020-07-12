import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI_label()
    def initUI_label(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("this is a text label")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("GUI program")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip("this is a label about picture")
        label3.setPixmap(QPixmap("./images/python.Png"))

        label4.setText("hha")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip("this is a HTTP")

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkhovered)
        label4.linkActivated.connect(self.linkclicked)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel demo")
    def linkhovered(self):
        print("当鼠标划过label2 标签")
    def linkclicked(self):
        print("when click label4 label")

class MyCalendar(QWidget):
    def __init__(self):
        super(MyCalendar,self).__init__()
        self.initUI()
    def initUI(self):
        self.cal = QCalendarWidget(self)
        self.cal.setMinimumDate(QDate(2000,1,1))
        self.cal.setMaximumDate(QDate(2100,1,1))
        self.cal.setGridVisible(True)
        self.cal.move(20,20)
        self.cal.clicked.connect(self.showdate)

        self.label = QLabel(self)
        date = self.cal.selectedDate()
        self.label.setText(date.toString('yyyy-MM-dd dddd'))
        self.label.move(20,300)

        self.setWindowTitle("Calendar Demo")

    def showdate(self,date):
        self.label.setText((date.toString("yyyy-MM-dd dddd")))

class DateTimeEdit1(QWidget):
    def __init__(self):
        super(DateTimeEdit1,self).__init__()
        self.initUI()
    def initUI(self):
        vlayout = QVBoxLayout()
        dateTimeEdit1 = QDateEdit()
        dateTimeEdit2 = QDateTimeEdit(QDateTime.currentDateTime())
        dateTimeEdit1.setMinimumDate(QDate.currentDate().addDays(-365))
        dateTimeEdit2.setMaximumDate(QDate.currentDate().addDays(365))
        dateTimeEdit2.setCalendarPopup(True)  # you can choose calendar on a popup widget.

        dateEdit = QDateTimeEdit(QDate.currentDate())
        timeEdit = QDateTimeEdit(QTime.currentTime())
        dateTimeEdit1.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateTimeEdit2.setDisplayFormat("yyyy/MM/dd HH:mm:ss")
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        dateEdit.setCalendarPopup(True)
        timeEdit.setDisplayFormat("HH:mm:ss")

        dateTimeEdit1.dateTimeChanged.connect(self.ondatetimechanged)  # set the signal
        dateEdit.dateChanged.connect(self.ondatechanged)
        dateTimeEdit2.timeChanged.connect(self.ontimechanged)

        vlayout.addWidget(dateTimeEdit1)
        vlayout.addWidget(dateTimeEdit2)
        vlayout.addWidget(dateEdit)
        vlayout.addWidget(timeEdit)
        self.setLayout(vlayout)

        self.resize(300,90)
        self.setWindowTitle("data and time")
    def ondatechanged(self,date):                      # this is a slot
        print(date)
    def ontimechanged(self,time):
        print(time)
    def ondatetimechanged(self,datetime):
        print(datetime)

class TableView(QWidget):
    # display two-dimension form. QTableView.
    # we should creat an QTableView object and a Model, then we need to connect them. it is like MVC(Model Viewer Controller)
    def __init__(self,arg=None):
        super(TableView,self).__init__(arg)

        self.model = QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(['ID','name','age'])
        self.tableview = QTableView()           # creat QTableView object.
        self.tableview.setModel(self.model)     # object and model connection.\
        # add data
        item11 = QStandardItem('10')
        item12 = QStandardItem("jack")
        item13 = QStandardItem("27")
        self.model.setItem(0,0,item11)
        self.model.setItem(0,1,item12)
        self.model.setItem(0,2,item13)

        layout = QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)

        self.setWindowTitle("QTableView Demo")
        self.resize(500,300)

class TableWidgetDemo(QWidget):
    # setItem : place the text into the cell.
    # setCellWidget : place one widget into a cell.
    # setStyleSheet : set the stytle of Widget(QSS)
    def __init__(self):
        super(TableWidgetDemo,self).__init__()
        self.initUI()

    def initUI(self):

        tablewidget = QTableWidget()
        tablewidget.setRowCount(10)
        tablewidget.setColumnCount(3)
        tablewidget.setHorizontalHeaderLabels(['NAME','AGE','BIRTHPLACE'])
        tablewidget.setVerticalHeaderLabels(['A','B','C'])
        nameItem = QTableWidgetItem("Xiao Ming")
        ageItem = QTableWidgetItem("23")
        birthplaceItem = QTableWidgetItem("Da Qing")
        tablewidget.setItem(0,0,nameItem)
        tablewidget.setItem(0,1,ageItem)
        tablewidget.setItem(0,2,birthplaceItem)
        tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)       # Edit is forbidden.
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)      # the whole row will be selected when you choose.
        tablewidget.resizeColumnsToContents()                               # adjust the rows and columns
        tablewidget.resizeRowsToContents()
        # tablewidget.horizontalHeader().setVisible(False)                   # hide the header of the form
        #tablewidget.setShowGrid(False)                                      # hide the grid of a form

        combox = QComboBox()
        combox.addItem('Men')
        combox.addItem('Women')
        # QSS
        combox.setStyleSheet('QComboBox(margin:5px)')
        tablewidget.setCellWidget(1,0,combox)

        modifyButton = QPushButton("Modify")
        modifyButton.setDown(True)                              # defaut status : this button is pushed.
        modifyButton.setStyleSheet('QPushButton(margin:5px)')
        tablewidget.setCellWidget(1,2,modifyButton)


        layout = QHBoxLayout()
        layout.addWidget(tablewidget)
        self.setLayout(layout)
        self.setWindowTitle("TableWidgetDemo")
        self.resize(500,500)

class ListViewDemo(QWidget):
    def __init__(self,parent=None):
        super(ListViewDemo,self).__init__(parent)

        listView = QListView()
        listModel = QStringListModel()
        self.list = ["listItem1",'listItem2','listItem3']
        listModel.setStringList(self.list)
        listView.setModel(listModel)
        listView.clicked.connect(self.clicked)

        layout = QVBoxLayout()
        layout.addWidget(listView)

        self.setLayout(layout)
        self.resize(300,500)
        self.setWindowTitle("ListView Demo")

    def clicked(self,item):
        QMessageBox.information(self,"QListView","You have choosed :"+self.list[item.row()])

class ListWidgetDemo(QWidget):
    def __init__(self,parent=None):
        super(ListWidgetDemo,self).__init__(parent)
        self.listwidget = QListWidget()
        self.listwidget.resize(300,200)
        self.listwidget.addItem("item1")
        self.listwidget.addItem("item2")
        self.listwidget.addItem("item3")
        self.listwidget.addItem("item4")
        self.listwidget.addItem("item5")
        self.listwidget.itemClicked.connect(self.clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.listwidget)
        self.setLayout(layout)
        self.resize(300,270)
        self.setWindowTitle("QListWidget Demo")

    def clicked(self,index):
        print(self.listwidget.item(self.listwidget.row(index)).text())

class BasicTreeWidget(QMainWindow):
    def __init__(self,parent=None):
        super(BasicTreeWidget,self).__init__(parent)

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)                     # set column count
        self.tree.setHeaderLabels(['Key','Value'])      # set label for column
        root = QTreeWidgetItem(self.tree)
        root.setText(0,"Root node")
        root.setIcon(0,QIcon('./images/7773/y2.ico'))
        self.tree.setColumnWidth(0,120)
        # add children node
        child1 = QTreeWidgetItem(root)
        child1.setText(0,"chirdren 1")
        child1.setText(1,"Children 2")
        child1.setIcon(0,QIcon("./images/7773/y1.ico"))
        #child1.setCheckState(0,Qt.Checked)

        child2 = QTreeWidgetItem(root)
        child2.setText(0,'child_2')
        child2.setIcon(0,QIcon('./images/7773/y2.ico'))

        child2_1 = QTreeWidgetItem(child2)
        child2_1.setText(0,"child node 2-1")
        child2_1.setText(1,"new Value")
        child2_1.setIcon(0,QIcon("./images/7773/y3.ico"))

        self.tree.expandAll()

        self.setWindowTitle("Tree Widget")
        self.resize(500,500)
        self.setCentralWidget(self.tree)

        self.tree.clicked.connect(self.onTreeClicked)

    def onTreeClicked(self,index):
        item = self.tree.currentItem()
        print(index.row())
        print('key=%s,value=%s' %(item.text(0),item.text(1)))

class ModifyTree(QWidget):
    def __init__(self):
        super(ModifyTree,self).__init__()

        self.tree = QTreeWidget()
        self.tree.setColumnCount(2)  # set column count
        self.tree.setHeaderLabels(['Key', 'Value'])  # set label for column
        root = QTreeWidgetItem(self.tree)
        root.setText(0, "Root node")
        root.setIcon(0, QIcon('./images/7773/y2.ico'))
        self.tree.setColumnWidth(0, 220)


        operateLayout = QHBoxLayout()
        addBtn = QPushButton("Add Node")
        updateBtn = QPushButton("Modify Node")
        deleteBtn = QPushButton("Delete Node")

        operateLayout.addWidget(addBtn)
        operateLayout.addWidget(updateBtn)
        operateLayout.addWidget(deleteBtn)

        addBtn.clicked.connect(self.addNode)
        updateBtn.clicked.connect(self.updateNode)
        deleteBtn.clicked.connect(self.deletNode)

        mainLayout = QVBoxLayout(self)
        mainLayout. addLayout(operateLayout)
        mainLayout.addWidget(self.tree)
        self.setLayout(mainLayout)
        self.resize(700,1000)

    def addNode(self):
        print("add")
        item = self.tree.currentItem()              # get the current node
        print(item)
        node = QTreeWidgetItem(item)
        node.setText(0,"New Node")
        node.setText(1,"New Value")
    def updateNode(self):
        print("modify")
        item = self.tree.currentItem()
        item.setText(0,"modify")
        item.setText(1,"Value was changed")
    def deletNode(self):
        print("delete")
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root()).removeChild(item)

if __name__ == "__main__":
    opp = QApplication(sys.argv)
    main = ModifyTree()
    main.show()
    sys.exit(opp.exec_())