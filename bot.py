import pyautogui
from time import sleep

dirname = "C:\\sourcecode.txt"#just an exemple

########################################################################1
def takeSourceCode():
    pyautogui.press('win')
    pyautogui.write(dirname)
    pyautogui.press('enter')
    pyautogui.click(1314,511,duration=1)#generic
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('ctrl','c')
    pyautogui.hotkey('alt','f4')

########################################################################main
takeSourceCode()
