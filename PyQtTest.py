import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My First PyQt6 App')
        self.resize(300, 200)

        layout = QVBoxLayout()
        self.label = QLabel('안녕하세요, PyQt6입니다!', self)
        layout.addWidget(self.label)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec())