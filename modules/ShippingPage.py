from faker import Faker
from selenium.webdriver.common.by import By
from base.SeleniumBaseClass import SeleniumBase

#locators


textbox_first_name = (By.CSS_SELECTOR,"input#BillingNewAddress_FirstName")
textbox_last_name = (By.CSS_SELECTOR,"input#BillingNewAddress_LastName")
textbox_email = (By.CSS_SELECTOR,"input#BillingNewAddress_Email")
textbox_company = (By.CSS_SELECTOR,"input#BillingNewAddress_Company")
dropdown_list_country = (By.CSS_SELECTOR,"select#BillingNewAddress_CountryId")
dropdown_list_state = (By.CSS_SELECTOR,"select#BillingNewAddress_StateProvinceId")
textbox_city = (By.CSS_SELECTOR,"input#BillingNewAddress_City")
textbox_address1 = (By.CSS_SELECTOR,"input#BillingNewAddress_Address1")
textbox_address2 = (By.CSS_SELECTOR,"input#BillingNewAddress_Address2")
textbox_zip = (By.CSS_SELECTOR,"input#BillingNewAddress_ZipPostalCode")
textbox_phone = (By.CSS_SELECTOR,"input#BillingNewAddress_PhoneNumber")
textbox_fax_number = (By.CSS_SELECTOR,"input#BillingNewAddress_FaxNumber")

button_submit = (By.XPATH,"//span[@id='shipping-please-wait']/preceding-sibling::button")
button_checkout_guest =(By.XPATH,"//button[text()='Checkout as Guest']")

#Shipping Methods
radio_shipping_method_ground=(By.CSS_SELECTOR,"input#shippingoption_0")
radio_shipping_method_nextdayair=(By.CSS_SELECTOR,"input#shippingoption_1")
radio_shipping_method_secondayair=(By.CSS_SELECTOR,"input#shippingoption_0")

#Payment_methods

radio_check_money_order = (By.CSS_SELECTOR,"input#paymentmethod_0")
radio_creditcard = (By.CSS_SELECTOR,"input#paymentmethod_1")

link_return_to_checkout = (By.XPATH,"//span[@id='shipping-method-please-wait']/preceding::a[@href = '#']")
button_continue = (By.XPATH,"//button[text()='Continue']")
button_next_shipping_method = (By.XPATH,"//button[@class='button-1 shipping-method-next-step-button']")
button_next_payment_method = (By.XPATH,"//button[@class='button-1 payment-method-next-step-button']")
button_next_step_info = (By.XPATH,"//button[@class='button-1 payment-info-next-step-button']")

button_continue_shopping = (By.XPATH,"//button[@name='continueshopping']")
button_confirm = (By.XPATH,"//button[text()='Confirm']")
message_shopping_success =(By.XPATH,"//strong[text()='Your order has been successfully processed!']")


billing_checkout_page = (By.CSS_SELECTOR,"h1")
button_continue_with_the_shipping_address = (By.CSS_SELECTOR,"button[name ='save']")
#data
country = "United States"
state = "Hawaii"
class Shipping(SeleniumBase):
    def __init__(self,driver):
        super().__init__(driver=driver)
        self.fk = Faker()

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


    def click_on_button_continue_with_the_shipping_address(self):
        self.click_element(button_continue_with_the_shipping_address)