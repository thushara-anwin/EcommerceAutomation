headless = False
from selenium import webdriver

class WebdriverFactory:
    def __init__(self, browser='Chrome'):
        self.browser = browser

    def get_driver_instance(self, headless=False):
        driver = None
        if self.browser.lower() == 'chrome':
            crm_option = webdriver.ChromeOptions()
            if headless:
                crm_option.add_argument('--headless')
            driver = webdriver.Chrome(options=crm_option)

        elif self.browser.lower() == 'firefox':
            driver = webdriver.Firefox()

        elif self.browser.lower() == 'edge':
            driver = webdriver.Edge()
        driver.maximize_window()
        return driver


# from selenium import webdriver
#
# class WebdriverFactory:
#     def __init__(self,browser):
#         self.browser = browser
#
#     def get_driver_instance(self):
#         if self.browser.lower().__eq__('chrome'):
#             headless = False
#             driver = None
#             if headless:
#                 crm_options = webdriver.ChromeOptions()
#                 crm_options.add_argument('--headless')
#             driver = webdriver.Chrome()
#         elif self.browser.lower().__eq__("firefox"):
#             driver= webdriver.Firefox()
#         elif self.browser.lower().__eq__('edge'):
#             driver = webdriver.Edge()
#         else:
#             print("Wrong choice")
#         return driver