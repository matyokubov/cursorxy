import pyautogui
import time
import os

try:
    while True:
        # Get the current mouse position
        x, y = pyautogui.position()
        
        # Clear the terminal output
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Print the current mouse coordinates
        print(f"Mouse Position: X = {x}, Y = {y}")
        
        # Delay to prevent excessive CPU usage
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated.")
