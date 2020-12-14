import sys
import pickle
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import *
from subjectSortModule import subjectSort
from dialog import sInputDialog


class TodoListApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'subjectDB.dat'
        self.subjectDB = []
        self.readSubjectDB()
        self.showSubjectDB()


    def initUI(self):

        # 추가, 완료, 수정 버튼
        addButton = QPushButton('추가', self)
        delButton = QPushButton('삭제', self)
        sortButton = QPushButton('정렬', self)

        addButton.clicked.connect(lambda: self.addButtonClicked())
        delButton.clicked.connect(lambda: self.delButtonClicked())
        sortButton.clicked.connect(lambda: self.sortButtonClicked())


        # 학번, 이름
        nameLabel = QLabel('202030xx 이OO', self)


        # 할 일 목록 만들기

        self.todoList = QTableView(self)
        self.todoList.setAlternatingRowColors(True)
        self.todoList.resize(400, 200)

        self.text = QStandardItemModel(0, 3, self)
        self.text.setHeaderData(0, Qt.Horizontal, "할 일")
        self.text.setHeaderData(1, Qt.Horizontal, "중요도")
        self.text.setHeaderData(2, Qt.Horizontal, "마감기한")

        self.todoList.setModel(self.text)
        self.todoList.setColumnWidth(0, 150)
        self.todoList.setColumnWidth(1, 80)


        # Layout배치

        buttonBox = QHBoxLayout()
        buttonBox.addWidget(addButton)
        buttonBox.addWidget(delButton)
        buttonBox.addWidget(sortButton)
        buttonBox.addStretch(1)

        nameBox = QHBoxLayout()
        nameBox.addStretch(1)
        nameBox.addWidget(nameLabel)

        todoBox = QHBoxLayout()
        todoBox.addWidget(self.todoList)

        mainLayout = QVBoxLayout()
        mainLayout.addLayout(buttonBox)
        mainLayout.addStretch(1)
        mainLayout.addLayout(nameBox)
        mainLayout.addLayout(todoBox)

        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 366, 300)
        self.setWindowTitle("To-do List")  # 타이틀 바꾸기
        # self.show()


    def addButtonClicked(self):
        dlg = sInputDialog()
        dlg.exec_()
        if dlg.subjectName != "" and dlg.priority != None:
            try:
                record = {'subjectName': dlg.subjectName, 'priority': dlg.priority, 'deadLine': dlg.deadLine}
                self.subjectDB += [record]
                self.showSubjectDB()
            except:
                pass
        return


    def delButtonClicked(self):

        text, ok = QInputDialog.getText(self, '삭제', '삭제할 과제명을 입력해 주세요:')

        if ok:
            t = text

            try:
                for task in self.subjectDB:
                    if t == task["subjectName"]:
                        self.subjectDB.remove(task)
                        break
            except IndexError as e:
                pass
        self.showSubjectDB()
        return


    def sortButtonClicked(self):
        self.subjectDB = subjectSort(self.subjectDB)
        self.subjectDB = sorted(self.subjectDB, key=lambda person: person['orderScore'])
        #print(self.subjectDB)
        self.showSubjectDB()
        return


    # DB에서 정보를 불러들이는 함수
    def readSubjectDB(self):
        try:
            fH = open(self.dbfilename)
        except FileNotFoundError as e:
            self.subjectDB = []
            return

        try:
            line = fH.read()
            self.subjectDB = eval(line)
        except:
            pass
        else:
            pass
        fH.close()

    # DB에서 불러온 정보를 화면에 표현하는 함수
    def showSubjectDB(self):
        # 테이블뷰 업데이트를 위해 이전테이블을 모두 지움
        self.text.removeRows(0, self.text.rowCount())

        # 테이블뷰에 subjectDB에 저장된 정보를 입력함
        row = 0
        for p in self.subjectDB:
            #print(p)
            col = 0
            self.text.insertRows(self.text.rowCount(), 1)
            for attr in p:
                self.text.setData(self.text.index(row, col), str(p[attr]))
                col += 1
            row += 1

    def writeSubjectDB(self):
        fH = open(self.dbfilename, 'w')
        fH.write(str(self.subjectDB) + '\n')
        fH.close()

    def closeEvent(self, event):
        self.writeSubjectDB()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApp = TodoListApp()
    mainApp.show()
    sys.exit(app.exec_())
