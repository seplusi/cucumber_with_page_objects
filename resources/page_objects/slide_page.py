import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from resources.page_objects.common.page_object_common_class import PageObjectCommonClass


class CarSlide(PageObjectCommonClass):
    def __init__(self, parent_element, explicit_wait=20):
        super().__init__(parent_element)
        # Get all elements locators
        with open('resources/page_objects_definitions/slide_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        self._load_page_object(explicit_wait)

    @property
    def get_safe_top_level_text(self):
        try:
            return self.top_level_text.web_element.text
        except Exception:
            return ''

INFO_TXT = 'div.menu-text > span'
SHP_CAR_SLIDE_IMAGE = 'picture'

class ShoppingCarSlide(PageObjectCommonClass):
    def __init__(self, parent_element, explicit_wait=10):
        super().__init__(parent_element)
        # Get all elements locators
        with open('resources/page_objects_definitions/slide_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        self._load_page_object(explicit_wait)
#        self.wait_driver = WebDriverWait(parent_element, explicit_wait)
#        self.info_txt = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, INFO_TXT))).text
#        self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, SHP_CAR_SLIDE_IMAGE)))
