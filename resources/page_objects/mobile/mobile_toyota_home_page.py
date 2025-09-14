import re
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from resources.page_objects.slide_page import CarSlide, ShoppingCarSlide
from resources.page_objects.toyota_home_page import ToyotaCommonHomePage
from appium.webdriver.extensions.action_helpers import ActionChains


TOYOTA_LOGO_BTN = 'a[data-di-id="#mobile-logo"]'
USER_BTN = 'button[aria-label="user icon"]'
HAMBURGER_BTN = 'button[aria-label="hamburger"]'
HOMEPAGE_CAROUSEL = 'div[data-aa-content-section="homepage hero"] ul[data-panelselect="carousel"]'
LEARN_MORE = 'div[data-aa-content-section="homepage hero"] li[class="cmp-carousel__item js_slide active"] span'
PLAY_BTN = 'div[data-aa-content-section="homepage hero"] li[class="cmp-carousel__item js_slide active"] button[class="video-control button-pause"]'
INFO_BTN = 'div[data-aa-content-section="homepage hero"] li[class="cmp-carousel__item js_slide active"] button[aria-label="info"]'
HEADING_TXT = 'div[data-aa-content-section="homepage hero"] li[class="cmp-carousel__item js_slide active"] h2[class="title heading-02"]'
SUBHEAD_TXT = 'div[data-aa-content-section="homepage hero"] li[class="cmp-carousel__item js_slide active"] p[class="copy body-03"]'
ALL_VEHI_TXT = 'div[data-aa-content-section="explore all vehicles"] h2[class="tabbed-container__title "]'
PAG_NUM_TXT = 'div[class="pagination numbers non-interactive"][style*="1;"]'
SHOP_TOOLS_TXT = 'h2[class="ttac-headline align-center spacing-none-d spacing-none-d-p"]'


class MobileToyotaHomePage(object):
    def __init__(self, driver, explicit_wait=20):
        self.driver = driver
        self.wait_driver = WebDriverWait(self.driver, explicit_wait)
        
        self.toyota_logo_btn = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.CSS_SELECTOR, TOYOTA_LOGO_BTN)))
        self.user_btn = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.CSS_SELECTOR, USER_BTN)))
        self.hamburger_btn = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.CSS_SELECTOR, HAMBURGER_BTN)))
        self.homepage_carousel = self.wait_driver.until(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, HOMEPAGE_CAROUSEL)))
        self.learn_more = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.CSS_SELECTOR, LEARN_MORE)))
        self.info_btn = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.CSS_SELECTOR, INFO_BTN)))
        self.heading_txt = self.wait_driver.until(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, HEADING_TXT)))
        self.subhead_txt = self.wait_driver.until(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, SUBHEAD_TXT)))
        self.al_vehi_txt = self.wait_driver.until(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, ALL_VEHI_TXT)))
        self.shop_tools_txt = self.wait_driver.until(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, SHOP_TOOLS_TXT)))
    
    @property
    def pag_num_txt(self):
        return self.wait_driver.until(EC.visibility_of_element_located((AppiumBy.CSS_SELECTOR, PAG_NUM_TXT)))

    @property
    def play_btn(self):
        return self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.CSS_SELECTOR, PLAY_BTN)))
