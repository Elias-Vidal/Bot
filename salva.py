from selenium import webdriver
import time
import os
from selenium.webdriver.chrome.options import Options


dir_path = os.getcwd()
chrome_options2 = Options()
chrome_options2.add_argument(r "user-data-dir"+ dir_path +"profile/whatsapp")
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
time.sleep(120)