import psycopg2
import sys
from login import *
if __name__ == "__main__":
    App = QApplication(sys.argv)
    aw = Ui_MainWindow()
    w = QMainWindow()
    aw.setupUi(w)
    w.show()
    sys.exit(App.exec_())
