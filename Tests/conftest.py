import pytest
from selenium import webdriver
from Config.Config import TestData


@pytest.fixture(params=["chrome", "edge"], scope='class')
def init_driver(request):
    wd = webdriver.Chrome(executable_path=TestData.CHROME_PATH)
    wd.delete_all_cookies()
    request.cls.driver = wd
    wd.get(TestData.URL)

    yield
    wd.quit()

