import pytest
from modules.ui.my_account.MyAccountPage import MyAccount
from modules.ui.user_login.LoginPage import Login
from modules.ui.home_page.HomePage import HomePage
from modules.ui.user_registration.RegistrationPage import Registration


@pytest.mark.usefixtures("setup_and_teardown")
class Test_017_RewardPoints():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.rp = Registration(self.driver)
        self.ma = MyAccount(self.driver)

    def test_my_account_functionality(self):
        self.rp.returning_user_registration_login()
        self.ma.click_on_link_my_account()
        self.ma.get_reward_points()
        element = self.ma.get_current_rewards_balance()
        if element.is_displayed():
            assert True
        else:
            assert False