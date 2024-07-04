import time
import pytest
from modules.LoginPage import *
from modules.HomePage import *
from modules.Jewelry import *
from modules.ShoppingCartPage import *
from modules.RegistrationPage import *
from modules.ShippingPage import *

@pytest.mark.usefixtures("setup_and_teardown")
class Test_10_ModifyOrCancelOrder:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.lp = Login(self.driver)
        self.jp = Jewelry(self.driver)
        self.sc= ShoppingCart(self.driver)
        self.rp = Registration(self.driver)
        self.sp = Shipping(self.driver)

    def test_user_can_modify_or_cancel_order(self):
        #self.rp.returning_user_registration()
        #self.lp.click_logout()
        self.lp.user_login()
        time.sleep(12)
        self.hp.click_on_link_jewelry()
        self.jp.add_flower_girl_bracelet_to_cart()
        self.jp.add_vintage_style_engagement_ring_to_cart()
        self.jp.add_flower_girl_bracelet_to_cart()
        self.sc.click_on_link_shopping_cart()
        self.sp.click_on_button_continue_shopping()
        self.jp.add_vintage_style_engagement_ring_to_cart()
        self.sc.click_on_link_shopping_cart()
        self.sc.remove_items_from_the_cart()
        self.sc.remove_items_from_the_cart()
        element = self.sc.get_message_shopping_cart_empty()
        assert element.is_displayed()




        time.sleep(12)
