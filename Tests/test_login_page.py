from Config.Config import TestData
from Pages.Dashboard_Page import Dashboard_Page
from Pages.Login_page import Login_Page
from Pages.Logout_page import Logout_Page
from Tests.test_base import BaseTest


class Test_LoginPage(BaseTest):

    """Login with Invalid Credentials"""

    def test_login_valid_mobile_invalid_pswrd(self):
        self.loginpage = Login_Page(self.driver)
        self.loginpage.do_login(TestData.Werong_mobile, TestData.Wrong_password)
        err_msg = self.loginpage.get_err_msg()
        assert err_msg == TestData.Err_msg

    """Login with Valid Mobile & invalid Password"""

    def test_login_valid_mobile_invalid_pswrd(self):
        self.loginpage = Login_Page(self.driver)
        self.loginpage.do_login(TestData.Mobile, TestData.Wrong_password)
        err_msg = self.loginpage.get_err_msg()
        assert err_msg == TestData.Err_msg

    """Login with Invalid Mobile & valid Password"""

    def test_login_valid_mobile_invalid_pswrd(self):
        self.loginpage = Login_Page(self.driver)
        self.loginpage.do_login(TestData.Werong_mobile, TestData.Password)
        err_msg = self.loginpage.get_err_msg()
        assert err_msg == TestData.Err_msg

    """Login with valid credentials"""

    def test_login(self):
        self.lp = Login_Page(self.driver)
        self.lp.do_login(TestData.Mobile, TestData.Password)
        self.dbp=Dashboard_Page(self.driver)
        title = self.dbp.get_dashboard_page_title(TestData.dashboard_page_title)
        assert title == TestData.dashboard_page_title
        self.lop = Logout_Page(self.driver)
        self.lop.do_logout()


