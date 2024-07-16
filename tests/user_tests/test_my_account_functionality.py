import pytest
from modules.ui.my_account.MyAccountPage import MyAccount
from modules.ui.user_login.LoginPage import Login
from modules.ui.home_page.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class Test_016_MyAccount():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.lp = Login(self.driver)
        self.ma = MyAccount(self.driver)

    def test_my_account_functionality(self):
        self.lp.user_login()
        self.ma.click_on_link_my_account()
        element = self.ma.get_customer_info_title()
        assert element.is_displayed()
        element = self.ma.get_customer_addresses()
        assert element.is_displayed()
        element = self.ma.get_orders()
        assert element.is_displayed()
        element = self.ma.get_downloadable_products()
        assert element.is_displayed()
        element = self.ma.get_back_in_stock_subscriptions()
        assert element.is_displayed()
        element = self.ma.get_reward_points()
        assert element.is_displayed()
        element = self.ma.get_change_password()
        assert element.is_displayed()
        element = self.ma.get_my_product_reviews()
        assert element.is_displayed()

