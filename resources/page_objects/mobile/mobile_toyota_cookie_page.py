from appium.webdriver.common.appiumby import AppiumBy
from resources.page_objects.toyota_cookie_page import ToyotaCookiesPage


class MobileToyotaCookiesPage(ToyotaCookiesPage):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver, explicit_wait, AppiumBy)
