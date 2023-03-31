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

# from data import DataLogin, DataLoginInvalid
from locator import Homepage, Navbar, Hero

class TestNavbar(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions() 
        # options.add_argument("--headless")
        self.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def test_TC01_open_page(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        self.assertEqual(driver.current_url, Homepage.base_url)

    
    def test_TC02_click_logo(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.logo).click()
        self.assertEqual(driver.current_url, Homepage.base_url)

    
    def test_TC03_open_menu_program(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.menu_program).click()
        menu_items = driver.find_element(By.CSS_SELECTOR, Navbar.menu_program_items)
        self.assertTrue(menu_items.is_displayed())
        time.sleep(1)

    
    def test_TC04_open_menu_program_webinar(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.menu_program).click()
        menu_items = driver.find_element(By.CSS_SELECTOR, Navbar.menu_program_items)
        self.assertTrue(menu_items.is_displayed())
        webinar = driver.find_element(By.CSS_SELECTOR, Navbar.program_webinar)
        webinar.click()
        self.assertFalse(menu_items.is_displayed())
        time.sleep(1)

    def test_TC05_open_menu_program_bootcamp(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.menu_program).click()
        menu_items = driver.find_element(By.CSS_SELECTOR, Navbar.menu_program_items)
        self.assertTrue(menu_items.is_displayed())
        webinar = driver.find_element(By.CSS_SELECTOR, Navbar.program_bootcamp)
        webinar.click()
        self.assertFalse(menu_items.is_displayed())
        time.sleep(1)

    def test_TC06_open_menu_program_online_course(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.menu_program).click()
        menu_items = driver.find_element(By.CSS_SELECTOR, Navbar.menu_program_items)
        self.assertTrue(menu_items.is_displayed())
        webinar = driver.find_element(By.CSS_SELECTOR, Navbar.program_online_course)
        webinar.click()
        self.assertFalse(menu_items.is_displayed())
        time.sleep(1)

    def test_TC07_open_bidang_ilmu(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.menu_bidang_ilmu).click()
        menu_items = driver.find_element(By.CSS_SELECTOR, Navbar.menu_bidang_ilmu_items)
        self.assertTrue(menu_items.is_displayed())
        time.sleep(1)

    def test_TC08_open_program_tech_development(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.menu_bidang_ilmu).click()
        menu_items = driver.find_element(By.CSS_SELECTOR, Navbar.menu_bidang_ilmu_items)
        self.assertTrue(menu_items.is_displayed())
        webinar = driver.find_element(By.CSS_SELECTOR, Navbar.program_tech_development)
        webinar.click()
        self.assertFalse(menu_items.is_displayed())
        time.sleep(1)
    
    def test_TC09_open_program_data(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.menu_bidang_ilmu).click()
        menu_items = driver.find_element(By.CSS_SELECTOR, Navbar.menu_bidang_ilmu_items)
        self.assertTrue(menu_items.is_displayed())
        webinar = driver.find_element(By.CSS_SELECTOR, Navbar.program_data)
        webinar.click()
        self.assertFalse(menu_items.is_displayed())
        time.sleep(1)

    def test_TC10_open_bidang_ilmu(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.menu_tentang).click()
        self.assertEqual(driver.current_url, Homepage.tentang_url)
        time.sleep(1)

    def test_TC11_open_login(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.login_button).click()
        modal = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, Navbar.login_modal)))
        self.assertTrue(modal)
        time.sleep(1)

    def test_TC12_login_using_google(self):
        driver = self.browser
        driver.get(Homepage.base_url)
        driver.find_element(By.CSS_SELECTOR, Navbar.login_button).click()
        modal = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, Navbar.login_modal)))
        self.assertTrue(modal)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, Navbar.login_link))).click()
        self.assertTrue(driver.current_url.startswith(Homepage.google_auth))
        time.sleep(1)



if __name__ == "__main__":
    unittest.main()