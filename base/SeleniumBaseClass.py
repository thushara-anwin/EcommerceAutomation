from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import logging
log = logging.getLogger('testLogger')


class SeleniumBase:
    def __init__(self,driver,timeout=30):
        self.selection = None
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver,timeout)
        self.act = ActionChains(self.driver)

    def get_element(self, locator):
        try:
            #log.info(f"finding element:{locator}")
            element = self.wait.until(ec.visibility_of_element_located(locator))
            return element
        except Exception as e:
            self.driver.save_screenshot(".\\screenshots\\locator_file.png")
            raise

    def click_element(self,locator):
        log.info(f"click to element :{locator}")
        element = self.get_element(locator)
        element.click()

    def enter_value(self,data,locator):
        log.info(f"enter value {data} to element :{locator} ")
        element = self.get_element(locator)
        element.clear()
        element.send_keys(data)

    def enter_dropdown_value(self,text,locator):
        element = self.get_element(locator)
        self.selection = Select(element)
        self.selection.select_by_visible_text(text)

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
        elif len(locators) == 4:
            element1 = self.get_element(locators[0])
            self.act.move_to_element(element1)
            self.act.click().perform()
            element2 = self.get_element(locators[1])
            element3 = self.get_element(locators[2])
            element4 = self.get_element(locators[4])
            self.act.move_to_element(element2).move_to_element(element3).move_to_element(element4).click().perform()


    # def add_product_to_cart(self,product_locator,add_to_cart_locator):
    #     self.click_element(product_locator)
    #     self.click_element(add_to_cart_locator)







