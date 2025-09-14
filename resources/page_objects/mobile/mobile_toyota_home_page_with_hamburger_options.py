from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy

TOYOTA_LOGO_BTN = 'a[data-di-id="#mobile-logo"]'
USER_BTN = 'button[aria-label="user icon"]'
HAMBURGER_BTN = 'button[aria-label="hamburger"]'
VEHIC_BTN = 'label[data-aa-link-type="button"][for="1-vehicles"] > h2'   
SHOP_BTN = 'label[data-aa-link-type="button"][for="1-shopping"] > h2'
OWNERS_BTN = 'label[data-aa-link-type="button"][for="1-owners"] > h2'
BUILD_PRICE_BTN = 'li[class*="build"] > a[href="/configurator/"]'


class MobileToyotaHomePagewithHamburgerOptions(object):
    def __init__(self, driver, explicit_wait=20):
        self.driver = driver
        self.wait_driver = WebDriverWait(self.driver, explicit_wait)
        
        self.toyota_logo_btn = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.CSS_SELECTOR, TOYOTA_LOGO_BTN)))
