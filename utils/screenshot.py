import os
import json
from typing import List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import shutil


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptInsecureCerts'] = True

    # Open the web page
    driver = webdriver.Chrome(options=chrome_options,
                              desired_capabilities=capabilities)

    return driver


def take_element_screenshot(url, css_selector):
    driver = get_driver()
    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, css_selector)

    
    element.screenshot(f"screenshots/{css_selector}.png")

    driver.quit()


# take_element_screenshot("http://localhost:4200/", "button", "dump/test.png")

def take_batch_screenshot(url):

    if os.path.exists("screenshots"):
        shutil.rmtree("screenshots")
    os.makedirs("screenshots")

    file_path = "dump/changes.json"
    with open(file_path, 'r') as f:
        data = json.load(f)

    data = data['color_contrast']
    res = []
    for d in data:
        temp = data[d]
        if len(temp) > 0:
            res.extend(temp)

    for elm in res:
        print(elm['selector'])
        if elm['selector'] not in [".main", ".form h2"]:
            selector = elm['selector']
            take_element_screenshot(url, selector)


# take_batch_screenshot("http://localhost:4200/")
