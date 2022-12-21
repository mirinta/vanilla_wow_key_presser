import random
import time
from datetime import datetime

from PyQt5.QtCore import QObject, pyqtSignal
from pywinauto import Application


class Worker(QObject):
    work_finished = pyqtSignal()
    report_msg = pyqtSignal(str)

    def __init__(self, parent=None):
        QObject.__init__(self, parent=parent)
        self.continue_run = True
        self.wow_pid = 0
        self.key_sequence = ["1", '{F12}', "1", "1", "2", "3", '{SPACE}']
        self.sleep_times = [0.5, 1, 1.5, 2, 2.5]  # sleep x seconds between each key pressing

    def start(self):
        try:
            wow = Application(backend="win32").connect(process=self.wow_pid)
            form = wow.window(title_re="魔兽世界")
            time_message = "wait for {} seconds..."
            key_message = "press key >{key}< @ {time}"

            self.report_msg.emit("***** work started *****")
            while self.continue_run:
                t1 = random.choice(self.sleep_times)
                self.report_msg.emit(time_message.format(t1))
                time.sleep(t1)
                for k in self.key_sequence:
                    self.report_msg.emit(
                        key_message.format(
                            time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            key=k))
                    form.send_keystrokes(k)
                    t2 = random.choice(self.sleep_times)
                    self.report_msg.emit(time_message.format(t2))
                    time.sleep(t2)
                self.report_msg.emit("-" * 10)

            self.work_finished.emit()
            self.report_msg.emit("***** work finished *****")

        except Exception as e:
            self.work_finished.emit()
            self.report_msg.emit("***** work interrupted *****\n{}".format(str(e)))

    def stop(self):
        self.continue_run = False
