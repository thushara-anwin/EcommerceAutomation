
from faker import Faker
from base.SeleniumBaseClass import SeleniumBase
from modules.ui.shipping_page.shipping_page_locators import *
from modules.ui.shipping_page.shipping_page_data import *


class Shipping(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)
        self.fk = Faker()
        #self.rd = random.randint(1,13)

    def click_on_button_continue_shopping(self):
        self.click_element(button_continue_shopping)


    def enter_first_name(self):

        self.fk = Faker()
        f_name = self.fk.first_name()
        self.enter_value(f_name,textbox_first_name)

    def enter_last_name(self):
        l_name = self.fk.last_name_male()
        self.enter_value(l_name,textbox_last_name)

    def enter_email(self):
        email = self.fk.email()
        self.enter_value(email,textbox_email)

    def enter_company(self):
        company = self.fk.company()
        self.enter_value(company, textbox_company)

    def enter_country(self):
        self.enter_dropdown_value(country,dropdown_list_country)

    def enter_state(self):
        self.enter_dropdown_value(state,dropdown_list_state)

    def enter_city(self):
        city = self.fk.city()
        self.enter_value(city,textbox_city)

    def enter_address1(self):
        address1 = self.fk.building_number()
        self.enter_value(address1,textbox_address1)

    def enter_address2(self):
        address2 = self.fk.building_number()
        self.enter_value(address2,textbox_address2)


    def enter_zip(self):
        zip = self.fk.postalcode()
        self.enter_value(zip,textbox_zip)

    def enter_phone(self):
        phone_number = self.fk.phone_number()
        self.enter_value(phone_number,textbox_phone)

    def enter_fax(self):
        fax = self.fk.building_number()
        self.enter_value(fax,textbox_fax_number)

    def click_on_radio_shipping_method_ground(self):
        self.click_element(radio_shipping_method_ground)

    def click_on_radio_shipping_method_nextdayair(self):
        self.click_element(radio_shipping_method_nextdayair)

    def click_on_radio_shipping_method_secondayair(self):
        self.click_element(radio_shipping_method_secondayair)

    def click_on_button_continue(self):
        self.click_element(button_continue)

    def click_on_button_next_shipping_method(self):
        self.click_element(button_next_shipping_method)

    def click_on_button_next_payment_method(self):
        self.click_element(button_next_payment_method)

    def click_on_button_next_step_info(self):
        self.click_element(button_next_step_info)

    def click_on_button_confirm(self):
        self.click_element(button_confirm)

    def click_on_button_checkout_guest(self):
        self.click_element(button_checkout_guest)




    def click_on_radio_check_money_order(self):
        self.click_element(radio_check_money_order)
        self.click_on_button_next_payment_method()

    def click_on_radio_creditcard(self):
        self.click_element( radio_creditcard)
        self.click_on_button_next_payment_method()

    def guest_shipping_address(self):
        self.enter_first_name()
        self.enter_last_name()
        self.enter_email()
        self.enter_company()
        self.enter_country()
        self.enter_state()
        self.enter_city()
        self.enter_address1()
        self.enter_address2()
        self.enter_zip()
        self.enter_phone()
        self.enter_fax()

    def returning_customer_shipping_address(self):
        self.enter_country()
        self.enter_state()
        self.enter_city()
        self.enter_address1()
        self.enter_address2()
        self.enter_zip()
        self.enter_phone()
        self.enter_fax()
        self.click_on_button_continue()


    def shipping_method(self,option):
        if option == 'ground':
            self.click_on_radio_shipping_method_ground()
        elif option == 'next_day':
            self.click_on_radio_shipping_method_nextdayair()
        elif option == 'second_day':
            self.click_on_radio_shipping_method_secondayair()
        self.click_on_button_next_shipping_method()

    def get_message_shopping_success(self):
        element = self.get_element(message_shopping_success)
        return element

    def get_to_checkout_page(self):
        element = self.get_element(billing_checkout_page)
        return element


    def get_continue_with_the_shipping_address(self):
        element = self.get_element(button_continue_with_the_shipping_address)
        return element
    def click_on_button_continue_with_the_shipping_address(self):
        self.click_element(button_continue_with_the_shipping_address)

    # def enter_card_expiration_date(self):
    #     expire_month = str(self.rd)
    #     self.enter_dropdown_value(expire_month,text_box_card_expiration_month )
    #     expire_year = self.fk.year()
    #     self.enter_dropdown_value(expire_year,text_box_card_expiration_year)

    def add_credit_card_details(self):
        self.enter_dropdown_value(card_type,text_box_card_type)
        self.enter_value(card_holder_name,text_box_card_holder_name)
        card_number = self.fk.credit_card_number()
        self.enter_value(card_number,text_box_card_number)
        self.enter_dropdown_value(expire_month, text_box_card_expiration_month)
        self.enter_dropdown_value(expire_year, text_box_card_expiration_year)
        self.enter_value(card_code,text_box_card_code)
        self.click_element(button_continue_credit_card_page)

    def title_order_number(self):
        element = self.get_element(order_number_locator)
        return element




