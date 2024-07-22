import pytest
from modules.ui.home_page.HomePage import HomePage

@pytest.mark.usefixtures("setup_and_teardown")
class Test_01_HomepageNavigation:
    @pytest.fixture(autouse= True)
    def setup(self):
        self.hp = HomePage(self.driver)
        self.hp.navigate_to_homepage()

    def test_homepage_navigation(self):
        ele = self.hp.get_home_page_title()
        # txt = ele.text
        # print(txt)
        # if ele.is_displayed():
        #     assert True
        # else:
        #     assert False
        assert ele.is_displayed()

