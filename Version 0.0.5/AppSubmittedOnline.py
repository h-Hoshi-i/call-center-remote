import pyautogui as auto
import time as t
import pyperclip as clip

auto.FAILSAFE = True

coordFetch = auto.Point(x=103,y=294)
coordFile = auto.Point(x=996,y=440)
coordLookUpRec = auto.Point(x=676,y=341)
coordDashboard = auto.Point(x=80,y=210)
coordFullName = auto.Point(x=182,y=170)
test = "your mom, works yes"

def get_coord():
    t.sleep(5)
    now = auto.position()
    print(now)
def get_color():
    x, y = auto.position()
    r,g,b = auto.pixel(x, y)
    print(r,g,b)
def get_full_name():
    auto.click(x=33, y=166, clicks=3)
    auto.hotkey('ctrl', 'c')
    fullName = clip.paste()
    return fullName
def get_first_name() -> str:
    FullName = get_full_name()
    firstName = FullName.split(",")[1].split()[0]
    print(firstName)
    return firstName
def open_record_on_input():
    #fetch next
    auto.click(coordFetch[0], coordFetch[1])
    t.sleep(2)

    #check if screen is ready
    while True:
        if auto.pixel(218, 327) == (255, 255, 255):
            break
        else:
            t.sleep(0.5)
    #click record
    auto.click(coordFile[0], coordFile[1])
    t.sleep(0.2)
    #click lookup record
    auto.click(coordLookUpRec[0], coordLookUpRec[1])
    t.sleep(0.3)
    #click dashboard
    auto.click(coordDashboard[0], coordDashboard[1])
    t.sleep(0.2)
def write_email():
    firstName = get_first_name()
    move_to_email()
    auto.press('enter')
    while True: #checks if loaded
        if auto.pixelMatchesColor(729, 289, (232, 241, 246)) or auto.pixelMatchesColor(725, 459, (232, 241, 246)):
            break
        else:
            t.sleep(0.1)
    if auto.pixelMatchesColor(725, 459, (232, 241, 246)):
        #if clicked phone number, close and open email
        auto.press('esc')
        auto.hotkey('shift', 'tab')
        auto.press('enter')#open email
    #change sender and move to subject line
    auto.press(['right', 'tab', 'tab', 'tab', 'tab', 'tab'])
    clip.copy("Southern Adventist University: Application Submitted")
    auto.hotkey('ctrl','v')
    #move to main message box
    auto.press('tab')
    #copy full email as html
    lines = [
            f"Hello {firstName},",
            "",
            "I am contacting you on behalf of Southern Adventist University to follow-up on your recently submitted application and wanted to let you know that we are excited that you are considering Southern! There are a few things we still need to complete your application and you can find them online at southern.edu/apply",
            ""
            "If you have any questions about the application process or about Southern please contact us at 1.800.SOUTHERN or email us at enrollment@southern.edu. Have a blessed day and we look forward to hearing from you!",
            "",
            "Sincerely,",
            "Your Admissions Team",
            "Nathaniel"
            ]

    # Join with newline character
    text = "\n".join(lines)
    clip.copy(text)
    auto.hotkey('ctrl','v')
    #goto previous tab
    auto.hotkey('ctrl', 'shift', 'tab')
def fillout_submitForm():
    t.sleep(0.2) #buffer for tab change
    auto.click(coordFile[0], coordFile[1]) #saftey click
    t.sleep(0.2)
    auto.click(x=652,y=366) #click submit form
    t.sleep(0.3) #may need to add a more consistiant buffer for the form to load
    auto.click(x=734, y=667)#relocate start position for consisitancy
    t.sleep(0.1)
    auto.press('tab', presses=3, interval=0.2)#still eating inputs at 0.1 but i dont like how slow 0.2 is
    t.sleep(0.1)
    auto.press('n')
    t.sleep(0.15)
    auto.press('a')
    t.sleep(0.15)
    # auto.press('right', presses=4, interval=0.15)
    # t.sleep(0.15)
    auto.press('tab')
    t.sleep(0.15)
    auto.press('right', presses=5, interval=0.1)
    t.sleep(0.1)
    auto.press('tab')
    auto.press('tab')
    t.sleep(0.1)
    clip.copy("email sent")
    auto.hotkey('ctrl','v')
    t.sleep(0.1)
    auto.hotkey('ctrl', 'tab')
    t.sleep(0.1)
def process():
    open_record_on_input()
    write_email()
    fillout_submitForm()
    return
def move_to_email():
    auto.click(x=1317, y=236)
    auto.press('tab', presses=2, interval=0.2)

if __name__ == "__main__":
    t.sleep(2)
    #process()
    #------------------Tests-------------------
    get_coord()
    get_color()
    #move_to_email()
    #--------------Single Process--------------
    #write_email() #worked
    #other_email()
    #fillout_submitForm() #worked