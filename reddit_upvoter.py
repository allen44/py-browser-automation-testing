from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from sys import argv

#Add your own reddit credentials
try:
    reddit_username = argv[1]
    reddit_password = argv[2]
except:
    reddit_username = input('Reddit username: ')
    reddit_password = input('Reddit password: ')


options = Options()
# options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--incognito")

chrome_browser = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome_browser.maximize_window()
chrome_browser.get('https://www.reddit.com/login/')

# #First login in to reddit before we are allowed to upvote
# login_button = chrome_browser.find_element(By.LINK_TEXT, 'Log in')

#Enter username
username_field = chrome_browser.find_element(By.ID, 'loginUsername')
username_field.clear()
username_field.send_keys(reddit_username)

#Enter password
password_field = chrome_browser.find_element(By.ID, 'loginPassword')
password_field.clear()
password_field.send_keys(reddit_password)

#Click Log In button
login_button = chrome_browser.find_element(By.CLASS_NAME, 'AnimatedForm__submitButton')
login_button.click()

# try:
print('starting to wait up to 10 seconds')
element = WebDriverWait(chrome_browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "icon-upvote"))
)
print('ending wait')

#We identify the upvote buttons by the intersection fo two CSS selectors
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 


css_selector1= chrome_browser.find_elements(By.CSS_SELECTOR, "button[aria-label='upvote']")
css_selector2 = chrome_browser.find_elements(By.CSS_SELECTOR, 'button[aria-pressed="false"]')
upvote_buttons = intersection(css_selector1, css_selector2)

wait_counter = 5
for upvote_button in upvote_buttons:
    print("upvoting")
    # upvote_button.click()
    hover = ActionChains(chrome_browser).move_to_element(upvote_button)
    hover.perform()
    upvote_button.click()
    chrome_browser.implicitly_wait(wait_counter)
    print(f'waiting {wait_counter} seconds until next upvote')
    wait_counter=+ wait_counter
# except:
    # chrome_browser.quit()
    # print('quit early')

print('script complete')