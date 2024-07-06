from base.SeleniumBaseClass import SeleniumBase
from modules.ui.my_account.my_account_locators import *


class MyAccount(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)

    def click_on_link_my_account(self):
        self.click_element(link_my_account)

    def get_customer_info_title(self):
        self.click_element(link_customer_info)
        element = self.get_element(title_customer_info)
        return element

    def get_customer_addresses(self):
        self.click_element(link_addresses)
        element = self.get_element(title_addresses)
        return element

    def get_orders(self):
        self.click_element(link_orders)
        element = self.get_element(title_orders)
        return element

    def get_downloadable_products(self):
        self.click_element(link_downloadable_products)
        element = self.get_element(title_downloadable_products)
        return element

    def get_back_in_stock_subscriptions(self):
        self.click_element(link_back_in_stock_subscriptions)
        element = self.get_element(title_back_in_stock_subscriptions)
        return element

    def get_reward_points(self):
        self.click_element(link_reward_points)
        element = self.get_element(title_reward_points)
        return element

    def get_current_rewards_balance(self):
        element = self.get_element(text_current_rewards_balance)
        return element

    def get_change_password(self):
        self.click_element(link_change_password)
        element = self.get_element(title_change_password)
        return element

    def get_my_product_reviews(self):
        self.click_element(link_my_product_reviews)
        element = self.get_element(title_my_product_reviews)
        return element