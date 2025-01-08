# Take a screenshot of the entire screen
import os
import random
from turtle import screensize
import pytest
from pywinauto import Application
from pywinauto import timings
from PIL import ImageGrab
import uuid

def test_windows_application():
    ## To open calculator from windows machine
    app = Application(backend="win32").start("C:\\Windows\\System32\\calc.exe")
    ##To wait for 15 seconds
    app.wait_cpu_usage_lower(threshold=15)
    ## to generate a random number
    file_name = f"screenshot_{uuid.uuid4()}.png"
    ## to take a screenshot
    screenshot = ImageGrab.grab()
    #To save the file with random name
    screenshot.save(file_name)
    screenshot.show()
    #To close the screenshot
    screenshot.close()
    #To close the application
    app.kill()


    