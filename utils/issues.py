from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from axe_selenium_python import Axe
import json, os


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

    # write to a json file
    with open("dump/issues.json", "w") as file:
        file.write(json.dumps(results["violations"], indent=2))

    # return the violations of the website
    # return results["violations"]
    # dummy = [{"name": "shivam", "age": 23} for i in range(10000)]
    violations = results["violations"]
    relevant_violations = filter_violations(violations)
    return relevant_violations


def filter_violations(violations):

    relevant_violations = [
        v for v in violations if v["impact"] in ["serious", "critical"]]

    return relevant_violations

# get_issues("http://127.0.0.1:5500/test.html")