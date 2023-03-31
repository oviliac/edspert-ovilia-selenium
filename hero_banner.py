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

from data import HeroData
from locator import Homepage, Navbar, Hero

class TestHero(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        # options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_TC13_TC14_page_title(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Hero.title)
        self.assertTrue(title.is_displayed())
        self.assertEqual(title.text, HeroData.title)
        subtitle = driver.find_element(By.CSS_SELECTOR, Hero.subtitle)
        self.assertTrue(subtitle.is_displayed())
        self.assertEqual(subtitle.text, HeroData.subtitle)

    def test_TC16_jelajahi_kelas(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)
        title = driver.find_element(By.CSS_SELECTOR, Hero.jelajahi_kelas_button).click()
        self.assertEqual(driver.current_url, Homepage.all_class_url)
    

if __name__ == "__main__":
    unittest.main()