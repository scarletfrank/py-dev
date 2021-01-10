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
        self.nstack = [4] # number stack
        self.ostack = [] # operator stack
        self.ans = 0.0 # float ans
        # 组件绑定
        self.tb_1.clicked.connect(self.num_add(1))
        self.tb_2.clicked.connect(self.num_add(2))
        self.tb_3.clicked.connect(self.num_add(3))
        self.tb_4.clicked.connect(self.num_add(4))
        self.tb_5.clicked.connect(self.num_add(5))
        self.tb_6.clicked.connect(self.num_add(6))
        self.tb_7.clicked.connect(self.num_add(7))
        self.tb_8.clicked.connect(self.num_add(8))
        self.tb_9.clicked.connect(self.num_add(9))
        self.tb_0.clicked.connect(self.num_add(0))
        self.tb_point.clicked.connect(self.num_add('.'))
        self.tb_show.clicked.connect(self.testStack)
        # 加减乘除
        self.btn_plus.clicked.connect(self.addlogic)
        self.btn_assign.clicked.connect(self.callogic)

    def log(self, s: str):
        self.label.setText(self.label.text() + "\n" + s)

    def testStack(self):
        self.log(repr(self.nstack))
        self.log(repr(self.ostack))

    def addlogic(self):
        """
        符号+ 逻辑：1. 推入数字 2. 推入符号
        """
        try:
            self.nstack.append(float(self.lineEdit.text())) # 数值转换
            self.ostack.append('+')
        except Exception as e:
            # Alert
            print('Reason:', e)
        finally:
            self.lineEdit.clear()

    def num_add(self, n):
        """
        给lineEdit增加数字
        """
        def callnum():
            self.lineEdit.setText(self.lineEdit.text() + str(n))
        return callnum # 带参数的情况下，要返回对应参数的函数

    def callogic(self):
        """
        按下=号的逻辑:1、取一个符号，清空lineEdit 2、取两个数字计算 3、新结果打印及推入
        """
        if len(self.nstack) < 2:
            return
        else:
            try:
                self.nstack.append(float(self.lineEdit.text())) # 数值转换
                self.lineEdit.clear()
            except Exception as e:
                print('Reason:', e)
            oper = self.ostack.pop()
            rn = self.nstack.pop()
            ln = self.nstack.pop()
            cals = f"{ln}{oper}{rn}"
            self.label.setText(self.label.text() + "\n" + cals)
            print(cals)
            self.nstack.append(eval(cals))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icons/favicon.ico'))
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())