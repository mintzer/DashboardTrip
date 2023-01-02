from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def scroll_tab():
    # driver.execute_script("document.body.style.zoom='100%'")
    # Get the wrapper element
    wrapper = driver.find_element_by_css_selector('.wrapper')
    driver.execute_script("arguments[0].style.height = '100%'", wrapper)

    height = driver.execute_script("return document.body.scrollHeight;")
    #print(height)
    driver.execute_script("arguments[0].scrollTop = 0;", wrapper)
    # Scroll to the bottom of the wrapper element slowly
    for i in range(int(height / 10.0)):
        # Set the scroll step (the amount by which the wrapper should be scrolled in each iteration)
        # Scroll by 50 pixels
        driver.execute_script("arguments[0].scrollBy(0, 50);", wrapper)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Pause
        time.sleep(0.5)

# Start the Chrome browser
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://shaym.shinyapps.io/AppCentralData/")

# Wait a few seconds for the page to load
driver.implicitly_wait(10)

# Find the username field and enter the username
username_field = driver.find_element(By.ID, "login-user_name")
username_field.send_keys("app")

# Find the password field and enter the password
password_field = driver.find_element(By.ID, "login-password")
password_field.send_keys("appc1")

#driver.maximize_window()

# Go full screen and zoom out
#driver.execute_script("document.body.style.zoom='50%'")
driver.execute_script("document.body.style.overflow='hidden'")
driver.execute_script("document.body.requestFullscreen()")

# Find the login button and click on it
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

# Wait a few seconds for the page to load
driver.implicitly_wait(3)

# Click on the element
driver.find_element(By.XPATH, '//*[@id="sidebarItemExpanded"]/ul/li[4]/ul/li[7]/a').click()
#driver.find_element(By.XPATH, '//a[@class="sidebar-toggle"]').click()
scroll_tab()
time.sleep(5)

#driver.find_element(By.XPATH, '//a[@class="sidebar-toggle"]').click()
time.sleep(2)
# Click on the element
driver.find_element(By.XPATH, '//a[@href="#shiny-tab-VersionsTimelineTab" and @data-toggle="tab"]').click()
#driver.find_element(By.XPATH, '//a[@class="sidebar-toggle"]').click()
scroll_tab()
time.sleep(5)