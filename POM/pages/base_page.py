from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_current_url(self):
        url = self.driver.current_url
        return url

    def go_to(self, url):
        self.driver.get(url)
    
    def back_to_previous_page(self):
        self.driver.back()
    
    def get_current_title(self):
        return self.driver.title
    
    def click_on(self, locator):
        self.wait.until(EC.presence_of_element_located(locator)).click()
