from selenium.webdriver.common.by import By
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

#cret card details
text_box_card_type = (By.CSS_SELECTOR, "select#CreditCardType")
text_box_card_holder_name = (By.CSS_SELECTOR, "input#CardholderName")
text_box_card_number = (By.CSS_SELECTOR, "input#CardNumber")
text_box_card_expiration_month = (By.CSS_SELECTOR, "select#ExpireMonth")
text_box_card_expiration_year = (By.CSS_SELECTOR, "select#ExpireYear")
text_box_card_code = (By.CSS_SELECTOR, "input#CardCode")
button_continue_credit_card_page = (By.XPATH, "//button[@onclick='if (!window.__cfRLUnblockHandlers) "
                                                  "return false; PaymentInfo.save()']")
