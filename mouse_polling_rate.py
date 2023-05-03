# This script uses the pyautogui and polling modules
# You can install them with pip install pyautogui and pip install polling
# This script is intended for educational purposes only and may not work as expected

import pyautogui
import polling
import time

# Define a function to get the current mouse position
def get_mouse_pos():
    return pyautogui.position()

# Define a function to calculate the mouse movement speed in pixels per second
def get_mouse_speed():
    # Get the initial mouse position and time
    x1, y1 = get_mouse_pos()
    t1 = time.time()
    # Wait for 0.01 seconds
    time.sleep(0.01)
    # Get the final mouse position and time
    x2, y2 = get_mouse_pos()
    t2 = time.time()
    # Calculate the distance and time difference
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    dt = t2 - t1
    # Calculate the speed in pixels per second
    speed = dist / dt
    return speed

# Define a function to estimate the mouse polling rate in hertz
def get_mouse_polling_rate():
    # Poll the mouse speed function until it returns a value greater than 0
    # This means the mouse is moving
    speed = polling.poll(get_mouse_speed, check_success=lambda x: x > 0, step=0.01, timeout=10)
    # Get the current mouse position and time
    x1, y1 = get_mouse_pos()
    t1 = time.time()
    # Poll the mouse position function until it returns a different value than the initial one
    # This means the mouse position has changed
    x2, y2 = polling.poll(get_mouse_pos, check_success=lambda x: x != (x1, y1), step=0.01, timeout=10)
    # Get the final time
    t2 = time.time()
    # Calculate the time difference in seconds
    dt = t2 - t1
    # Estimate the polling rate in hertz by taking the inverse of the time difference
    rate = 1 / dt
    return rate

# Print the estimated mouse polling rate
print(f"Your mouse polling rate is {get_mouse_polling_rate():.0f} Hz")
