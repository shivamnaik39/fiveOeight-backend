from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from axe_selenium_python import Axe
import json
import os
from typing import Dict, List, Any


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    capabilities = DesiredCapabilities.CHROME.copy()
    capabilities['acceptInsecureCerts'] = True

    # Open the web page
    driver = webdriver.Chrome(options=chrome_options)

    return driver


def get_issues(url: str):
    # Set up Selenium to run the Chrome browser
    driver = get_driver()

    driver.get(url)

    # Run an accessibility check using the Axe engine and filter the results
    axe = Axe(driver)
    axe.inject()
    results = axe.run()

    if not os.path.exists("dump"):
        os.makedirs("dump")

    # Write violations to a JSON file
    with open("dump/issues.json", "w") as file:
        file.write(json.dumps(results["violations"], indent=2))

    # # Take screenshots of the violations and save them to a directory
    # if results["violations"]:
    #     if not os.path.exists("dump/screenshots"):
    #         os.makedirs("dump/screenshots")

    #     for i, violation in enumerate(results["violations"]):
    #         screenshot_path = os.path.join("dump/screenshots", f"{i}.png")
    #         driver.save_screenshot(screenshot_path)

    # Filter the violations of the website
    relevant_violations = filter_violations(results["violations"])

    # Quit the browser
    driver.quit()

    return relevant_violations


def filter_violations(violations):

    relevant_violations = [
        v for v in violations if v["impact"] in ["serious", "critical"]]

    return relevant_violations

# get_issues("http://127.0.0.1:5500/test.html")


def take_screenshots(violations: List[Dict[str, Any]]):
    if not os.path.exists("dump/screenshots"):
        os.makedirs("dump/screenshots")

    # Set up Selenium to run the Chrome browser
    driver = get_driver()

    for i, violation in enumerate(violations):
        # Navigate to the page and the element of the violation
        driver.get(violation["url"])
        target = driver.find_element_by_css_selector(violation["selector"])

        # Take a screenshot of the element and save it to a file
        screenshot_path = os.path.join("dump/screenshots", f"{i}.png")
        target.screenshot(screenshot_path)

    # Quit the browser
    driver.quit()
