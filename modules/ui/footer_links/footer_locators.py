from selenium.webdriver.common.by import By

#footer links
link_contact_us = (By.PARTIAL_LINK_TEXT,"Contact us")
text_box_full_name = (By.CSS_SELECTOR,"input#FullName")
text_box_email = (By.CSS_SELECTOR,"input#Email")
text_box_enquiry =(By.CSS_SELECTOR,"textarea#Enquiry")
message_enquiry_submitted_successfully = (By.CSS_SELECTOR,"div.result")
button_enquiry_submit = (By.XPATH,"//button[@name='send-email']")
message_error_full_name = (By.CSS_SELECTOR,"span#FullName-error")
message_error_email = (By.CSS_SELECTOR,"span#Email-error")
message_error_enquiry = (By.CSS_SELECTOR,"span#Enquiry-error")


link_compare_products =(By.PARTIAL_LINK_TEXT,"Compare products list")
title_compare_products_page = (By.XPATH,"//h1")


link_new_products = (By.PARTIAL_LINK_TEXT,"New products")
title_new_products_page =(By.XPATH,"//h1")


link_news = (By.PARTIAL_LINK_TEXT,"News")
title_news_page =(By.XPATH,"//h1")