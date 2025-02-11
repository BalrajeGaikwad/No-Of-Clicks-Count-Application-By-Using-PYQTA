from PyQt5 import QtWidgets
from win_ui import Ui_MainWindow

class mainwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwin, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.Number_Of_Clicks=0
        self.ui.pushButton_click.pressed.connect(self.update_clicks)
        self.show()

    def update_clicks(self):
        self.Number_Of_Clicks+=1
        self.ui.click_count_label.setText(f"Number Of Clicks {self.Number_Of_Clicks}")


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    obj=mainwin()
    sys.exit(app.exec_())