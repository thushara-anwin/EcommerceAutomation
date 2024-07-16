import time
import pytest
from modules.ui.user_registration.RegistrationPage import Registration
from modules.ui.home_page.HomePage import HomePage
from modules.ui.cellphones.CellPhonesPage import CellPhone
from modules.ui.electronics_page.ElectronicsPage import Electronics
from modules.ui.user_login.LoginPage import Login
from modules.ui.shopping_cart.ShoppingCartPage import ShoppingCart
from modules.ui.shipping_page.ShippingPage import Shipping





@pytest.mark.usefixtures("setup_and_teardown")
class Test_013_CheckoutRegisteredUser():
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

    def test_checkout_functionality_registeted_user(self):
        #self.rp.returning_user_registration()
        #self.lp.click_logout()
        self.lp.user_login()
        self.hp.click_on_link_electronics()
        self.ep.click_on_link_cellphone()
        self.cp.add_htc_one_mini_blue_to_cart()
        self.hp.click_on_link_electronics()
        self.ep.click_on_link_cellphone()
        self.cp.add_htc_m8one_android_lollipop_to_cart()
        self.sc.click_on_link_shopping_cart()
        self.sc.click_on_check_box_terms_of_service()
        self.sc.click_on_button_checkout()
        element = self.sp.get_to_checkout_page()
        assert element.is_displayed()
