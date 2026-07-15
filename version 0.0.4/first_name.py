import easyocr
import pyautogui
import numpy as np

def first_name_grabber(bounds: tuple = (106, 142, 250, 207)) -> str:
    """Grabs the first name off of the record on a slate dashboard profile.
    defaults to the coordinates for Brave Browser.
    """
    #Take screenshot (returns a PIL Image)
    img = pyautogui.screenshot(region=bounds)
    #Convert PIL Image to NumPy array
    img_array = np.array(img)
    #Initialize Reader
    reader = easyocr.Reader(['en'], gpu=False)
    #Pass the numpy array to EasyOCR
    results = reader.readtext(img_array)
    #cuts the exess, than grabs just the first name using spaces.
    texts = [text for bbox, text, confidence in results][2].split()[1]
    print(texts)
    return texts