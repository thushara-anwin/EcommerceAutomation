from selenium.webdriver.common.by import By

link_my_account = (By.XPATH,"//a[@class='ico-account']")

link_customer_info = (By.PARTIAL_LINK_TEXT,"Customer info")
title_customer_info = (By.XPATH,"//h1")

link_addresses = (By.PARTIAL_LINK_TEXT,"Addresses")
title_addresses = (By.XPATH,"//h1")

link_orders = (By.PARTIAL_LINK_TEXT,"Orders")
title_orders = (By.XPATH,"//h1")

link_downloadable_products = (By.PARTIAL_LINK_TEXT,"Downloadable products")
title_downloadable_products= (By.XPATH,"//h1")

link_back_in_stock_subscriptions = (By.PARTIAL_LINK_TEXT,"Back in stock subscriptions")
title_back_in_stock_subscriptions = (By.XPATH,"//h1")

link_reward_points = (By.PARTIAL_LINK_TEXT,"Reward points")
title_reward_points = (By.XPATH,"//h1")
text_current_rewards_balance = (By.CSS_SELECTOR,"div.current-balance")

link_change_password = (By.PARTIAL_LINK_TEXT,"Change password")
title_change_password = (By.XPATH,"//h1")

link_my_product_reviews = (By.PARTIAL_LINK_TEXT,"My product reviews")
title_my_product_reviews = (By.XPATH,"//h1")
