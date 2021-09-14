from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import _find_elements
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage


class Dashboard_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #by locators


    assign_driver = (By.XPATH, "//span[normalize-space()='Assign Driver']")
    driver_btn = (By.XPATH, "//a[normalize-space()='Driver']")
    nick_name =(By.XPATH, "//select[@id='machine_select']")
    names_xpath = "//select[@id='machine_select']/option"
    start_timer = (By.XPATH, "//input[@id='start_timer']")
    stop_timer = (By.XPATH, "//input[@id='start_timer']")
    reset_timer =(By.XPATH, "//input[@value='Reset']")
    submit_button =(By.XPATH, "//button[normalize-space()='Submit']")
    value ="MA-03"

    def get_dashboard_page_title(self, title):
        title = self.get_title(title)
        return title

    def click_on_assig_driver(self):
        self.do_click(self.assign_driver)
        self.do_click(self.driver_btn)

    def select_nickname(self):
        nameslist = self.driver.find_elements(By.XPATH, self.names_xpath)
        for ele in nameslist:
            ele.text
            if ele.text == 'MA-01':
                ele.click()
                break

    def click_on_start(self):
        self.do_click(self.start_timer)

    def click_on_stop(self):
        self.do_click(self.stop_timer)

    def click_reset(self):
        self.do_click(self.reset_timer)

    def click_submit(self):
        self.do_click(self.submit_button)

    def get_alert_text(self):
        alert = Alert(self.driver)
        alert.accept()
        return alert.text

