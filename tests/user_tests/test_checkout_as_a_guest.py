import time

import pytest

from modules.ui.home_page.HomePage import HomePage
from modules.ui.jewelry.Jewelry import Jewelry
from modules.ui.shopping_cart.ShoppingCartPage import ShoppingCart
from modules.ui.shipping_page.ShippingPage import Shipping


@pytest.mark.usefixtures("setup_and_teardown")
class Test_07_CheckoutAsGuest:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.jp = Jewelry(self.driver)
        self.sc = ShoppingCart(self.driver)
        self.sp= Shipping(self.driver)

    @pytest.mark.smoke
    def test_checkout_as_a_guest_user(self):
        self.hp.click_on_link_jewelry()
        self.jp.add_vintage_style_engagement_ring_to_cart()
        self.jp.add_flower_girl_bracelet_to_cart()
        self.sc.click_on_link_shopping_cart()
        self.sc.click_on_check_box_terms_of_service()
        self.sc.click_on_button_checkout()
        self.sp.click_on_button_checkout_guest()
        self.sp.guest_shipping_address()
        self.sp.click_on_button_continue()
        self.sp.shipping_method('next_day')
        self.sp.click_on_radio_check_money_order()
        self.sp.click_on_button_next_step_info()
        self.sp.click_on_button_confirm()
        element = self.sp.get_message_shopping_success()
        assert element.is_displayed()
















