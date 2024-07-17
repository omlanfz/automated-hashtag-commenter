import cv2
import numpy as np
import pyautogui
import pyperclip
import keyboard
import time
# Function to locate an image on the screen
def locate_image_on_screen(image_path, confidence=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY), template_gray, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= confidence)
    if len(loc[0]) > 0:
        return loc[1][0], loc[0][0]
    else:
        return None

# Function to comment on a post
def comment_on_post():
    button_location = locate_image_on_screen('comment_button.png', confidence=0.9)
    if button_location:
        x, y = button_location
        pyautogui.moveTo(x, y)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.typewrite('We want justice!')
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        pyautogui.typewrite('#SaveBangladeshiStudents')
        # time.sleep(0.1)
        # Copy the emoji to the clipboard
        pyperclip.copy('✅')
        # Paste the emoji
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(0.1)
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        pyautogui.typewrite('#ALjazerra #Bbcnews #CNN #TheWashingtonPost')
        # time.sleep(0.1)
        # Copy the emoji to the clipboard
        pyperclip.copy('✅')
        # Paste the emoji
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(0.1)
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        pyautogui.typewrite('#TheNewYorkTimes #TheGuardian')
        # time.sleep(0.1)
        # Copy the emoji to the clipboard
        pyperclip.copy('✅')
        # Paste the emoji
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(0.1)
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        pyautogui.typewrite('#BBC #AlJazeeraEnglish #TheWallStreetJournal')
        # time.sleep(0.1)
        # Copy the emoji to the clipboard
        pyperclip.copy('✅')
        # Paste the emoji
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(0.1)
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        pyautogui.typewrite('#CNBC #UnitedNations #TheGuardian #NewYorkTimesOpinion')
        # time.sleep(0.1)
        # Copy the emoji to the clipboard
        pyperclip.copy('✅')
        # Paste the emoji
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(0.1)
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        pyautogui.typewrite('#ABCNews #NewYorkPost #ProjectNightfall')
        # time.sleep(0.1)
        # Copy the emoji to the clipboard
        pyperclip.copy('✅')
        # Paste the emoji
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(0.1)
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        pyautogui.typewrite('#DUUnderAttack #JUUnderAttack #NoQuot #QuotaReformProtest')
        # time.sleep(0.1)
        # Copy the emoji to the clipboard
        pyperclip.copy('✅')
        # Paste the emoji
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(0.1)
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        pyautogui.typewrite('#DhakaUniversityUnderAttack #QuotaReformMovement #ProtectStudents')
        # time.sleep(0.1)
        # Copy the emoji to the clipboard
        pyperclip.copy('✅')
        # Paste the emoji
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(0.1)
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')

        pyautogui.typewrite('#savebangladeshalluniversitystudents')
        # time.sleep(0.1)
        # Copy the emoji to the clipboard
        pyperclip.copy('✅')
        # Paste the emoji
        pyautogui.hotkey('ctrl', 'v')
        # time.sleep(0.1)
        # Press Shift+Enter
        pyautogui.keyDown('shift')
        pyautogui.press('enter')
        pyautogui.keyUp('shift')
        time.sleep(1)
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('esc')
        pyautogui.press('esc')
    else:
        print("Comment button image not found on screen.")

time.sleep(3)
while True:
    if keyboard.is_pressed('r'):
        print("Script stopped by user.")
        break
    # for i in range(1, 11):
    #     pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('pagedown')
    time.sleep(1)
    comment_on_post()
    time.sleep(1)
