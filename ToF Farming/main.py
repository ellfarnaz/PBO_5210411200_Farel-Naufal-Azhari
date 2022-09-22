

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

delay = 0.1  # in seconds
resume_key = Key.f1
pause_key = Key.f3
exit_key = Key.esc
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


def display_controls():
    print("// AutoClicker by iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.hotkey('F')
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
