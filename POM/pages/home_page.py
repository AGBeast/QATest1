from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from POM.pages.base_page import BasePage

import random


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = 'https://theadvo.com/'


    def visit_page(self):
        self.driver.get(self.url)

    def get_random_influencer_link(self):
        influencer_profiles = self.driver.find_elements(By.PARTIAL_LINK_TEXT,'Visit')
        random_profile = influencer_profiles[random.randint(0, len(influencer_profiles)-1)]
        return random_profile

    def switch_context(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window)
        WebDriverWait(self.driver,5).until(EC.url_contains('influencers'))

    def follow_button_appears(self):
        follow_button = self.driver.find_element_by_xpath("//span[contains(text(),'Follow')]")
        return follow_button.is_displayed()
    
    def share_button_appears(self):
        share_button = self.driver.find_element_by_xpath("//span[contains(text(),'Share')]")
        return share_button.is_displayed()




    





