from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging, time

logging.basicConfig(level=logging.INFO)

SERVICE_URL = "http://localhost"

def download(driver, link):
    driver.get(f'{SERVICE_URL}/{link}')
    driver.implicitly_wait(180)
    l = driver.find_element(By.ID, "print-button")
    ActionChains(driver).click(l).perform()
    time.sleep(2.5)

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--normal")
    # options.add_argument('--headless')  # example
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    # options.add_argument("--auto-open-devtools-for-tabs")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")
    # options.add_argument("--window-size=2000x2000")
    options.add_argument('--disable-dev-shm-usage')
    prefs = {
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
        "download.prompt_for_download": False,
        # "plugins.always_open_pdf_externally": True,
        "download.open_pdf_in_system_reader": False,
        "profile.default_content_settings.popups": 0,
        'download.directory_upgrade': True,
        "download.extensions_to_open": "applications/pdf",
        "download.default_directory" : "/home/oem/git/new-05-30/c/timmy-project/merge-pdf"
    }
    # options.add_experimental_option("prefs",prefs)
    options.experimental_options["prefs"] = prefs
    driver = webdriver.Chrome(options=options)
    results = [
        'current', 'historical', 'datatable',
        'stats/current', 'stats/prev', 'stats/ytd',
        'stats/trends/current', 'stats/trends/prev', 'stats/trends/ytd',
        'graph/scatter/current', 'graph/scatter/prev', 'graph/scatter/ytd',
        'graph/line/current', 'graph/line/prev', 'graph/line/ytd',
        'graph/bar/current', 'graph/bar/prev', 'graph/bar/ytd',
        'graph/hbar/current', 'graph/hbar/prev', 'graph/hbar/ytd',
        'graph/linear/current', 'graph/linear/prev', 'graph/linear/ytd',
        'graph/expo/current', 'graph/expo/prev', 'graph/expo/ytd',
        'graph/log/current', 'graph/log/prev', 'graph/log/ytd',
        'graph/current/basic', 'graph/ytd/frequency',
    ]
    for i in results:
        download(driver, i)

    driver.quit()
    
if __name__ == '__main__':
    main()