from selenium.webdriver.common.by import By

custom_t_shirt = (By.PARTIAL_LINK_TEXT,"Custom T-Shirt")
nike_tailwind_short_sleeve_running_shirt = (By.PARTIAL_LINK_TEXT,"Nike Tailwind Loose Short-Sleeve Running Shirt")
Levi_511_jeans = (By.PARTIAL_LINK_TEXT,"Levi's 511 Jeans")



custom_t_shirt_name =(By.XPATH,"//h1[text()='Custom T-Shirt']")
custom_t_shirt_price =(By.ID,"price-value-29")
custom_t_shirt_description = (By.XPATH,"//div[@class='full-description']")
custom_tshirt_code = (By.CSS_SELECTOR,"sku-29")
text_box_custom_tshirt_code =(By.CSS_SELECTOR,"input#product_attribute_12")
button_custom_tshirt_add_to_cart =(By.CSS_SELECTOR,"button#add-to-cart-button-29")
button_custom_tshirt_add_to_wishlist =(By.CSS_SELECTOR,"button#add-to-wishlist-button-29")
button_nike_tailwind_short_sleeve_running_shirt_add_to_wishlist =(By.CSS_SELECTOR,"button#add-to-wishlist-button-27")
button_Levi_511_jeans_add_to_wishlist =(By.CSS_SELECTOR,"button#add-to-wishlist-button-30")
#remove_Levi_511_jeans_from_wishlist = (By.CSS_SELECTOR,"input#removefromcart11229")
remove_Levi_511_jeans_from_wishlist = (By.CSS_SELECTOR,"button.remove-btn")
message_wishlist_empty = (By.CSS_SELECTOR,"div.no-data")

