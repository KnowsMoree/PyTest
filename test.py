import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestWebsite:
    # 1. Check browser configuration in browser_setup_and_teardown
    # 2. Run 'Selenium Tests' configuration
    # 3. Test report will be created in reports/ directory

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        # self.use_selenoid = False  # set to True to run tests with Selenoid
        #
        # if self.use_selenoid:
        #     self.browser = webdriver.Remote(
        #         command_executor='http://localhost:4444/wd/hub',
        #         desired_capabilities={
        #             "browserName": "chrome",
        #             "browserSize": "1920x1080"
        #         }
        #     )
        # else:
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get("https://app.tandatanganku.com")

        yield

        self.browser.close()
        self.browser.quit()

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
