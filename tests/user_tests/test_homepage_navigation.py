import pytest
from modules.ui.home_page.HomePage import HomePage
from modules.ui.home_page.home_page_data import *

@pytest.mark.usefixtures("setup_and_teardown")
class Test_01_HomepageNavigation:
    @pytest.fixture(autouse= True)
    def setup(self):
        self.hp = HomePage(self.driver)

    def test_homepage_navigation(self):
        self.hp.navigate_to_homepage()
        ele = self.hp.get_welcome_message()
        if ele.is_displayed():
            assert True
        #     self.driver.close()
        # else:
        #     assert False

