from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

COOKIE_BANNER = 'div[class="cookie-banner cookie-banner--default visible"]'
ACCEPT_BTN = 'button[class="cookie-banner__accept"]'
DECLINE_BTN = 'button[class="cookie-banner__reject"]'
TITLE = 'div[class="cookie-banner__title"]'
CLOSE_BTN = 'button[aria-label="Close Cookie Banner"]'
CONTENT_TXT = 'div[class="cookie-banner__primary-content"]'


class MobileToyotaCookiesPage(object):
    def __init__(self, driver, explicit_wait=20):
        self.driver = driver
        self.wait_driver = WebDriverWait(self.driver, explicit_wait)

        try:
            self.accept_btn = self.wait_driver.until(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, ACCEPT_BTN)))
            self.decline_btn = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.CSS_SELECTOR, DECLINE_BTN)))
            self.title = self.wait_driver.until(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, TITLE)))
            self.close_btn = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.CSS_SELECTOR, CLOSE_BTN)))
            self.content_txt = self.wait_driver.until(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, CONTENT_TXT)))
        except Exception as e:
            print("cfvgh")
    
    def accept(self):
        self.accept_btn.click()
    
    def cookie_banner_not_displayed_after_some_time(self):
        assert self.wait_driver.until_not(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, COOKIE_BANNER)))
