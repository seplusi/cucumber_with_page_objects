from selenium.webdriver.support.wait import WebDriverWait
import yaml
from resources.page_element import PageElement


class MobileToyotaHomePage(object):
    def __init__(self, driver, explicit_wait=20):
        self.driver = driver
        # Get all elements locators
        with open('resources/page_objects_definitions/mobile_toyota_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        for obj_def in self.data[self.__class__.__name__]:
            name = list(obj_def.keys())[0]
            locator_type = obj_def[name]['Locator-Type']
            locator_value = obj_def[name]['Locator-Value']
            wait = explicit_wait if obj_def[name]['Wait-For-Loaded'] else None
            setattr(self, list(obj_def.keys())[0], PageElement(locator_type, locator_value, self.driver, wait))
        self.wait_driver = WebDriverWait(self.driver, explicit_wait)
