"""
tutorial: https://maicss.gitbooks.io/pyqt5
"""

import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QToolTip, QPushButton
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction
from PyQt5.QtGui import QFont

def demo_01():
    """ 展示Qt设计的GUI的最简单效果
    """
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(400, 400)
    widget.setWindowTitle('Qt用户界面程序测试')
    widget.show()
    sys.exit(app.exec_())

def demo_02():
    """ 展示Qt添加按钮的效果
    """
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(400, 400)
    widget.setWindowTitle('Qt用户界面程序测试')
    QToolTip.setFont(QFont('SansSerif', 10))
    # 设置按钮
    btn = QPushButton('按钮', widget)
    btn.setToolTip('这是一个<b style="color:blue;">QPushButton</b>')
    btn.resize(btn.sizeHint())
    btn.move(100,100)

    widget.show()
    sys.exit(app.exec_())

def demo_03():
    """ 展示Qt添加状态栏的效果
    """
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.resize(400, 400)
    win.setWindowTitle('Qt用户界面程序测试')
    win.statusBar().showMessage('一切准备就绪')
    win.show()
    sys.exit(app.exec_())

def demo_04():
    """ 展示Qt添加菜单栏的效果
    """
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.resize(400, 400)
    win.setWindowTitle('Qt用户界面程序测试')

    menubar = win.menuBar()
    menubar.setNativeMenuBar(False)
    fileMenu = menubar.addMenu('&File')
    editMenu = menubar.addMenu('&Edit')
    selectMenu = menubar.addMenu('&Selection')
    viewMenu = menubar.addMenu('&View')
    goMenu = menubar.addMenu('&Go')
    runMenu = menubar.addMenu('&Run')
    terminalMenu = menubar.addMenu('&Terminal')
    windowMenu = menubar.addMenu('&Window')
    helpMenu = menubar.addMenu('&Help')

    importMenu = QMenu('导入')
    newAct = QAction('New', win) 
    importMenu.addAction(newAct)
    exportMenu = QMenu('导出')
    # exportMenu.addAction(newAct)
    fileMenu.addMenu(importMenu)
    fileMenu.addMenu(exportMenu)

    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    demo_04()
