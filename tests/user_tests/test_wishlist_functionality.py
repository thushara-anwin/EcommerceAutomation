import time
import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.clothings_page.ClothingPage import Clothing


@pytest.mark.usefixtures("setup_and_teardown")
class Test_011_Wishlist():
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.cp = Clothing(self.driver)

    def test_adding_and_removing_items_to_wishlist(self):
        self.hp.click_clothing()
        self.cp.add_levi_511_jeans_to_wishlist()
        #self.hp.click_clothing()
        #self.cp.add_custom_tshirt_to_wishlist()
        #self.hp.click_clothing()
        #self.cp.add_nike_tailwind_short_sleeve_running_shirt_to_wishlist()
        self.hp.click_on_link_wishlist()
        self.cp.remove_levi_511_jeans_from_wishlist()
        message = self.cp.get_wishlist_empty_message()
        assert message.is_displayed()

