import pytest
from modules.ui.user_login.LoginPage import Login
from modules.ui.home_page.HomePage import HomePage
from modules.ui.user_registration.RegistrationPage import Registration



@pytest.mark.usefixtures("setup_and_teardown")
class Test_09_TestLogin:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.lp = Login(self.driver)
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        #self.lp.click_link_login()
        self.rp = Registration(self.driver)

    @pytest.mark.smoke
    def test_login_with_valid_credentials(self):
        self.rp.returning_user_registration()
        self.lp.click_logout()
        self.lp.click_link_login()
        self.lp.enter_valid_id_to_text_box_email_id()
        self.lp.enter_valid_pswd_to_text_box_password()
        self.lp.click_button_login()
        element = self.lp.get_logout_element()
        if element.is_displayed():
            self.lp.click_logout()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\login_user_failure.png")
            assert False


    def test_login_with_invalid_email(self):
        self.lp.click_link_login()
        self.lp.enter_invalid_id_to_text_box_email_id()
        self.lp.enter_valid_pswd_to_text_box_password()
        self.lp.click_button_login()
        message = self.lp.get_warning_email_error()
        if message.is_displayed():
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\login_failure.png")
            assert False

    def test_login_with_invalid_password(self):
        self.lp.click_link_login()
        self.lp.enter_valid_id_to_text_box_email_id()
        self.lp.enter_invalid_pswd_to_text_box_password()
        self.lp.click_button_login()
        message = self.lp.get_warning_invalid_credentials()
        if message.is_displayed():
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\invalid_pswd.png")
            assert False

    def test_login_with_empty_fields(self):
        self.lp.click_link_login()
        self.lp.enter_no_value_to_text_box_email_id()
        self.lp.enter_no_value_to_text_box_password()
        self.lp.click_button_login()
        message = self.lp.get_warning_email_error()
        if message.is_displayed():
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\empty_fields.png")
            assert False


