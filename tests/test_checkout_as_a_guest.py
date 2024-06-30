import time

import pytest
from modules.HomePage import *
from modules.Jewelry import *
from modules.ShoppingCartPage import *
from modules.ShippingPage import *


@pytest.mark.usefixtures("setup_and_teardown")
class Test_07_CheckoutAsGuest:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.jp = Jewelry(self.driver)
        self.sc = ShoppingCart(self.driver)
        self.sp= Shipping(self.driver)

    def test_checkout_as_a_guest_user(self):
        self.hp.click_on_link_jewelry()
        self.jp.add_vintage_style_engagement_ring_to_cart()
        self.jp.add_flower_girl_bracelet_to_cart()
        self.sc.click_on_link_shopping_cart()
        self.sc.click_on_check_box_terms_of_service()
        self.sc.click_on_button_checkout()
        self.sp.click_on_button_checkout_guest()
        self.sp.shipping_address()
        self.sp.click_on_button_continue()
        self.sp.shipping_method('next_day')
        self.sp.click_on_radio_check_money_order()
        self.sp.click_on_button_next_step_info()
        self.sp.click_on_button_confirm()
        element = self.sp.get_message_shopping_success()
        assert element.is_displayed()
















