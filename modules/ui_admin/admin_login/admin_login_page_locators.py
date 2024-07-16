from selenium.webdriver.common.by import By
#locators

textbox_admin_email = (By.ID,"Email")
textbox_admin_password = (By.ID,"Password")
btn_login = (By.XPATH,"//button[@type='submit']")
admin_page_title = (By.XPATH,"//h1[contains(text(),'Dashboard')]")
invalid_user_warning =(By.XPATH,"//li")
invalid_password= (By.XPATH,"//li")
no_credentials = (By.CSS_SELECTOR,"span#Email-error")
btn_logout = (By.LINK_TEXT,"Logout")