import pytest
from modules.ui.user_login.LoginPage import Login
from modules.ui.home_page.HomePage import HomePage
from modules.ui.footer_links.FooterSection import Footer
import time

@pytest.mark.usefixtures("setup_and_teardown")
class Test_018_ContactUs():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.lp = Login(self.driver)
        self.fs = Footer(self.driver)

    def test_contact_us_with_all_data(self):
        self.fs.click_on_link_contact_us()
        self.fs.enter_fullname()
        self.fs.enter_email()
        self.fs.enter_enquiry()
        time.sleep(12)

        self.fs.click_submit_enquiry()
        element = self.fs.get_success_message_enquiry_submission()
        if element.is_displayed():
            assert True
        else:
            assert False

    def test_contact_us_with_empty_full_name_field(self):
        self.fs.click_on_link_contact_us()
        self.fs.empty_fullname()
        self.fs.enter_email()
        self.fs.enter_enquiry()
        time.sleep(12)

        self.fs.click_submit_enquiry()
        element = self.fs.get_message_error_full_name()
        if element.is_displayed():
            assert True
        else:
            assert False


    def test_contact_us_with_empty_email_field(self):
        self.fs.click_on_link_contact_us()
        self.fs.enter_fullname()
        self.fs.empty_email()
        self.fs.enter_enquiry()
        self.fs.click_submit_enquiry()
        element = self.fs.get_message_error_email()
        if element.is_displayed():
            assert True
        else:
            assert False

    def test_contact_us_with_empty_enquiry_field(self):
        self.fs.click_on_link_contact_us()
        self.fs.enter_fullname()
        self.fs.enter_email()
        self.fs.empty_enquiry()
        self.fs.click_submit_enquiry()
        element = self.fs.get_message_error_enquiry()
        if element.is_displayed():
            assert True
        else:
            assert False

    def test_contact_us_with_empty_fields(self):
        self.fs.click_on_link_contact_us()
        self.fs.empty_fullname()
        self.fs.empty_email()
        self.fs.empty_enquiry()
        self.fs.click_submit_enquiry()
        error_fullname = self.fs.get_message_error_enquiry()
        error_email = self.fs.get_message_error_enquiry()
        error_enquiry = self.fs.get_message_error_enquiry()
        assert error_fullname.is_displayed()
        assert error_email.is_displayed()
        assert error_enquiry.is_displayed()






