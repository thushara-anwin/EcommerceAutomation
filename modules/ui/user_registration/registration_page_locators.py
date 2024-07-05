from selenium.webdriver.common.by import By
#locators

link_registration = (By.CSS_SELECTOR,"a.ico-register")
radio_male = (By.CSS_SELECTOR,"input#gender-male")
radio_female = (By.CSS_SELECTOR,"input#gender-female")
text_box_fname = (By.CSS_SELECTOR,"input#FirstName")
text_box_lname = (By.CSS_SELECTOR,"input#LastName")
dropdown_day = (By.CSS_SELECTOR,"select[name =DateOfBirthDay]")
dropdown_month = (By.CSS_SELECTOR,"select[name =DateOfBirthMonth]")
dropdown_year = (By.CSS_SELECTOR,"select[name =DateOfBirthYear]")
text_box_email = (By.CSS_SELECTOR,"input#Email")
text_box_company = (By.CSS_SELECTOR,"input#Company")
check_box_newsletter =(By.CSS_SELECTOR,"input#Newsletter")
text_box_pswd = (By.CSS_SELECTOR,"input#Password")
text_box_confirm_pswd = (By.CSS_SELECTOR,"input#ConfirmPassword")
button_register = (By.CSS_SELECTOR,"button#register-button")
message_registration_completed = (By.CSS_SELECTOR,"div.result")