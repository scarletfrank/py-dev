from PyQt5 import QtWidgets, QtGui, QtCore, uic
import sys
import resources

# 设置任务栏的图标
try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PyQt5.QtWinExtras import QtWin
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # 加载resources中的ui（注意prefix）
        fileh = QtCore.QFile(':/ui/sample.ui')
        fileh.open(QtCore.QFile.ReadOnly)
        uic.loadUi(fileh, self)
        fileh.close()
        
        # 组件绑定
        self.toolButton_1.clicked.connect(self.addone)
        self.btn_clear.clicked.connect(self.clsLine)
        self.btn_label.clicked.connect(self.changeLabel)

    def addone(self):
        self.lineEdit.setText(self.lineEdit.text() + "1")

    def clsLine(self):
        self.lineEdit.clear()

    def changeLabel(self):
        self.label.setText("newHelloWorld")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icons/favicon.ico'))
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())