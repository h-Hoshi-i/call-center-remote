import pyautogui as auto
from time import sleep
import first_name as firna
import threading
import pyperclip as clip
import compileEmail as mmail

first_name = None

def grab_name():
    global first_name
    first_name = firna.first_name_grabber()

def open_record_and_form():
    auto.press("home")
    auto.click(x=962, y=558)
    sleep(0.5)
    while True:
        if auto.pixelMatchesColor(123, 149, [255,255,255]):
            sleep(0.2)
            break
        else:
            sleep(0.2)
    auto.click(x=1395, y=165)
    sleep(0.1)
    auto.press("tab", presses=9, interval=0.15)
    clip.copy("vm and email sent")
    auto.hotkey("ctrl", "v")
    auto.press("tab")
    auto.press("m")
    auto.press("tab", presses=2, interval=0.15)
    auto.press("down")
    auto.hotkey("shift", "tab")
    auto.press("enter")
    while True:
        if auto.pixelMatchesColor(565,299,[227,230,150]):
            auto.press("esc") #break out of email for first time
            break
        else:
            sleep(0.2)

def dashboard_email(user_name:str = "Nathaniel"):
    auto.click(x=103, y=972)
    auto.press("home")
    sleep(0.2)
    thread1 = threading.Thread(target=grab_name)
    thread1.start()
    auto.click(x=1395, y=165)
    auto.press("tab", presses=11, interval=0.15)
    auto.press("enter")
    while True:
        if auto.pixelMatchesColor(565,299,[227,230,150]):
            break
        else:
            sleep(0.2)
    auto.press("right")
    auto.press("tab", presses=5, interval=0.1)
    clip.copy("Reconnecting with Southern Adventist University")
    auto.hotkey("ctrl","v")
    auto.click(x=1033, y=538) #click html source
    auto.press("tab")
    auto.hotkey("ctrl","a")
    thread1.join()
    sleep(0.1)
    email = mmail.select_email("previous2026", stu_name=first_name, user_name=user_name)
    clip.copy(email)
    auto.hotkey("ctrl", "v")
    auto.click(x=1033, y=538)

    

if __name__ == "__main__":
    sleep(2)
    #open_record_and_form()
    dashboard_email()