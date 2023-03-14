import time
import importlib
from credentials.credentials import MyCredentials
from configuration.product import data_product
from locators.pages_locators import Driver
from locators.pages_locators import Login_zalando
from locators.pages_locators import Google_login
from configuration.music_notice.notice_music import Notice
from program.browser_webdriver import Browser


class Zalando_lounge:
    """
    class for opening zalando_lounge.cz
    logging in and opening the page with the item
    waits for the item to become available and adds it to the cart
    """

    def start(self):

        music = Notice()
        importlib.reload(data_product)  # reload cache

        # open page
        browser = Browser(Driver.driver_path)  # chrome driver
        browser.open_page(Login_zalando.url_homepage)
        print(browser.current_url())
        # browser.maximize_window() # if browser_webdriver don´t have argument self.options.add_argument("--start-maximized")
        print("• The page is loaded")
        browser.screenshot()

        # cookies
        # browser.click_button(*Login_zalando.COOKIES)

        if browser.current_url() == Login_zalando.first_page:

            # login zalando
            browser.click_button(*Login_zalando.LOGIN_BUTTON_LOUNGE)
            # login to zalando via google account
            browser.click_button(*Login_zalando.LOGIN_VIA_GOOGLE)
            browser.switch_window()  # switch to window google login
            time.sleep(5)
            print("switch to google")
            browser.screenshot()
            browser.click_button(*Google_login.CHOOSE_ANOTHER_ACCOUNT)
            time.sleep(5)
            browser.login_through_google(MyCredentials.GMAIL, MyCredentials.PASSWORD)

            browser.switch_window()  # switch back to zalando
            print("• Login was successful")

            # after logging in, it is possible to open the page with the item
            browser.open_page(data_product.url_product)
            print("• The page with item was loaded")
            browser.scroll_down(*Login_zalando.ADD_TO_CART)

            while True:
                # if find item in reservation, refresh page
                if (
                    browser.element_is_finded(*data_product.xpath_item_is_reserved)
                    == True
                ):
                    print("• The product is reserved")
                    browser.refresh_page()
                    time.sleep(1)

                elif (
                    browser.element_is_finded(*data_product.xpath_item_is_sold_out)
                    == True
                ):
                    music.play()
                    print("• The product is sold out")
                    break

                # if item isn't reserved or sold out, scroll to button, add to card
                else:
                    browser.click_button(*data_product.xpath_size)
                    browser.click_button(*Login_zalando.ADD_TO_CART)
                    print("• The product is added to the cart")
                    music.play()
                    break
            browser.close_browser()

        else:
            # after logging in, it is possible to open the page with the item
            browser.open_page(data_product.url_product)
            print("• The page with item was loaded")
            browser.scroll_down(*Login_zalando.ADD_TO_CART)

            while True:
                # if find item in reservation, refresh page
                if (
                    browser.element_is_finded(*data_product.xpath_item_is_reserved)
                    == True
                ):
                    print("• The product is reserved")
                    browser.refresh_page()
                    time.sleep(1)

                elif (
                    browser.element_is_finded(*data_product.xpath_item_is_sold_out)
                    == True
                ):
                    music.play()
                    print("• The product is sold out")
                    break

                # if item isn't reserved or sold out, scroll to button, add to card
                else:
                    browser.click_button(*data_product.xpath_size)
                    browser.click_button(*Login_zalando.ADD_TO_CART)
                    print("• The product is added to the cart")
                    music.play()
                    break
            browser.close_browser()
