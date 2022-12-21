from selenium.webdriver.common.by import By

from test import TestWebsite


class Testing(TestWebsite):
    def test_tools_menu(self):
        """this test checks presence of Developer Tools menu item"""
        tools_menu = self.browser.find_element(
            By.XPATH,
            "//div[@data-test='main-menu-item' and @data-test-marker = 'Developer Tools']"
        )

        tools_menu.click()

        menu_popup = self.browser.find_element(
            By.CSS_SELECTOR,
            "div[data-test='main-submenu']"
        )
        assert menu_popup is not None
