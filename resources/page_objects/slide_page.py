from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


AS_SHOWN_PRICE = 'p.as-shown'
MODEL_NAME = 'p.model'
MSRP_PRICE = 'p.short-description'
BUILD_LINK = 'a[href*="/configurator/build"]'
OFFERS_LINK = 'a[href*="/local-specials/"]'
CAR_SLIDE_IMAGE = 'div.vehicle-image-wrapper  > img'


class CarSlide(object):
    def __init__(self, parent_element, explicit_wait=20):
        self.element = parent_element
        self.wait_driver = WebDriverWait(self.element, explicit_wait)
        self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, CAR_SLIDE_IMAGE)))
        self.model_name = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, MODEL_NAME))).text
        self.model_price = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, MSRP_PRICE))).text
        self.build_link = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, BUILD_LINK)))
        self.offers_link = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, OFFERS_LINK)))
        self.as_shown_price = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, AS_SHOWN_PRICE))).text
        self.msrp_price = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, MSRP_PRICE))).text

    @property
    def top_level_text(self):
        try:
            return self.element.find_element(By.CSS_SELECTOR, 'span.top-label').text
        except Exception:
            return ''

INFO_TXT = 'div.menu-text > span'
SHP_CAR_SLIDE_IMAGE = 'picture'

class ShoppingCarSlide(object):
    def __init__(self, parent_element, explicit_wait=10):
        self.wait_driver = WebDriverWait(parent_element, explicit_wait)
        self.info_txt = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, INFO_TXT))).text
        self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, SHP_CAR_SLIDE_IMAGE)))
