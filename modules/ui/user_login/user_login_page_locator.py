from selenium.webdriver.common.by import By
#locators
link_login =(By.CSS_SELECTOR,"a.ico-login")
text_box_email_id =(By.CSS_SELECTOR,"input#Email")
text_box_password =(By.CSS_SELECTOR,"input#Password")
button_login = (By.XPATH,"//button[contains(text(),'Log in')]")
link_log_out = (By.CSS_SELECTOR,"a.ico-logout")

#messages_locators
warning_email_error =(By.CSS_SELECTOR,"span#Email-error")
warning_invalid_credentials = (By.CSS_SELECTOR,"div.message-error.validation-summary-errors")
