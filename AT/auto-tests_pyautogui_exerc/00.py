import pyautogui
import time
# from time import sleep

pyautogui.hotkey('win', 'r') #открывем cmd

pyautogui.typewrite('C:\\Users\\user\AppData\Local\Programs\AISMK\AISMK.exe') #пишем в окне путь к приложению
pyautogui.press('enter') #нажимаем enter
time.sleep(5) #ждем 5сек
#pyautogui.hotkey('alt', 'f4') #закрываем приложение
