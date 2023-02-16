import pyautogui
from time import sleep

dirwork = "C:\\workingnow.txt"#just an exemple

########################################################################
def takeWorkCode():
    pyautogui.press('win')
    pyautogui.write(dirwork)
    pyautogui.press('enter')
    pyautogui.click(1314,511,duration=1)#generic
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','f4')

########################################################################main
takeWorkCode()
