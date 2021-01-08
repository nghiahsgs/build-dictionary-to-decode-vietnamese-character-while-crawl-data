import pyautogui
import time

def ham_copy_all_interface_web():
  width, height = pyautogui.size()

  for i in range(20):
    pyautogui.click(width//2, height//2)
    pyautogui.keyDown('pgdn')
    pyautogui.keyUp('pgdn')
    time.sleep(1)

  pyautogui.click(width//2, height//2)
  pyautogui.keyDown('ctrl')
  pyautogui.keyDown('end')
  pyautogui.keyUp('ctrl')
  pyautogui.keyUp('end')
  time.sleep(1)

  pyautogui.keyDown('ctrl')
  pyautogui.keyDown('a')
  pyautogui.keyUp('ctrl')
  pyautogui.keyUp('a')

  pyautogui.keyDown('ctrl')
  pyautogui.keyDown('c')
  pyautogui.keyUp('ctrl')
  pyautogui.keyUp('c')

def ham_paste_all_interface_web():
  width, height = pyautogui.size()
  pyautogui.click(width//2, height//2)
  time.sleep(1)
  pyautogui.click(width//2, height//2)

  pyautogui.keyDown('ctrl')
  pyautogui.keyDown('v')
  pyautogui.keyUp('ctrl')
  pyautogui.keyUp('v')
  time.sleep(1)