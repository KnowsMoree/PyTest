import time

from selenium.webdriver.common.by import By

from test import TestWebsite


class TestReg(TestWebsite):
    def test_register(self):
        link_create = self.browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div[1]/a[1]")
        link_create.click()
        time.sleep(5)
