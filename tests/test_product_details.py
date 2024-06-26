import time
import pytest
from modules.HomePage import HomePage
from modules.ClothingPage import *


@pytest.mark.usefixtures("setup_and_teardown")
class Test_03_ProductDetails:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        time.sleep(15)
        self.cp = ClothingPage(self.driver)

    def test_if_product_details_displayed(self):
        self.hp.click_clothing()
        self.cp.click_custom_t_shirt()
        element = self.cp.get_custom_t_shirt_name()
        assert element.is_displayed()
        element1 = self.cp.get_custom_t_shirt_price()
        assert element1.is_displayed()
        element2= self.cp.get_custom_t_shirt_description()
        assert element2.is_displayed()

