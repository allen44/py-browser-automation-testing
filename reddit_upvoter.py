from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from sys import argv

#Add your own reddit credentials
assert argv[1]
assert argv[2]
reddit_username = argv[1]
reddit_password = argv[2]

options = Options()
# options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")

chrome_browser = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

 # Check to see if the "Show Message" buttonexists on page
assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I am cool!')

user_button2 = chrome_browser.find_element(By.CSS_SELECTOR, '#get-input > .btn')
print(user_button2)

show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')
assert 'I am cool!' in output_message.text

chrome_browser.find_element(By.ID, 'display')

chrome_browser.get('reddit')
chrome_browser.quit()

print('script complete')