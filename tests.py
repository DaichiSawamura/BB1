import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestsMain(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.URI = "https://goldapple.ru/parfjumerija"

    def open_browser(self):
        driver = self.driver
        driver.get(self.URI)

    def test_get_url(self):
        self.open_browser()
        assert "Gold Apple" in self.driver.title

    def test_find_element(self):
        self.open_browser()
        time.sleep(2)
        assert self.driver.find_element(By.CLASS_NAME, 'IYYkW') is not None

    def test_click(self):
        self.open_browser()
        self.driver.maximize_window()
        button = self.driver.find_element(By.CLASS_NAME, 'IYYkW')
        button.click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()
