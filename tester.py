import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem

class list_test(QApplication):
    def __init__(self, list_given):
        super(list_test, self).__init__(list_given)
        self.resize(500,500)
        self.listIn = list_given

        for x in self.listIn:
            self.addItem(x)

    



app = QApplication(sys.argv)
listTBP = [["egg","sock","2"],["cheese","mad","4"],["rh","bruh", "19"]]
test = list_test(listTBP)
test.show()

sys.exit(app.exec_())
