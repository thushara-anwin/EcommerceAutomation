import pytest
from HomePage import *

@pytest.mark.usefixtures("setup_and_teardown")
class Test_01_Search:
    @pytest.fixture(autouse= True)
    def setup(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()

    def test_search_with_valid_data(self):
        self.hp.enter_valid_search_data()
        self.hp.click_search_button()
        ele = self.hp.get_valid_product_locator()
        if ele.is_displayed():
            assert True
        else:
            assert False

    def test_search_with_invalid_data(self):
        self.hp.enter_invalid_search_data()
        self.hp.click_search_button()
        ele = self.hp.get_no_product_message_locator()
        if ele.is_displayed():
            assert True
        else:
            assert False

    def test_minimum_length_search_data(self):
        self.hp.enter_short_search_data()
        self.hp.click_search_button()
        ele = self.hp.get_minimum_length_message_locator()
        if ele.is_displayed():
            assert True
        else:
            assert False