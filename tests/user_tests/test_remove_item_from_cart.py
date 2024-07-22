import time
import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.jewelry.Jewelry import Jewelry
from modules.ui.shopping_cart.ShoppingCartPage import ShoppingCart
@pytest.mark.usefixtures("setup_and_teardown")
class Test_06_RemoveFromCart:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp =HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.jp = Jewelry(self.driver)
        self.sc = ShoppingCart(self.driver)

    @pytest.mark.smoke
    def test_add_item_to_cart(self):
        self.hp.click_on_link_jewelry()
        self.jp.add_flower_girl_bracelet_to_cart()
        self.sc.click_on_link_shopping_cart()
        self.sc.remove_items_from_the_cart()
        element = self.sc.get_message_shopping_cart_empty()
        assert element.is_displayed()


