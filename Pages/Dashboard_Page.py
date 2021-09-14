from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage


class Dashboard_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_dashboard_page_title(self, title):
        title = self.get_title(title)
        return title