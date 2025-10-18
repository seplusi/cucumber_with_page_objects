from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from resources.page_objects.common.page_object_common_class import PageObjectCommonClass
import yaml

USER_BTN = 'button[aria-label="user icon"]'
HAMBURGER_BTN = 'button[aria-label="hamburger"]'
VEHIC_BTN = 'label[data-aa-link-type="button"][for="1-vehicles"] > h2'   
SHOP_BTN = 'label[data-aa-link-type="button"][for="1-shopping"] > h2'
OWNERS_BTN = 'label[data-aa-link-type="button"][for="1-owners"] > h2'
BUILD_PRICE_BTN = 'li[class*="build"] > a[href="/configurator/"]'


class MobileToyotaHomePagewithHamburgerOptions(PageObjectCommonClass):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver)
        with open('resources/page_objects_definitions/mobile_toyota_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        self._load_page_object(explicit_wait)