from PyQt6 import QtWidgets
import sys

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1920, 1080)
        self.setWindowTitle("Page 1")
        self.setup_ui()

    def setup_ui(self):
        # Create main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        header_widget = self.create_header()

        # Add header to main layout
        main_layout.addWidget(header_widget)

        # Add buttons with different texts
        initial_button_text1 = "Click Me!"
        button_widget1 = self.create_button(initial_button_text1)
        main_layout.addWidget(button_widget1)

        initial_button_text2 = "Click Me 2!"
        button_widget2 = self.create_button(initial_button_text2)
        main_layout.addWidget(button_widget2)

        self.setLayout(main_layout)

    def create_header(self):
        # Header container
        header_widget = QtWidgets.QWidget(self)
        header_layout = QtWidgets.QHBoxLayout(header_widget)

        # Company title
        company_title_label = QtWidgets.QLabel("XXX電子有限公司", self)
        company_title_label.setStyleSheet('''
            font-size: 30px;
            background: green;
            color: white;
        ''')

        # Menu label
        menu_label = QtWidgets.QLabel("菜單", self)
        menu_label.setStyleSheet('''
            font-size: 30px;
            background: pink;
        ''')

        # Add labels to header layout
        header_layout.addWidget(company_title_label)
        header_layout.addWidget(menu_label)
        header_widget.setLayout(header_layout)

        return header_widget

    def create_button(self, text):
        # Button widget
        button_widget = QtWidgets.QWidget(self)
        button_layout = QtWidgets.QVBoxLayout(button_widget)

        # Button
        button = QtWidgets.QPushButton(text, self)  # Set text dynamically
        button.setStyleSheet('''
            QPushButton {
                font-size: 20px;
                color: #f00;
                background: #ff0;
                border: 2px solid #000;
            }
            QPushButton:hover {
                color: #ff0;
                background: #f00;
            }
        ''')
        button_layout.addWidget(button)
        button_widget.setLayout(button_layout)

        return button_widget


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec())
