import pyautogui
import cv2
import numpy as np
import time

# Path to the image of the element to detect
target_image_path = "target.png"


def monitor_screen():
    while True:
        # Capture the screen
        screenshot = pyautogui.screenshot()

        # Load the target image
        target = cv2.imread(target_image_path, cv2.IMREAD_UNCHANGED)

        # Making sure both images have the same format
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
        target_gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
        
        # Match the target element
        result = cv2.matchTemplate(screenshot, target_gray, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)

        if max_val > 0.8:
            print("Element detected! Performing action...")
            perform_action_x()

        time.sleep(1)

def perform_action_x():
    print("...Performing Action X...")

monitor_screen()