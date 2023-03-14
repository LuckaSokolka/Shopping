class Product:
    """
    This class retrieves product information and writes it to a file.
    """

    def load_from_user(self):
        self.url = input("Url of the item in zalando_lounge.cz: ")
        self.size = input("What size from zalando-lounge do you need: ")
        self.order = input("What's the order of the item (number): ")

    def write_info_in_to_file(self):
        """
        get input from user
        """

        with open(
            "configuration/product/data_product.py", mode="w", encoding="utf-8"
        ) as file_:
            # self.url = input("Url of the item in zalando_lounge.cz: ")
            # self.size = input("What size from zalando-lounge do you need: ")
            # self.order = input("What's the order of the item (number): ")
            print("from selenium.webdriver.common.by import By", file=file_)
            print(file=file_)
            print(f"url_product = '{self.url}'", file=file_)
            print(
                f'xpath_item_is_reserved = (By.XPATH, \'//*[@id="article-size-section"]/div[2]/div[3]/div[{self.order}]//*[text()="Rezervováno"]\')',
                file=file_,
            )
            print(
                f'xpath_item_is_sold_out = (By.XPATH, \'//*[@id="article-size-section"]/div[2]/div[3]/div[{self.order}]//*[text()="Vyprodáno"]\')',
                file=file_,
            )
            print(f"xpath_size = (By.XPATH, \"//*[text()='{self.size}']\")", file=file_)
            print("\n• Product data has been entered")
