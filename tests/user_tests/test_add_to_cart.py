import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.electronics_page.ElectronicsPage import Electronics
from modules.ui.clothings_page.ClothingPage import Clothing
import time
@pytest.mark.usefixtures("setup_and_teardown")
class Test_05_Add_to_Cart:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.ep = Electronics(self.driver)
        self.cp = Clothing(self.driver)


    @pytest.mark.smoke
    def test_adding_cellphone_to_cart(self):
        self.hp.click_on_link_electronics()
        self.ep.click_on_link_cellphone()
        self.ep.click_htc_one_mini_blue()
        self.ep.add_cellphone_pdts_to_cart()
        element = self.hp.get_message_product_added_locator()
        assert element.is_displayed()

    def test_enter_text_custom_tshirt(self):
        self.hp.click_clothing()
        self.cp.click_custom_t_shirt()
        self.cp.enter_custom_tshirt_code()
        self.cp.click_add_to_cart()
        ele = self.cp.get_added_to_cart_message()
        if ele.is_displayed():
            assert True
        else:
            assert False

    def test_no_text_custom_tshirt(self):
        self.hp.click_clothing()
        self.cp.click_custom_t_shirt()
        self.cp.enter_custom_tshirt_code()
        self.cp.click_add_to_cart()
        ele = self.cp.get_warning_enter_text()
        if ele.is_displayed():
            assert True
        else:
            assert False

    def test_add_quantity_custom_tshirt(self):
        self.hp.click_clothing()
        self.cp.click_custom_t_shirt()
        self.cp.enter_custom_tshirt_code()
        self.cp.enter_custom_tshirt_quantity()
        self.cp.click_add_to_cart()
        ele = self.cp.get_added_to_cart_message()
        if ele.is_displayed():
            assert True
        else:
            assert False

    def test_add_maximum_quantity_custom_t_shirt(self):
        self.hp.click_clothing()
        self.cp.click_custom_t_shirt()
        self.cp.enter_custom_tshirt_code()
        self.cp.enter_maximum_quantity_custom_tshirt()
        self.cp.click_add_to_cart()
        ele = self.cp.get_warning_maximum_quantity()
        if ele.is_displayed():
            assert True
        else:
            assert False






