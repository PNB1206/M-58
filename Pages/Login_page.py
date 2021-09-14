from selenium.webdriver.common.by import By

from Config.Config import TestData
from Pages.BasePage import BasePage


class Login_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        #self.driver.get(TestData.URL)

    #by_locators:
    mobile_number =(By.NAME, 'username')
    password = (By.XPATH, "//input[@type='password']")
    login_button = (By.ID, 'submit-btn')
    error_message=(By.ID, "aj_pass")

    #Page Actions
    def do_login(self, mobileNo, paswrd, ):
        self.do_send_keys(self.mobile_number, mobileNo)
        self.do_send_keys(self.password, paswrd)
        self.do_click(self.login_button)

    def get_err_msg(self):
        return self.getText(self.error_message)


    def get_dashboardpage_title(self, title):
        return self.get_title(title)

    def do_logout(self):
        self.do_click(self.user)
        self.do_click(self.logout_button)