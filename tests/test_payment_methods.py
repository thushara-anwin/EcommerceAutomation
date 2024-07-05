import time
import pytest
from modules.HomePage import HomePage
from modules.CellPhonesPage import *
from modules.ElectronicsPage import *
from modules.LoginPage import *
from modules.ShoppingCartPage import *
from modules.ShippingPage import *





@pytest.mark.usefixtures("setup_and_teardown")
class Test_014_PaymentMethods():
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.cp = CellPhone(self.driver)
        self.ep = Electronics(self.driver)
        self.lp = Login(self.driver)
        self.sc = ShoppingCart(self.driver)
        self.sp = Shipping(self.driver)





    def test_compare_products(self):
        self.lp.user_login()
        self.hp.click_on_link_electronics()
        self.ep.click_on_link_cellphone()
        self.cp.add_htc_one_mini_blue_to_cart()
        self.sc.click_on_link_shopping_cart()
        self.sc.click_on_check_box_terms_of_service()
        self.sc.click_on_button_checkout()
        time.sleep(2)
        #self.sp.returning_customer_shipping_address()
        self.sp.click_on_button_continue_with_the_shipping_address()
        self.sp.click_on_radio_shipping_method_nextdayair()
        self.sp.click_on_button_next_shipping_method()
        self.sp.click_on_radio_check_money_order()
        self.sp.click_on_button_next_step_info()
        self.sp.click_on_button_confirm()
        element = self.sp.get_message_shopping_success()
        assert element.is_displayed()
