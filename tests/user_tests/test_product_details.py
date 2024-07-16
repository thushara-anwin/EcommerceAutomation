import time
import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.clothings_page.ClothingPage import Clothing


@pytest.mark.usefixtures("setup_and_teardown")
class Test_04_ProductDetails:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.cp = Clothing(self.driver)

    def test_if_product_details_displayed(self):
        self.hp.click_clothing()
        self.cp.click_custom_t_shirt()
        element = self.cp.get_custom_t_shirt_name()
        assert element.is_displayed()
        element1 = self.cp.get_custom_t_shirt_price()
        assert element1.is_displayed()
        element2= self.cp.get_custom_t_shirt_description()
        assert element2.is_displayed()

