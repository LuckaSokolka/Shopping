from selenium.webdriver.common.by import By


class Driver:

    driver_path = "selenium_projects/drivers/chromedriver.exe"


class Login_zalando:

    url_homepage = "https://www.zalando-lounge.cz"
    first_page = "https://www.zalando-lounge.cz/#/"
    COOKIES = (By.XPATH, '//*[@id="uc-btn-accept-banner"]')
    LOGIN_BUTTON_LOUNGE = (By.XPATH, '//button[@type="button"]')
    LOGIN_VIA_GOOGLE = (By.XPATH, '//*[@id="sso-login-google"]/div')
    xpath_login_via_zalando_lounge = '//*[@id="sso-login-lounge"]'
    xpath_login_via_facebook = '//*[@id="sso-login-facebook"]/div/span'
    # xpath_login_via_zalando_lounge = '//*[@id="react-root-form"]/div/div/div/div[2]/div/div/div[2]/div/div/div/div/div[1]/div/div/div/button'
    xpath_do_kosiku = "//*[text()='Do košíku']"
    ADD_TO_CART = (By.XPATH, '//*[@id="addToCartButton"]/button')


class Google_login:

    # data for google login with selenium from html protocol

    # with visible screen
    # xpath_email_input = '//*[@id="identifierId"]'
    EMAIL_INPUT = (By.XPATH, '//*[@id="identifierId"]')
    NEXT_BUTTON_EMAIL = (By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    NEXT_BUTTON_PASSWORD = (By.XPATH, '//*[@id="passwordNext"]/div/button/span')
    xpath_choose_account = '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[1]'
    CHOOSE_ANOTHER_ACCOUNT = (
        By.XPATH,
        '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div',
    )

    # with headless
    """
    xpath_email_input = "/html/body/div/div[2]/div[2]/div[1]/form/div/div/div/div/div/input[1]"
    xpath_next_button_email = "/html/body/div/div[2]/div[2]/div[1]/form/div/div/input"
    xpath_password_input = "/html/body/div[1]/div[2]/div/div[2]/form/span/div/div[2]/input"
    xpath_next_button_password = "/html/body/div[1]/div[2]/div/div[2]/form/span/div/input[2]"
    """

    # zalando
    # xpath_email_input = '//*[@id="form-email"]'
    # xpath_password_input = '//*[@id="form-password"]'
    # xpath_next_button_password = '//*[@id="react-root-content"]/div/div[2]/div/div[2]/div/div/div/form/button'

    # facebook
    # xpath_email_input = '//*[@id="email"]'
    # xpath_password_input = '//*[@id="pass"]'
    # xpath_next_button_password = '//*[@id="u_0_0_pQ"]'
