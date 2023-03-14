from selenium.webdriver.common.by import By

url_product = 'https://www.zalando-lounge.cz/campaigns/ZZO24UH/categories/28977875/articles/PU141I03S-J11'
xpath_item_is_reserved = (By.XPATH, '//*[@id="article-size-section"]/div[2]/div[3]/div[2]//*[text()="Rezervováno"]')
xpath_item_is_sold_out = (By.XPATH, '//*[@id="article-size-section"]/div[2]/div[3]/div[2]//*[text()="Vyprodáno"]')
xpath_size = (By.XPATH, "//*[text()='S']")
