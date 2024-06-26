from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


class SeleniumBase:
    def __init__(self,driver,timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver,timeout)


    def get_element(self,locator):
        element = self.wait.until(ec.visibility_of_element_located(locator))
        return element

    def click_element(self,locator):
        element = self.get_element(locator)
        element.click()

    def enter_value(self,data,locator):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(data)

    def enter_dropdown_value(self,text,locator):
        self.selection = Select(locator)
        self.selection.select_by_visible_text()

    def get_text(self,locator):
        element = self.get_element(locator)
        text = element.text
        return text


