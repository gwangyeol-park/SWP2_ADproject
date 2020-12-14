from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
import sys


class sInputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

        self.subjectName = None
        self.priority = None
        self.deadLine = None

    def setupUI(self):
        self.setGeometry(350, 350, 300, 100)
        self.setWindowTitle("추가")

        ...


        label1 = QLabel("과제명: ")
        label2 = QLabel("중요도: ")
        label3 = QLabel("마감일: ")

        # 과제명을 입력하기위한 라인에딧
        self.lineEdit1 = QLineEdit()

        # 중요도를 입력하기위한 콤보박스
        self.comboBox1 = QComboBox(self)
        self.comboBox1.addItem('상')
        self.comboBox1.addItem('중상')
        self.comboBox1.addItem('중')
        self.comboBox1.addItem('중하')
        self.comboBox1.addItem('하')

        # 마감일을 입력하기 위한 데이트에딧
        self.dateedit1 = QDateEdit(self)
        self.dateedit1.setDate(QDate.currentDate())
        self.dateedit1.setMinimumDate(QDate(1900, 1, 1))
        self.dateedit1.setMaximumDate(QDate(2100, 12, 31))
        self.dateedit1.setCalendarPopup(True)

        # 정보입력이 완료됬음을 알리는 버튼
        self.pushButton1= QPushButton("완료")
        self.pushButton1.clicked.connect(self.pushButton1Clicked)

        # 위에서 만든 라인에딧, 콤보박스, 데이트에딧을 레이아웃에 배치
        layout = QGridLayout()
        layout.addWidget(label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(label2, 1, 0)
        layout.addWidget(self.comboBox1, 1, 1)
        layout.addWidget(label3, 2, 0)
        layout.addWidget(self.dateedit1, 2, 1)
        layout.addWidget(self.pushButton1, 3, 3)

        self.setLayout(layout)

    def pushButton1Clicked(self):
        self.subjectName = self.lineEdit1.text()
        self.priority = self.comboBox1.currentText()
        self.deadLine = self.dateedit1.date().toString("yyyy.MM.dd")
        self.close()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   w = sInputDialog()

   sys.exit(app.exec_())