#Mouse & keyboard automation
import pyautogui
import time
print(pyautogui.size())
##pyautogui.moveTo(400,100,duration=1)
##pyautogui.moveRel(0,50,duration=3)
##print(pyautogui.position())
##pyautogui.click(70,50)
##pyautogui.scroll(-100)
##pyautogui.typewrite("subscribe to this channel")
##pyautogui.hotkey('ctrlleft','a')
pyautogui.moveTo(150,1079)
time.sleep(2)
time.sleep(1)
pyautogui.click()
pyautogui.write("notepad")
pyautogui.moveTo(230,350,duration=2)
pyautogui.doubleClick()
time.sleep(2)
pyautogui.write("Welcome to coding")
time.sleep(2)
pyautogui.hotkey("ctrl","a")
time.sleep(2)
pyautogui.hotkey("ctrl","x")
time.sleep(2)
pyautogui.moveTo(400,400,duration=3)
time.sleep(1)
pyautogui.hotkey("ctrl","v")
pyautogui.press('enter')
pyautogui.typewrite(" Hello")
pyautogui.PAUSE=2.5
pyautogui.alert('Do you want to continue')
pyautogui.confirm('Do you want to continue')
pyautogui.prompt('Enter your age.')
print("Desktop automation")
print("Task completed")

#pyautogui.screenshot('')  #returns a Pillow/PIL Image object, and saves it to a file




#alert(text='Confirm',title='Notepad',buttons=['OK','Cancel'])




