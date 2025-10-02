import yaml
from selenium.webdriver.support import expected_conditions as EC
from resources.page_objects.common.page_object_common_class import PageObjectCommonClass
from selenium.webdriver.support.wait import WebDriverWait


class ToyotaCookiesPage(PageObjectCommonClass):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver)
        # Get all elements locators
        with open('resources/page_objects_definitions/toyota_cookies_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        self._load_page_object(explicit_wait)
    
    def accept(self):
        self.accept_btn.web_element.click()
    
    def cookie_banner_not_displayed_after_some_time(self, timeout):
        assert WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((self.cookie_banner.locator)))

