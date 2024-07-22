import time
import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.user_registration.RegistrationPage import Registration

@pytest.mark.usefixtures("setup_and_teardown")

class Test_08_NewUserRegistration:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.rp = Registration(self.driver)

    @pytest.mark.smoke
    def test_user_registration_with_valid_data(self):
        self.rp.click_on_link_registration()
        self.rp.click_on_radio_male()
        self.rp.enter_value_to_text_box_fname()
        self.rp.enter_value_to_text_box_lname()
        self.rp.enter_date_of_birth()
        self.rp.enter_value_to_text_box_email()
        self.rp.enter_value_to_text_box_company()
        self.rp.enter_value_to_text_box_pswd_and_confirm_pswd()
        self.rp.click_on_button_register()
        msg = self.rp.get_message_registration_completed()
        assert msg.is_displayed()


