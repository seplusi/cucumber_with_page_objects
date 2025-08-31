import re
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from resources.page_objects.slide_page import CarSlide, ShoppingCarSlide


TOYOTA_LOGO_BTN = 'a[data-di-id="#logo"]'
VEHICLES_BTN = 'button[data-aa-action="aa-action"][class*="select-vehicle"]'
SHOPPING_BTN = 'button[data-aa-action="aa-action"][class*="shopping-tools"]'
OWNERS_BTN = 'button[data-aa-action="aa-action"][class*="owners"]'
USER_BTN = 'button > div[class="user-icon-wrap"]'
EXPL_ALL_VEHI_TXT = 'div[data-aa-content-section="explore all vehicles"] h2[class="tabbed-container__title "]'


class ToyotaCommonHomePage(object):
    def __init__(self, driver, explicit_wait=20):
        self.driver = driver
        self.wait_driver = WebDriverWait(self.driver, explicit_wait)

        self.toyota_logo_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, TOYOTA_LOGO_BTN)))
        self.vehicles_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, VEHICLES_BTN)))
        self.shopping_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SHOPPING_BTN)))
        self.owners_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, OWNERS_BTN)))
        self.user_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, USER_BTN)))

#######################################################################################################################

EXPL_ALL_VEHI_LST = 'div[data-aa-content-section="explore all vehicles"]  ol[role="tablist"] > li'


class ToyotaHomePage(ToyotaCommonHomePage):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver, explicit_wait)
        self.expl_all_vehi_txt = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, EXPL_ALL_VEHI_TXT)))
    
    @property
    def expl_all_vehi_lst(self):
        return self.wait_driver.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, EXPL_ALL_VEHI_LST)))

#######################################################################################################################

CROSS_AND_MINIVANS_BTN = 'li[data-model-category="crossovers-suvs"] > button'
CARS_AND_MINIVANS_BTN = 'li[data-model-category="cars-minivan"] > button'
TRUCKS_BTN = 'li[data-model-category="trucks"] > button'
ELECTRIFIED_BTN = 'li[data-model-category="electrified"] > button'
UPCOM_VEHI_BTN = 'li[data-model-category="upcoming-vehicle"] > button'
GAZOO_RCN_BTN = 'div[class="performance-links"] a[aria-label="Gazoo Racing"]'
TRD_PRO_BTN = 'div[class="performance-links"] a[aria-label="TRD Pro"]'
VIEW_ALL_VEHI_BTN = 'ul[class="models"] a[href="/all-vehicles/"]'
CERT_USED_VEHI_BTN = 'ul[class="models"] a[href*="certified"]'
CROSS_SUVS_LST = 'ul[class="vehicles"] > li[data-model-category="crossovers-suvs"]'


class ToyotaVehiclesPage(ToyotaCommonHomePage):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver, explicit_wait)
        self.cross_and_minivans_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, CROSS_AND_MINIVANS_BTN)))
        self.cars_and_minivans_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, CARS_AND_MINIVANS_BTN)))
        self.trucks_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, TRUCKS_BTN)))
        self.electrified_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ELECTRIFIED_BTN)))
        self.upcom_vehi_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, UPCOM_VEHI_BTN)))
        self.gazoo_rcn_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, GAZOO_RCN_BTN)))
        self.trd_pro_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, TRD_PRO_BTN)))
        self.view_all_vehi_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, VIEW_ALL_VEHI_BTN)))
        self.cert_used_vehi_btn = self.wait_driver.until(EC.element_to_be_clickable((By.CSS_SELECTOR, CERT_USED_VEHI_BTN)))

    @property
    def cross_suvs_lst(self):
        return self.wait_driver.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, CROSS_SUVS_LST)))

    def verify_each_car_slide_has_correct_data(self, names, hybrid_txts):
        slides_elements_lst = self.cross_suvs_lst
        for car_name, hybrid_txt, element in zip(names, hybrid_txts, slides_elements_lst):
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            car_slide = CarSlide(element)
            assert car_slide.model_name == car_name
            assert car_slide.top_level_text == hybrid_txt
            assert car_slide.build_link.text == "Build"
            assert car_slide.offers_link.text == "Special Offers"
            assert re.search('^\$[0-9]{2},[0-9]{3} as shown \*$', car_slide.as_shown_price), f'car_slide.as_shown_price assertion error'
            assert re.search('^\$[0-9]{2},[0-9]{3}\* Starting MSRP$', car_slide.msrp_price), f'car_slide.msrp_price assertion error'

#######################################################################################################################
FIND_YR_VEHICLE_TXT = 'ul[class="col1"] > li[class="category"]:nth-child(1)'
TOY_CERT_USED_VEH = 'ul[class="col1"] a[href*="https://www.toyotacertified.com"]'
ACCESSORIES = 'ul[class="col1"] a[href="/accessories/"]'
COMP_VEHI = 'ul[class="col1"] a[href="/compare/"]'
BUY_PARTS_ACCESS = 'ul[class="col1"] a[href="https://autoparts.toyota.com/"]'
SHOP_ONLINE_W_SPATH = 'ul[class="col1"] a[href="/smartpath/how-it-works/"]'
VIEW_BROCH = 'ul[class="col1"] a[href="/brochures/"]'
SHIPPING_SLIDES = 'div.primary-links-wrapper > ul[data-aarole="cta-container"] > li'

class ToyotaShoppingPage(ToyotaCommonHomePage):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver, explicit_wait)
        self.find_yr_vehicle_txt = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, FIND_YR_VEHICLE_TXT)))
        self.toy_cert_used_veh = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, TOY_CERT_USED_VEH)))
        self.accessories = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ACCESSORIES)))
        self.comp_vehi = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, COMP_VEHI)))
        self.buy_parts_access = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, BUY_PARTS_ACCESS)))
        self.shop_online_w_spath = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, SHOP_ONLINE_W_SPATH)))
        self.view_broch = self.wait_driver.until(EC.visibility_of_element_located((By.CSS_SELECTOR, VIEW_BROCH)))
    
    @property
    def shopping_slides(self):
        return self.wait_driver.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, SHIPPING_SLIDES)))

    def verify_each_car_slide_has_correct_data(self, infos):
        shopping_slides_elements_lst = self.shopping_slides
        for info, element in zip(infos, shopping_slides_elements_lst):
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            time.sleep(1)
            shipping_car_slide = ShoppingCarSlide(element)
            assert shipping_car_slide.info_txt == info, f'{shipping_car_slide.info_txt} differs from {info}'
