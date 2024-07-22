import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.electronics_page.ElectronicsPage import Electronics

@pytest.mark.usefixtures("setup_and_teardown")
class Test_05_Add_to_Cart:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.ep = Electronics(self.driver)

    @pytest.mark.smoke
    def test_adding_cellphone_to_cart(self):
        self.hp.click_on_link_electronics()
        self.ep.click_on_link_cellphone()
        self.ep.click_htc_one_mini_blue()
        self.ep.add_cellphone_pdts_to_cart()
        element = self.hp.get_message_product_added_locator()
        assert element.is_displayed()

