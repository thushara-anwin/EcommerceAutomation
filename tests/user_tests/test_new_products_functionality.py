import time

import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.footer_links.FooterSection import Footer


@pytest.mark.usefixtures("setup_and_teardown")
class Test_019_NewProducts():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.fs = Footer(self.driver)

    @pytest.mark.smoke
    def test_my_account_functionality(self):
        self.fs.click_on_link_new_products()
        time.sleep(13)
        element = self.fs.get_title_new_products()
        if element.is_displayed():
            assert True
        else:

            self.driver.savescreeshot(".\\screenshots\\new_products.png")
            assert False
