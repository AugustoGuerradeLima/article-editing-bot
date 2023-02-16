import pyautogui
from time import sleep

dirname = "C:\\Users\\Augus\\Desktop\\psi\\sourcecode.txt"

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
