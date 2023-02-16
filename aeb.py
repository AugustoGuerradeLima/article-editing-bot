import pyautogui
from time import sleep

-----------------------------------------------------------------------------------#PARTONE
#load text
pyautogui.click(1314,511,duration=2)
pyautogui.doubleClick(398,263,duration=2)

#prepare the source code of the article
pyautogui.click(184,5,duration=2)
pyautogui.click(555,342,duration=2)
pyautogui.click(1062,413,duration=2)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
pyautogui.press('esc')
pyautogui.click(13,52,duration=2)
pyautogui.click(137,214,duration=2)
pyautogui.click(1062,413,duration=2)
pyautogui.hotkey('ctrl','v')
pyautogui.click(1191,874,duration=2)
