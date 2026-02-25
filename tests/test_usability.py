# Epic Title: Test Portal Usability on Various Screen Sizes

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PortalUsabilityTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_usability_desktop(self):
        self.driver.set_window_size(1920, 1080)
        self.driver.get("http://localhost:5000")
        time.sleep(2)
        self.assertIn("Welcome to the Responsive Portal", self.driver.page_source)
        # Additional checks for desktop usability
        self.check_elements()

    def test_usability_tablet(self):
        self.driver.set_window_size(768, 1024)
        self.driver.get("http://localhost:5000")
        time.sleep(2)
        self.assertIn("Welcome to the Responsive Portal", self.driver.page_source)
        # Additional checks for tablet usability
        self.check_elements()

    def test_usability_mobile(self):
        self.driver.set_window_size(375, 667)
        self.driver.get("http://localhost:5000")
        time.sleep(2)
        self.assertIn("Welcome to the Responsive Portal", self.driver.page_source)
        # Additional checks for mobile usability
        self.check_elements()

    def check_elements(self):
        # Check if all necessary elements are present and functional
        header = self.driver.find_element_by_tag_name("header")
        self.assertIsNotNone(header)
        footer = self.driver.find_element_by_tag_name("footer")
        self.assertIsNotNone(footer)
        main_content = self.driver.find_element_by_tag_name("main")
        self.assertIsNotNone(main_content)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()