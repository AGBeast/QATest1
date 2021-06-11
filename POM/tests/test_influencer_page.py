import unittest
import sys
import time
from selenium import webdriver

# sys.path.append(<path/to/the/project>)

from POM.pages.home_page import HomePage


class InfluencerPageTest(unittest.TestCase):
    def setUp(self):
        # basic set up for the test
        self.driver = webdriver.Chrome()
        self.driver.set_script_timeout(5)
        self.page = HomePage(self.driver)
        
    
    def test_can_visit_influencer_site(self):
        self.page.visit_page()
        self.assertEqual('https://theadvo.com/', self.page.get_current_url()) #confirming that we are on the right page
        link = self.page.get_random_influencer_link()
        link.click()
        time.sleep(4)
        self.page.switch_context()
        # making assertions regarding the follow and share buttons 
        self.assertTrue(self.page.follow_button_appears())
        self.assertTrue(self.page.share_button_appears())



    def tearDown(self):
        self.driver.close()











if __name__ == "__main__":
    unittest.main()