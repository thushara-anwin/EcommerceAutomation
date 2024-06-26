from selenium import webdriver

class WebdriverFactory:
    def __init__(self,browser):
        self.browser = browser

    def get_driver_instance(self):
        if self.browser.lower().__eq__('chrome'):
            headless = False
            driver = None
            if headless:
                crm_options = webdriver.ChromeOptions()
                crm_options.add_argument('--headless')
            driver = webdriver.Chrome()
        elif self.browser.lower().__eq__("firefox"):
            driver= webdriver.Firefox()
        elif self.browser.lower().__eq__('edge'):
            driver = webdriver.Edge()
        else:
            print("Wrong choice")
        return driver