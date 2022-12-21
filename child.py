import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from test import TestWebsite


class Testing(TestWebsite):
    # super().browser_setup_and_teardown

    def test_login_and_upload_file(self):
        """this test checks presence of Developer Tools menu item"""
        uname = self.browser.find_element(By.XPATH, "//*[@id='username']")
        uname.send_keys("ditest6@tandatanganku.com" + Keys.ENTER)
        pw = self.browser.find_element(By.XPATH, "//input[@id='pd']")
        pw.send_keys("Coba1234" + Keys.ENTER)
        time.sleep(2)
        file = self.browser.find_element(By.XPATH, "//input[@type='file']")
        file.send_keys("C:\\Users\\dignitas\\Downloads\\company_image_20221101065745 (1) (1).pdf")
        self.browser.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)
