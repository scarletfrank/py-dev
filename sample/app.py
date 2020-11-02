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
        self.toolButton_1.clicked.connect(self.num_add(1))
        self.toolButton_2.clicked.connect(self.num_add(2))
        self.toolButton_3.clicked.connect(self.num_add(3))
        self.toolButton_4.clicked.connect(self.num_add(4))
        self.toolButton_5.clicked.connect(self.num_add(5))
        self.toolButton_6.clicked.connect(self.num_add(6))
        self.toolButton_7.clicked.connect(self.num_add(7))
        self.toolButton_8.clicked.connect(self.num_add(8))
        self.toolButton_9.clicked.connect(self.num_add(9))
        self.toolButton_0.clicked.connect(self.num_add(0))

    def num_add(self, n):
        def callnum():
            self.lineEdit.setText(self.lineEdit.text() + str(n))
        return callnum # 带参数的情况下，要返回对应参数的函数


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icons/favicon.ico'))
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())