import time
import random
from datetime import datetime

from PyQt5.QtCore import QObject, pyqtSignal
from pywinauto import Application


class Worker(QObject):

    finished = pyqtSignal()

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True
        self.wow_pid = 0

    def start(self):
        wow = Application(backend="win32").connect(process=self.wow_pid)
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

        self.finished.emit()

    def stop(self):
        self.continue_run = False