#check if i'm playing apex legends instead of studying
#minimize the Game
#play an annoying ass sound
#test on home PC

import win32ui
import win32gui
import time
import winsound

localtime = time.asctime(time.localtime(time.time())

#download some annoying sound and place it in script dir as alert.wav
def areYouGaming(localtime):
    if FindWindow("Apex Legends", "Apex Legends"):
        print "Apex Legends found at ", localtime
        time.sleep(200)
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        winsound.Playsound('alert.wav', winsound.SND_FILENAME)
        
while True:
    areYouGaming()
