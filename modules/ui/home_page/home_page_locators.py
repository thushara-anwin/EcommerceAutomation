from selenium.webdriver.common.by import By

# homepage _locators
textbox_search =(By.ID,"small-searchterms")
btn_search=(By.XPATH,"//button[@type='submit']")

title_locator =(By.XPATH,"//title")
welcome_message_locator =(By.XPATH,"//div[@class='topic-block-title']/h2")

link_login =(By.LINK_TEXT,"Log in")
link_register =(By.LINK_TEXT,"Register")
link_wishlist =(By.XPATH,"//span[text()='Wishlist']")
valid_product_locator=(By.XPATH,"//button[text()='Add to cart']")
no_product_message=(By.XPATH,"//div[@class='no-result']")
min_length_warning_locator =(By.XPATH,"//div[@class='warning']")


#product_category_locators
link_computers= (By.PARTIAL_LINK_TEXT,"Computers")
link_desktops = (By.PARTIAL_LINK_TEXT,"Desktops")
link_notebooks = (By.PARTIAL_LINK_TEXT,"notebooks")
link_software  = (By.PARTIAL_LINK_TEXT,"Software")




link_electronics= (By.PARTIAL_LINK_TEXT,"Electronics")
link_camera_and_photo = (By.PARTIAL_LINK_TEXT,"Camera & photo")
link_cell_phones =(By.PARTIAL_LINK_TEXT,"Cell phones")
link_electronics_others =(By.PARTIAL_LINK_TEXT,"Cell phones")


link_apparel= (By.PARTIAL_LINK_TEXT,"Apparel")
link_shoes = (By.PARTIAL_LINK_TEXT,"Shoes")
link_clothing =(By.PARTIAL_LINK_TEXT,"Clothing")
link_accessories  =(By.PARTIAL_LINK_TEXT,"Accessories")



link_digital_downloads= (By.PARTIAL_LINK_TEXT,"Digital downloads")
link_books= (By.PARTIAL_LINK_TEXT,"Books")
link_jewelry= (By.PARTIAL_LINK_TEXT,"Jewelry")
link_gift_cards= (By.PARTIAL_LINK_TEXT,"Gift Cards")
computer_products_page_title = (By.XPATH,"//h1[text()='Computers']")
electronics_products_page_title = (By.XPATH,"//h1[text()='Electronics']")
apparel_products_page_title = (By.XPATH,"//h1[text()='Apparel']")
digital_downloads_products_page_title = (By.XPATH,"//h1[text()='Digital downloads']")
books_products_page_title = (By.XPATH,"//h1[text()='Books']")
jewelry_products_page_title = (By.XPATH,"//h1[text()='Jewelry']")
gift_card_products_page_title = (By.XPATH,"//h1[text()='Gift Cards']")

#messages
message_product_added_locator = (By.CSS_SELECTOR,"p.content")
title_home_page = (By.XPATH,"//title")

