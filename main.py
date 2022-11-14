import time
import random
from datetime import datetime
from pywinauto import Application


sleep_times = [0.5, 1, 1.5, 2, 2.5]


def press_keys():
    t1 = random.choice(sleep_times)
    print("wait for {} seconds...".format(t1))
    time.sleep(t1)
    for k in ["1", '{F12}', "1", "1", "2", "3", '{SPACE}']:
        print(message.format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), key=k))
        form.send_keystrokes(k)
        t2 = random.choice(sleep_times)
        print("wait for {} seconds...".format(t2))
        time.sleep(t2)


if __name__ == "__main__":
    app = Application(backend="win32").connect(process=16560)
    form = app.window(title_re="魔兽世界")
    message = "pressing key >{key}< @ {time}"
    print("-" * 10)
    while True:
        press_keys()
        print("-" * 10)

