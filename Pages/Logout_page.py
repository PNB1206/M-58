from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class Logout_Page(BasePage):
    user = (By.XPATH, "//span[@class='mr-2 d-none d-lg-inline text-gray-600 small']")
    logout_button = (By.XPATH, "//a[@class='dropdown-item']")

    def __init__(self, driver):
        super().__init__(driver)


    def get_dashboardpage_title(self,title):
        return self.get_title(title)

    def do_logout(self):
        self.do_click(self.user)
        self.do_click(self.logout_button)
