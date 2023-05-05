from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI,self).__init__()
        uic.loadUi('frontend.ui',self)
        self.show()

# def set_but_color(window):
#     print("Hi")
#     window.button_left.setStyleSheet("background-color: green")


def main():
    app = QApplication([])
    window = MyGUI()

    # window.button_center.clicked.connect(lambda: set_but_color(window))
    app.exec()

if __name__=="__main__":
    main()