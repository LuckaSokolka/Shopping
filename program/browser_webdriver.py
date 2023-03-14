import time
import undetected_chromedriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.pages_locators import Google_login


class Browser:
    """
    the class imitating human behavior on the page using selenium
    in this file WebDriverWait is used, in browser.py time.sleep()
    """

    browser, service = None, None

    def __init__(self, driver: str):

        self.service = Service(driver)
        self.options = (
            undetected_chromedriver.ChromeOptions()
        )  # next solution chromedriver.ChromeOptions()
        self.options.headless = False
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--profile-directory=Default")
        self.options.add_argument("--ignore-certificate-errors")
        self.options.add_argument("--disable-plugins-discovery")
        self.options.add_argument(
            "--user-data-dir=C:/Users/lucie/AppData/Local/Google/Chrome/User Data/Profile 1/"
        )
        # self.options.add_argument("--incognito")
        self.options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        )
        # self.options.add_argument("user_agent=DN")
        self.browser = undetected_chromedriver.Chrome(
            service=self.service, options=self.options
        )
        self.browser.delete_all_cookies()

    def open_page(self, url: str):
        self.browser.get(url)
        time.sleep(3)

    def maximize_window(self):
        self.browser.maximize_window()
        time.sleep(3)

    def current_url(self):
        return self.browser.current_url

    def find_element(self, by: By, value: str):
        timeout = 120
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        timeout = 60
        field = WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        field.send_keys(text)

    def click_button(self, by: By, value: str):
        timeout = 60
        button = WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        button.click()
        time.sleep(4)

    def switch_window(self):
        handles = self.browser.window_handles
        for i in handles:
            self.browser.switch_to.window(i)
        time.sleep(10)

    def screenshot(self):
        self.browser.save_screenshot("screenshot.png")

    def login_through_google(self, email: str, password: str):

        self.add_input(*Google_login.EMAIL_INPUT, text=email)
        self.click_button(*Google_login.NEXT_BUTTON_EMAIL)
        self.add_input(*Google_login.PASSWORD_INPUT, text=password)
        self.click_button(*Google_login.NEXT_BUTTON_PASSWORD)

    def scroll_down(self, by: By, value: str):
        ActionChains(self.browser).move_to_element(
            self.browser.find_element(by=by, value=value)
        ).perform()
        time.sleep(5)

    def refresh_page(self):
        self.browser.refresh()

    def element_is_finded(self, by: By, value: str):

        try:
            return self.browser.find_element(by=by, value=value) != None
        except:
            return False
