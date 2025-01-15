import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
import time

SBR_WEBDRIVER = f'https://brd-customer-hl_25bb6466-zone-ai_scrapper:jr6f1crk0ztv@brd.superproxy.io:9515'

def scrape_website(website):
    print("Launching chrome browser...")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')

    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print("Connected! Navigating to {website}")
        driver.get(website)
        #CAPTCHA handling
        print("Waiting Captcha to solve...")
        solve_res = driver.execute('executeCdpCommand', {
            'cmd': 'Captcha.waitForSolve',
            'params': {'detectTimeout': 10000},
        })
        print('Captcha solve status:', solve_res['value']['status'])
        #print("Taking page screenshot to file page.png")
        #driver.get_screenshot_as_file('./page.png')
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html