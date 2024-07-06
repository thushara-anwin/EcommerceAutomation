import time
import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.cellphones.CellPhonesPage import CellPhone
from modules.ui.electronics_page.ElectronicsPage import Electronics
from modules.ui.user_login.LoginPage import Login
from modules.ui.footer_links.FooterSection import Footer



@pytest.mark.usefixtures("setup_and_teardown")
class Test_012_CompareProducts():
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()
        self.cp = CellPhone(self.driver)
        self.ep = Electronics(self.driver)
        self.lp = Login(self.driver)
        self.fs = Footer(self.driver)



    def test_compare_products(self):
        self.lp.user_login()
        self.hp.click_on_link_electronics()
        self.ep.click_on_link_cellphone()
        self.cp.add_htc_m8one_android_lollipop_to_compare_list()
        self.hp.click_on_link_electronics()
        self.ep.click_on_link_cellphone()
        time.sleep(12)
        self.cp.add_htc_one_mini_blue_to_compare_list()
        time.sleep(15)
        self.fs.click_on_link_compare_products_list()
        element = self.fs.get_compare_products_title()
        assert element.is_displayed()
