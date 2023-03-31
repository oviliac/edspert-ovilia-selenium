import time
import pytest
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from data import HeroData, Section2Data
from locator import Homepage, Navbar, Hero, Section2

class TestSection2(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        # options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_TC23_section_visibility(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section2.title)
        actions = ActionChains(driver)
        actions.move_to_element(title).perform()
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, Section2Data.title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Section2.subtitle)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, Section2Data.subtitle)

    def test_TC24_section_cards(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section2.title)

        actions = ActionChains(driver)
        actions.move_to_element(title).perform()

        items = driver.find_elements(By.CSS_SELECTOR, Section2.card_item)
        self.assertEqual(len(items), 3)

    def test_TC25_card_1(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section2.card_1_title)
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, Section2Data.card_1_title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Section2.card_1_desc)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, Section2Data.card_1_desc)

    def test_TC26_card_2(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section2.card_2_title)
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, Section2Data.card_2_title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Section2.card_2_desc)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, Section2Data.card_2_desc)

    def test_TC26_card_3(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section2.card_3_title)
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, Section2Data.card_3_title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Section2.card_3_desc)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, Section2Data.card_3_desc)

    

if __name__ == "__main__":
    unittest.main()