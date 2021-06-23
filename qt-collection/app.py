from PyQt5 import QtWidgets, QtGui, QtCore, uic
from cryptography.fernet import Fernet
import sys
import resources

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PyQt5.QtWinExtras import QtWin
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 加载resources中的ui（注意prefix）
        fileh = QtCore.QFile(':/ui/locker.ui')
        fileh.open(QtCore.QFile.ReadOnly)
        uic.loadUi(fileh, self)
        fileh.close()
        self.lock = Fernet(b'8GiEHryrOId7fJd9K8CeMAuubCjsL1UX5DDZWARByCE=')
        # 绑定关系
        self.encodeButton.clicked.connect(self.encodeText)
        self.decodeButton.clicked.connect(self.decodeText)
        self.pushButton.clicked.connect(self.fileDialog)
        # 
        menubar = self.menuBar()
    
    def fileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)", options=options)
        if fileName:
            print(fileName)

    def encodeText(self):
        before = self.beforeText.toPlainText()
        cryptext = self.lock.encrypt(bytes(before, encoding='utf-8')).decode()
        self.afterText.setPlainText(cryptext)
    
    def decodeText(self):
        before = self.beforeText.toPlainText()
        cryptext = self.lock.decrypt(bytes(before, encoding='utf-8')).decode()
        self.afterText.setPlainText(cryptext)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(':/icons/favicon.ico'))
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())