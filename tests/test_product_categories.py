
import pytest
from modules.ui.home_page.HomePage import HomePage

@pytest.mark.usefixtures("setup_and_teardown")
class Test_03_ProductCategories:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()

    def test_computer_products_navigation(self):
        self.hp.click_on_link_computers()
        element = self.hp.get_computer_products()
        if element.is_displayed():
            assert True
        else:
            assert False

    def test_electronics_products_navigation(self):
        self.hp.click_on_link_electronics()
        element = self.hp.get_electronics_products()
        if element.is_displayed():
            assert True
        else:
            assert False

    def test_apparel_products_navigation(self):
        self.hp.click_on_link_apparel()
        element = self.hp.get_apparel_products()
        if element.is_displayed():
            assert True
        else:
            assert False

    def test_digital_downloads_products_navigation(self):
        self.hp.click_on_link_digital_downloads()
        element = self.hp.get_digital_download_products()
        if element.is_displayed():
            assert True
        else:
            assert False

    def test_books_products_navigation(self):
        self.hp.click_on_link_books()
        element = self.hp.get_books_products()
        if element.is_displayed():
            assert True
        else:
            assert False

    def test_jewelry_products_navigation(self):
        self.hp.click_on_link_jewelry()
        element = self.hp.get_jewelry_products()
        if element.is_displayed():
            assert True
        else:
            assert False

    def test_gift_card_products_navigation(self):
        self.hp.click_on_link_gift_cards()
        element = self.hp.get_gift_card_products()
        if element.is_displayed():
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\giftcard_products_not_found.png")

            assert False
