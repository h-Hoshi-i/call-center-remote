import pyautogui as auto
from time import sleep
import pyperclip as clip
import compileEmail

fetchNext = auto.Point(x=103,y=294)#done
stuRecord = auto.Point(x=996,y=440)#done
underSubForm = auto.Point(x=808, y=535)#done
contDeets = auto.Point(x=673, y=781)
emailcoord = auto.Point(x=598, y=505)
source = auto.Point(x=998, y=445)

#"tab" - paste in comment title
#"tab" - paste in call summary
#end

def open_record():
    #auto.click(fetchNext)
    #check if screen is ready
    while True:
        if auto.pixel(574, 381) == (255, 255, 255):
            sleep(0.1)
            break
        else:
            sleep(0.5)

    auto.click(stuRecord)

def open_sub_form():
    auto.click(underSubForm)
    auto.press("tab")
    sleep(0.15)
    auto.press("tab")
    sleep(0.1)
    auto.press("enter")

def fillout_form():
    auto.click(contDeets)
    auto.press("tab")
    auto.press('right', presses=2, interval=0.1) #communication type
    auto.press("tab")
    auto.press('right', presses=4, interval=0.1)#call outcome
    auto.press("tab")
    #paste in form
    clip.copy("Registration Contact Plan")
    auto.hotkey("ctrl", "v")
    auto.press("tab")
    #paste in summary
    clip.copy("vm sent; email sent")
    auto.hotkey("ctrl", "v")
    auto.click(x=856, y=856)
    auto.press("home")
    sleep(0.2)

def email(user: str = "Nathaniel"):
    auto.click(x=563, y=402, clicks = 3)
    auto.hotkey("ctrl", "c")
    student = clip.paste()
    auto.click(emailcoord)
    while True:
            if auto.pixel(451, 304) == (255, 255, 255):
                sleep(0.1)
                break
            else:
                sleep(0.5)
    auto.click(x=515, y=315)
    auto.press("tab")
    sleep(0.1)
    auto.press("right")#sender
    sleep(0.1)
    auto.press('tab', presses=5, interval=0.15)
    sleep(0.1)
    clip.copy("Checking In—Let Us Know Your Plans for Next Semester")
    auto.hotkey("ctrl", "v") #subject
    sleep(0.1)
    auto.click(source)
    sleep(0.1)
    auto.press("tab")
    sleep(0.1)
    auto.hotkey("ctrl", "a")
    sleep(0.1)
    clip.copy(compileEmail.select_email("retention", student, user))
    auto.hotkey("ctrl", "v")
    auto.click(source)
    

def process_form():
    open_record()
    sleep(0.2)
    open_sub_form()
    sleep(0.2)
    fillout_form()

def process_email(usr_name):
    email(usr_name)

if __name__ == "__main__":
    sleep(2)
    #open_record() #works
    #open_sub_form() #works
    #fillout_form() #works
    #email() #works
    process_form()