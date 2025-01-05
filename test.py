from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

def load_stylesheet(file_path):
    with open(file_path, "r") as file:
        return file.read()

app = QApplication([])

# 加载 QSS 文件
stylesheet = load_stylesheet("style.qss")
app.setStyleSheet(stylesheet)

# 创建主窗口
window = QWidget()
layout = QVBoxLayout(window)

# 添加按钮
btn1 = QPushButton("Button 1")
btn2 = QPushButton("Button 2")
layout.addWidget(btn1)
layout.addWidget(btn2)

window.setLayout(layout)
window.show()

app.exec()
