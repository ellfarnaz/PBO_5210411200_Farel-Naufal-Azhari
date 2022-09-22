

from pynput.keyboard import *
import pyautogui
import win32com.client
import win32gui
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

lang = 'jp'

tofApp = win32gui.FindWindow(None, 'Tower of Fantasy  ')
shell = win32com.client.Dispatch("WScript.Shell")

shell.SendKeys('%')
win32gui.SetForegroundWindow(tofApp)

delay = 0.000000001
button = Button.left
start_stop_key = KeyCode(char='x')
exit_key = KeyCode(char='z')
pause_key = Key.f2
resume_key = Key.f1
#  ==========================

pause = True
running = True


def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


class ClickMouse(threading.Thread):
    print("// AutoClicker by iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t x = Star and Stop")
    print("\t z = Exit")
    print("-----------------------------------------------------")
    print('Press X to start and stop  click...')

    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True

    def main():
        lis = Listener(on_press=on_press)
        lis.start()
        while running:
            if not pause:
                pyautogui.hotkey('F')
                pyautogui.PAUSE = delay
        lis.stop()

    def start_clicking(self):
        self.running = True
        print("[Star]")

    def stop_clicking(self):
        self.running = False
        print("[Pause]")

    def exit(self):
        self.stop_clicking()
        self.program_run = False

    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.00001)


mouse = Controller()
thread = ClickMouse(delay, button)
thread.start()


def on_press(key):
    if key == start_stop_key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key == exit_key:
        thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
