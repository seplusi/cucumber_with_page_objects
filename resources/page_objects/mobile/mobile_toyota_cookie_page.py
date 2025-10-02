from selenium.webdriver.support import expected_conditions as EC
from resources.page_element import PageElement
from selenium.webdriver.support.wait import WebDriverWait
import yaml


class MobileToyotaCookiesPage(object):
    def __init__(self, driver, explicit_wait=20):
        self.driver = driver
        # Get all elements locators
        with open('resources/page_objects_definitions/mobile_toyota_cookies_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        for obj_def in self.data[self.__class__.__name__]:
            name = list(obj_def.keys())[0]
            locator_type = obj_def[name]['Locator-Type']
            locator_value = obj_def[name]['Locator-Value']
            wait = explicit_wait if obj_def[name]['Wait-For-Loaded'] else None
            setattr(self, list(obj_def.keys())[0], PageElement(locator_type, locator_value, self.driver, wait))
        self.wait_driver = WebDriverWait(self.driver, explicit_wait)

    def accept(self):
        self.accept_btn.web_element.click()

    def cookie_banner_not_displayed_after_some_time(self):
        assert self.wait_driver.until_not(EC.visibility_of_element_located((self.cookie_banner.locator)))
