from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import math
from selenium.webdriver.chrome.options import Options



def scroll_tab():
    # driver.execute_script("document.body.style.zoom='100%'")
    # Get the wrapper element
    wrapper = driver.find_element(By.CLASS_NAME, 'wrapper')
    driver.execute_script("arguments[0].style.height = '100%'", wrapper)

    height = driver.execute_script("return document.body.scrollHeight;")
    driver.implicitly_wait(10)
    time.sleep(10)
    #print(height)
    driver.execute_script("document.body.scrollTop = 0;")
    driver.execute_script("document.body.scrollTo(0, 0);")
    driver.execute_script("arguments[0].scrollTop = 0;", wrapper)
    driver.execute_script("arguments[0].scrollTo(0, 0);", wrapper)
    driver.execute_script('document.documentElement.style.overflow = "hidden";')
    driver.execute_script('arguments[0].style.overflow = "hidden";', wrapper)
    # Scroll to the bottom of the wrapper element slowly
    while True:
        # Set the scroll step (the amount by which the wrapper should be scrolled in each iteration)
        # Scroll by 50 pixels
        scroll_position = wrapper.get_attribute('scrollTop')
        driver.execute_script("arguments[0].scrollBy(0, 1);", wrapper)
        # Get the current position of the scrollbar
        time.sleep(0.02)
        # Print the current scroll position
        #print(scroll_position)
        #driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if scroll_position == wrapper.get_attribute('scrollTop'):
            break
        # Pause


def login():
    driver.execute_script("window.scrollTo(0, 0);")
    driver.implicitly_wait(10)

    # Find the username field and enter the username
    username_field = driver.find_element(By.ID, "login-user_name")
    username_field.send_keys("app")

    # Find the password field and enter the password
    password_field = driver.find_element(By.ID, "login-password")
    password_field.send_keys("appc1")
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

# Start the Chrome browser
driver = webdriver.Chrome()

#options = Options()
# Navigate to the website
#driver.get("https://shaym.shinyapps.io/AppCentralData/")
#driver.execute_script("document.body.style.zoom='60%'")
#driver.find_element(By.XPATH, '//a[@class="sidebar-toggle"]').click()
#options.add_argument('window-size=1920x1080')
# Wait a few seconds for the page to load

driver.implicitly_wait(3)
time.sleep(3)
driver.maximize_window()


# Go full screen and zoom ou
driver.execute_script("document.body.style.overflow='hidden'")
driver.execute_script("document.body.requestFullscreen()")


# Find the login button and click on it

# Wait a few seconds for the page to load

tabs = ["CampaignsTrackTab", "VersionsTimelineTab","ISeCPMTab"]

time.sleep(2)
while True:
    for tab in tabs:
        driver.get(f"https://shaym.shinyapps.io/AppCentralData/?tab={tab}")
        login()
        # Click on the element
        driver.find_element(By.XPATH, '//a[@class="sidebar-toggle"]').click()
        scroll_tab()
        time.sleep(5)