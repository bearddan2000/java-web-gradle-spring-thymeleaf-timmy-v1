from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging, time

logging.basicConfig(level=logging.INFO)

SERVICE_URL = "http://java-srv:8080"

def download(driver, link):
    driver.get(f'{SERVICE_URL}/{link}')
    driver.implicitly_wait(180)
    l = driver.find_element(By.ID, "print-button")
    ActionChains(driver).click(l).perform()
    time.sleep(2.5)

def get_links():
    return [ 'current', 'historical']

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--normal")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    prefs = {
        "plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}],
        "download.prompt_for_download": False,
        "download.open_pdf_in_system_reader": False,
        "profile.default_content_settings.popups": 0,
        'download.directory_upgrade': True,
        "download.extensions_to_open": "applications/pdf",
        "download.default_directory" : "/home/developer/Downloads"
    }
    options.experimental_options["prefs"] = prefs
    driver = webdriver.Chrome(options=options)
    results = get_links()
    for i in results:
        download(driver, i)

    driver.quit()
    
if __name__ == '__main__':
    main()