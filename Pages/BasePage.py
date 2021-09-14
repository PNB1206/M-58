from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
"""This class is the parent of all classes"""
"""It contains all the generic methods and utilities for all pages"""



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def getText(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_title(self, title):
        #WebDriverWait(self.driver, 30).until(ec.title_is(title))
        return self.driver.title

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def is_enable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def do_clear(self,by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).clear()


    def get_text(self, by_locator):
        self.wait = WebDriverWait(self.driver, 25)
        element = self.wait.until(ec.visibility_of_element_located(by_locator))
        return element.text

    #def take_screenshot(self):


        # To select multiple options from drop down

    def select_all_values(options_list, value):
        if not value[0] == 'all':
            for ele in options_list:
                print(ele.text)
                for k in range(len(value)):
                    if ele.text == value[k]:
                        ele.click()
                        break
        else:
            try:
                for ele in options_list:
                    ele.click()
            except Exception as e:
                print(e)


    def select_by_values(self, element, index):
        select =Select(element)
        #select.select_by_value(value)
        self.select_by.index(index)



