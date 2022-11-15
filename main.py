import sys
import time
import random
from datetime import datetime

import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, \
    QListWidget, QAbstractItemView
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from pywinauto import Application


class Worker(QObject):

    work_finished = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True
        self.pid = 0

    def do_work(self):
        wow = Application(backend="win32").connect(process=self.pid)
        form = wow.window(title_re="魔兽世界")
        message = "pressing key >{key}< @ {time}"
        sleep_times = [0.5, 1, 1.5, 2, 2.5]

        print("-" * 10)
        while self.continue_run:
            t1 = random.choice(sleep_times)
            print("wait for {} seconds...".format(t1))
            time.sleep(t1)
            for k in ["1", '{F12}', "1", "1", "2", "3", '{SPACE}']:
                print(message.format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), key=k))
                form.send_keystrokes(k)
                t2 = random.choice(sleep_times)
                print("wait for {} seconds...".format(t2))
                time.sleep(t2)
            print("-" * 10)

        self.work_finished.emit()

    def stop(self):
        self.continue_run = False


class MyWindow(QMainWindow):

    stop_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setWindowTitle("Vanilla WoW Battleground Assist")
        self.setCentralWidget(QWidget())
        self.main_layout = QVBoxLayout()
        self.centralWidget().setLayout(self.main_layout)

        self.pid_list = QListWidget()
        self.pid_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pid_list.currentRowChanged.connect(self.on_pid_changed)
        pid_layout = QVBoxLayout()
        pid_layout.addWidget(QLabel("Running PID of WowClassic.exe"))
        pid_layout.addWidget(self.pid_list)
        self.main_layout.addLayout(pid_layout)

        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.on_refresh_clicked)
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.on_stop_clicked)
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.on_start_clicked)
        button_layout = QHBoxLayout()
        for btn in [self.refresh_button, self.stop_button, self.start_button]:
            btn.setFixedHeight(80)
            button_layout.addWidget(btn)
        self.refresh_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(False)
        self.main_layout.addLayout(button_layout)

    def on_refresh_clicked(self):
        self.pid_list.clear()
        self.pid_list.addItems([str(p.pid) for p in psutil.process_iter() if p.name() == "WowClassic.exe"])

    def on_start_clicked(self):
        self.thread = QThread()
        self.worker = Worker()
        self.stop_signal.connect(self.worker.stop)

        self.worker.pid = int(self.pid_list.currentItem().text())
        self.worker.moveToThread(self.thread)
        self.worker.work_finished.connect(self.thread.quit)
        self.worker.work_finished.connect(self.worker.deleteLater)

        self.thread.started.connect(self.update_button_status)
        self.thread.started.connect(self.worker.do_work)
        self.thread.finished.connect(self.worker.stop)
        self.thread.finished.connect(self.update_button_status)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def on_stop_clicked(self):
        self.stop_signal.emit()

    def on_pid_changed(self, index):
        no_selection = index < 0 or self.pid_list.count() == 0
        self.start_button.setDisabled(no_selection)

    def update_button_status(self):
        self.refresh_button.setEnabled(self.thread.isFinished())
        self.stop_button.setDisabled(self.thread.isFinished())
        self.start_button.setEnabled(self.thread.isFinished())
        self.pid_list.setEnabled(self.thread.isFinished())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    sys.exit(app.exec_())

