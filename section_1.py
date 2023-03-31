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

from data import HeroData, Section1Data
from locator import Homepage, Navbar, Hero, Section1

class TestSection1(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        # options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_TC17_section_visibility(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section1.title)
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, Section1Data.title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Section1.subtitle)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, Section1Data.subtitle)

    def test_TC18_section_cards(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        items = driver.find_elements(By.CSS_SELECTOR, Section1.card_item)
        self.assertEqual(len(items), 4)

    def test_TC19_card_1(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section1.card_1_title)
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, Section1Data.card_1_title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Section1.card_1_subtitle)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, Section1Data.card_1_subtitle)

    def test_TC20_card_2(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section1.card_2_title)
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, Section1Data.card_2_title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Section1.card_2_subtitle)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, Section1Data.card_2_subtitle)

    def test_TC21_card_3(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section1.card_3_title)
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, Section1Data.card_3_title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Section1.card_3_subtitle)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, Section1Data.card_3_subtitle)

    def test_TC22_card_4(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Section1.card_4_title)
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, Section1Data.card_4_title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Section1.card_4_subtitle)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, Section1Data.card_4_subtitle)

    

if __name__ == "__main__":
    unittest.main()