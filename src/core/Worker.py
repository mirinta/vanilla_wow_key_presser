import random
import time
from datetime import datetime

from PyQt5.QtCore import QObject, pyqtSignal
from pywinauto import Application


class Worker(QObject):
    work_finished = pyqtSignal()
    msg_reported = pyqtSignal(str)

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True
        self.wow_pid = 0

    def start(self):
        wow = Application(backend="win32").connect(process=self.wow_pid)
        form = wow.window(title_re="魔兽世界")
        time_message = "wait for {} seconds..."
        key_message = "press key >{key}< @ {time}"
        sleep_times = [0.5, 1, 1.5, 2, 2.5]

        self.msg_reported.emit("***** work started *****")
        while self.continue_run:
            t1 = random.choice(sleep_times)
            self.msg_reported.emit(time_message.format(t1))
            time.sleep(t1)
            for k in ["1", '{F12}', "1", "1", "2", "3", '{SPACE}']:
                self.msg_reported.emit(key_message.format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), key=k))
                form.send_keystrokes(k)
                t2 = random.choice(sleep_times)
                self.msg_reported.emit(time_message.format(t2))
                time.sleep(t2)
            self.msg_reported.emit("-" * 10)

        self.work_finished.emit()
        self.msg_reported.emit("***** work finished *****")

    def stop(self):
        self.continue_run = False
