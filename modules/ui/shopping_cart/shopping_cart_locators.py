from selenium.webdriver.common.by import By
#locators
link_shopping_cart = (By.PARTIAL_LINK_TEXT,"Shopping cart")
items_list = (By.CSS_SELECTOR,"button.remove-btn")
check_box_terms_of_service =(By.CSS_SELECTOR,"input#termsofservice")
message_shopping_cart_empty = (By.XPATH,"//div[contains(text(),'Your Shopping Cart is empty!')]")
button_checkout = (By.CSS_SELECTOR,"button#checkout")