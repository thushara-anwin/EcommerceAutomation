from modules.ui.user_registration.registration_page_locators import *
from modules.ui.user_registration.registration_page_data import *

from base.SeleniumBaseClass import SeleniumBase
from faker import Faker
import random


class Registration(SeleniumBase):

    def __init__(self,driver):
        super().__init__(driver=driver)
        self.fk = Faker()
        self.rd = random.randint(1,28)

    def click_on_link_registration(self):
        self.click_element(link_registration)

    def click_on_radio_male(self):
       self.click_element(radio_male)

    def click_on_radio_female(self):
        self.click_element(radio_female)

    def enter_value_to_text_box_fname(self):
        fname = self.fk.first_name()
        self.enter_value(fname,text_box_fname)

    def enter_value_to_text_box_lname(self):
        lname = self.fk.last_name()
        self.enter_value(lname, text_box_lname)

    def enter_date_of_birth(self):
        date = str(self.rd)
        self.enter_dropdown_value(date,dropdown_day)
        month = self.fk.month_name()
        self.enter_dropdown_value(month, dropdown_month)
        year = self.fk.year()
        self.enter_dropdown_value(year, dropdown_year)

    def enter_value_to_text_box_email(self):
        email = self.fk.email()
        self.enter_value(email, text_box_email)

    def enter_value_to_text_box_company(self):
        company = self.fk.company()
        self.enter_value(company, text_box_company)

    def click_on_check_box_newsletter(self):
        self.click_element(check_box_newsletter)

    def enter_value_to_text_box_pswd_and_confirm_pswd(self):
        pswd = self.fk.password()
        self.enter_value(pswd, text_box_pswd)
        self.enter_value(pswd, text_box_confirm_pswd)

    def click_on_button_register(self):
        self.click_element(button_register)

    def get_message_registration_completed(self):
        element = self.get_element(message_registration_completed)
        return element

    # registration_for returning user

    def returning_user_registration(self):
        self.click_on_link_registration()
        self.click_element(radio_female)
        self.enter_value(fname, text_box_fname)
        self.enter_value(lname, text_box_lname)
        self.enter_dropdown_value(date,dropdown_day)
        self.enter_dropdown_value(month, dropdown_month)
        self.enter_dropdown_value(year, dropdown_year)
        self.enter_value(email_user, text_box_email)
        self.enter_value(company, text_box_company)
        self.enter_value(pswd, text_box_pswd)
        self.enter_value(pswd, text_box_confirm_pswd)
        self.click_element(button_register)


    # def returning_user2_registration(self):
    #     self.click_on_link_registration()
    #     self.click_element(radio_female)
    #     self.enter_value(fname, text_box_fname)
    #     self.enter_value(lname, text_box_lname)
    #     self.enter_dropdown_value(date,dropdown_day)
    #     self.enter_dropdown_value(month, dropdown_month)
    #     self.enter_dropdown_value(year, dropdown_year)
    #     self.enter_value(email_user2, text_box_email)
    #     self.enter_value(company, text_box_company)
    #     self.enter_value(pswd, text_box_pswd)
    #     self.enter_value(pswd, text_box_confirm_pswd)
    #     self.click_element(button_register)
    #
    #
    # def returning_user3_registration(self):
    #     self.click_on_link_registration()
    #     self.click_element(radio_female)
    #     self.enter_value(fname, text_box_fname)
    #     self.enter_value(lname, text_box_lname)
    #     self.enter_dropdown_value(date,dropdown_day)
    #     self.enter_dropdown_value(month, dropdown_month)
    #     self.enter_dropdown_value(year, dropdown_year)
    #     self.enter_value(email_user3, text_box_email)
    #     self.enter_value(company, text_box_company)
    #     self.enter_value(pswd, text_box_pswd)
    #     self.enter_value(pswd, text_box_confirm_pswd)
    #     self.click_element(button_register)
    #
    #
    #











