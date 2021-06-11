from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import time
import random

driver = webdriver.Chrome()

driver.get('https://theadvo.com/')
time.sleep(3)

# after page loads gather the buttons to visit influencers
influencer_profiles = driver.find_elements(By.PARTIAL_LINK_TEXT,'Visit')
# of the gathered links, pick a random link to follow
random_profile = influencer_profiles[random.randint(0, len(influencer_profiles)-1)]
# click on the random profile
random_profile.click()

#switch to the next window
new_window = driver.window_handles[1]
driver.switch_to_window(new_window)

time.sleep(3)

WebDriverWait(driver,5).until(EC.url_contains('influencers'))

"""
Below I am using xpath to find both the Follow and Share buttons respectively. There are better ways of doing this other than through
xpath

"""
follow_button = driver.find_element_by_xpath("//span[contains(text(),'Follow')]")

share_button = driver.find_element_by_xpath("//span[contains(text(),'Share')]")


if follow_button.is_displayed() == True:
    print("Follow button appears on the page.")
else :
    print("The follow button does NOT appear on the page.")

if share_button.is_displayed() == True:
    print("Share button appears on the page")
else:
    print("Share button does NOT appear on the page")


