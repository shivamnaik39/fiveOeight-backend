from lib2to3.pgen2 import driver

from optparse import Option

from webbrowser import Chrome

from selenium import webdriver

from selenium.webdriver.common.by import By

import json


with open('D:/data.json', 'r') as f:

    data = json.load(f)


def alert():

    options = webdriver.ChromeOptions()

    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)

    driver.get("http://localhost:4200/login-page")

    driver.save_screenshot("screen.png")

    for selector_data in data['color_contrast']['angular-demo\\src\\app\\app.component.css']:

        selector = selector_data['selector']

    # print(f"Selector: {selector}")

        element = driver.find_element(By.CSS_SELECTOR, selector)

        element.screenshot(selector+"-" + "element.png")


alert()
