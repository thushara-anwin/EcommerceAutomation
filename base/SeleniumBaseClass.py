from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select



class SeleniumBase:
    def __init__(self,driver,timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver,timeout)
        self.act = ActionChains(self.driver)

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

    def get_element_mouse_hover(self,*locators):
        if len(locators) == 2:
            element1 = self.get_element(locators[0])
            self.act.move_to_element(element1)
            self.act.click().perform()
            element2 = self.get_element(locators[1])
            self.act.move_to_element(element2).click().perform()
        elif len(locators) == 3:
            element1 = self.get_element(locators[0])
            self.act.move_to_element(element1)
            self.act.click().perform()
            element2 = self.get_element(locators[1])
            element3 = self.get_element(locators[2])
            self.act.move_to_element(element2).move_to_element(element3).click().perform()




