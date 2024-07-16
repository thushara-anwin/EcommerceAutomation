import time
import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.cellphones.CellPhonesPage import CellPhone
from modules.ui.electronics_page.ElectronicsPage import Electronics
from modules.ui.user_login.LoginPage import Login
from modules.ui.shopping_cart.ShoppingCartPage import ShoppingCart
from modules.ui.shipping_page.ShippingPage import Shipping
from modules.ui.user_registration.RegistrationPage import Registration






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
        self.rp = Registration(self.driver)

    def test_payment_method_money_order_or_check(self):
        # self.rp.returning_user_registration()
        # self.lp.click_logout()
        self.lp.user_login()
        self.hp.click_on_link_electronics()
        self.ep.click_on_link_cellphone()
        self.cp.add_htc_one_mini_blue_to_cart()
        self.sc.click_on_link_shopping_cart()
        self.sc.click_on_check_box_terms_of_service()
        self.sc.click_on_button_checkout()
        time.sleep(10)
        #self.sp.click_on_button_continue_with_the_shipping_address()
        # element = self.sp.get_continue_with_the_shipping_address()
        # if element.is_displayed():
        #     self.sp.click_on_button_continue_with_the_shipping_address()
        # else:
        #     self.sp.returning_customer_shipping_address()

        self.sp.returning_customer_shipping_address()
        self.sp.click_on_radio_shipping_method_nextdayair()
        self.sp.click_on_button_next_shipping_method()
        self.sp.click_on_radio_check_money_order()
        self.sp.click_on_button_next_step_info()
        self.sp.click_on_button_confirm()
        element = self.sp.get_message_shopping_success()
        assert element.is_displayed()
        self.lp.click_logout()

    def test_payment_method_credit_card(self):
        # self.rp.returning_user2_registration()
        self.lp.user_login()
        self.hp.click_on_link_electronics()
        self.ep.click_on_link_cellphone()
        self.cp.add_htc_one_mini_blue_to_cart()
        self.sc.click_on_link_shopping_cart()
        self.sc.click_on_check_box_terms_of_service()
        self.sc.click_on_button_checkout()
        self.sp.click_on_button_continue_with_the_shipping_address()
        self.sp.click_on_radio_shipping_method_nextdayair()
        self.sp.click_on_button_next_shipping_method()
        self.sp.click_on_radio_creditcard()
        self.sp.add_credit_card_details()
        time.sleep(15)
        self.sp.click_on_button_confirm()
        element = self.sp.get_message_shopping_success()
        assert element.is_displayed()
