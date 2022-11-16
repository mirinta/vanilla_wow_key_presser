import os

import psutil
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QPushButton, QListWidget, QAbstractItemView
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QCloseEvent

from core.Worker import Worker


class MainWindow(QMainWindow):

    stop_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Vanilla WoW Battleground Assist")
        self.setWindowIcon(QIcon(os.path.join(os.getcwd(), "resource/icon.png")))
        self.setCentralWidget(QWidget())
        self.main_layout = QVBoxLayout()
        self.centralWidget().setLayout(self.main_layout)

        self.pid_list = QListWidget()
        self.pid_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pid_list.currentRowChanged.connect(self.on_pid_changed)
        pid_layout = QVBoxLayout()
        pid_layout.addWidget(QLabel("Running PID(s) of WowClassic.exe"))
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
        self.main_layout.addLayout(button_layout)
        self.refresh_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(False)

        self.worker = None
        self.thread = None

    def on_refresh_clicked(self):
        self.pid_list.clear()
        self.pid_list.addItems([str(p.pid) for p in psutil.process_iter() if p.name() == "WowClassic.exe"])

    def on_start_clicked(self):
        if not self.pid_list.count() or self.pid_list.currentRow() < 0:
            return

        self.thread = QThread()
        self.worker = Worker()
        self.stop_signal.connect(self.worker.stop)
        self.worker.wow_pid = int(self.pid_list.currentItem().text())
        self.worker.moveToThread(self.thread)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)

        self.thread.started.connect(self.update_button_status)
        self.thread.started.connect(self.worker.start)
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
