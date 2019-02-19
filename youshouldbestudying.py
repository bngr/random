#check if i'm playing apex legends instead of studying and then minimize it
import win32ui
import win32gui
import time

localtime = time.asctime(time.localtime(time.time())
def areYouGaming(localtime):
    if FindWindow("Apex Legends", "Apex Legends"):
        print "Apex Legends found at ", localtime
        time.sleep(200)
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minize, win32con.SW_MINIMIZE)
