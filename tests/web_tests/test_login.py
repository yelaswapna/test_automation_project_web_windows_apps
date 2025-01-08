from csv import writer
from turtle import screensize
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import ImageGrab
import os
import logging
from PIL import Image
import uuid
import pytest

def test_web_application():
    logging.basicConfig(level=logging.INFO)
    logging.info("Opening the browser...")
    # Automatically downloads and installs the correct ChromeDriver version

    # Path to your ChromeDriver
    service = Service(r"C:\Swapna\Tech\chromedriver_win32\chromedriver.exe")

    # # Initialize the WebDriver
    #driver = webdriver.Chrome(executable_path="C://Program Files//Google//Chrome//Application//chrome.exe")
    driver = webdriver.Chrome(service=service)
    url = "https://www.geeksforgeeks.org/"
    
    # Opening the website
    driver.get(url)

    #Generate random name for the file
    file_name = f"screenshot_{uuid.uuid4()}.png"
        
    driver.save_screenshot(file_name)
    
    # Loading the image
    image = Image.open(file_name)
    
    # Showing the image
    image.show()   

    # Closing the image
    image.close()

    # Close the browser
    driver.quit()
    

def test_web_application_title():
    
    # Path to your ChromeDriver
    service = Service(r"C:\Swapna\Tech\chromedriver_win32\chromedriver.exe")

    # # Initialize the WebDriver
    #driver = webdriver.Chrome(executable_path="C://Program Files//Google//Chrome//Application//chrome.exe")
    driver = webdriver.Chrome(service=service)

    url = "https://www.geeksforgeeks.org/"
    
    # Opening the website
    driver.get(url)

    # Test case to check the title of the web page
    expected_title = "GeeksforGeeks | A computer science portal for geeks"
    actual_title = driver.title

    try:
        assert actual_title == expected_title
        logging.info("Title matches expected title.")
    except AssertionError:
        logging.error(f"Title does not match. Expected: {expected_title}, but got: {actual_title}")
        raise AssertionError(f"Title does not match. Expected: {expected_title}, but got: {actual_title}")

    # Close the browser
    driver.quit()
    