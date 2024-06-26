import pytest
from WebdriverFactory import WebdriverFactory

@pytest.fixture(scope="class")
def setup_and_teardown(request):
    wf = WebdriverFactory('chrome')
    driver = wf.get_driver_instance()
    #driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()
