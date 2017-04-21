import sys
import os
from PySide import QtGui

from mayatools.ui import playblastUI

reload(playblastUI)

# styles :
styles_dir = os.path.join(os.path.dirname(__file__), 'styles')
qt_dark_blue = os.path.join(styles_dir, 'qt_dark_blue.qss')
# qt_dark_green = os.path.join(styles_dir, 'qt_dark_green.qss')
qt_dark_orange = os.path.join(styles_dir, 'qt_dark_orange.qss')

with open(qt_dark_blue, 'r') as fid:
    QTDark = fid.read()


class PlayblastUIConn(QtGui.QMainWindow, playblastUI.Ui_MainWindow):
    def __init__(self):
        super(PlayblastUIConn, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(QTDark)
        self.connections()

    def connections(self):
        self.custom_res_CB.stateChanged.connect(self.resOnOff)
        # self.custom_res_CB.clicked.connect(self.resOnOff)

    def abcdaf(self):
        print 1111111111111111111

    def resOnOff(self):
        self.custResX_SB.setEnabled(self.custom_res_CB.checkState())
        self.custResY_SB.setEnabled(self.custom_res_CB.checkState())


def main():
    app = QtGui.QApplication(sys.argv)
    win = PlayblastUIConn()
    win.show()
    return app.exec_()


if __name__ == '__main__':
    win = main()
