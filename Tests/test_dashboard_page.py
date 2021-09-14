import time
from Config.Config import TestData
from Pages.Dashboard_Page import Dashboard_Page
from Pages.Login_page import Login_Page
from Tests.test_base import BaseTest


class Test_Dashboard_Page(BaseTest):

    def test_assign_driver(self):
        self.loginpage = Login_Page(self.driver)
        self.loginpage.do_login(TestData.Mobile, TestData.Password)
        self.dashboardPage = Dashboard_Page(self.driver)
        self.dashboardPage.click_on_assig_driver()
        self.dashboardPage.select_nickname()
        self.dashboardPage.click_on_start()
        time.sleep(20)
        self.dashboardPage.click_on_start()
        self.dashboardPage.click_submit()

