from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1920, 1080)
        self.setWindowTitle("page1")
        self.header()
        self.buttonItem()
    def header(self):
        # self.hbox = QtWidgets.QWidget(self)
        # self.hbox.setGeometry(150,0,500,150)
        # self.h_layout = QtWidgets.QHBoxLayout(self.hbox)
        # company_title_label = self.companyTitle()
        # menu_label = self.menu() 
        # self.h_layout.addWidget(company_title_label)
        # self.h_layout.addWidget(menu_label)
        self.label = QtWidgets.QLabel(self)
        self.label.setStyleSheet('''
                background:blue;
            ''')
        self.companyTitle()
        self.menu()
    # def container(self):



    def companyTitle(self):
        self.label = QtWidgets.QLabel(self)
        self.label.move(10,0)
        self.label.setText('XXX電子有限公司')
        self.label.setStyleSheet('''
                font-size:30px;
                background:green;
            ''')
        
    def menu(self):
        self.label = QtWidgets.QLabel(self)
        self.label.move(500,0)
        self.label.setText('菜單')
        self.label.setStyleSheet('''
                font-size:30px;
                background:pink;
            ''')

#元件        
    def buttonItem(self):
        self.item = QtWidgets.QPushButton(self)
        self.item.setText("123")
        self.item.setGeometry(30, 60, 100, 20)
        self.item.setStyleSheet('''
            QPushButton {
                font-size:20px;
                color: #f00;
                background: #ff0;
                border: 2px solid #000;
            }
            QPushButton:hover {
                color: #ff0;
                background: #f00;
            }
            ''')
   
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = MyWidget()
    Form.show()
    sys.exit(app.exec())