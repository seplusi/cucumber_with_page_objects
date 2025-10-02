import re
import time
import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from resources.page_objects.slide_page import CarSlide, ShoppingCarSlide
from resources.page_objects.common.page_object_common_class import PageObjectCommonClass


class ToyotaHomePage(PageObjectCommonClass):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver)
        # Get all elements locators
        with open('resources/page_objects_definitions/toyota_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        self._load_page_object(explicit_wait)

#######################################################################################################################

class ToyotaVehiclesPage(PageObjectCommonClass):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver)
        with open('resources/page_objects_definitions/toyota_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        self._load_page_object(explicit_wait)

    def verify_each_car_slide_has_correct_data(self, names, hybrid_txts):
        slides_elements_lst = self.cross_suvs_lst.web_elements
        for car_name, hybrid_txt, element in zip(names, hybrid_txts, slides_elements_lst):
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            car_slide = CarSlide(element)
            assert car_slide.model_name.web_element.text == car_name, f'{car_slide.model_name} differs from {car_name}'
            assert car_slide.get_safe_top_level_text == hybrid_txt, f'{car_slide.get_safe_top_level_text} differs from {hybrid_txt}'
            assert car_slide.build_link.web_element.text == "Build", f'{car_slide.build_link.text} differs from Build'
            assert car_slide.offers_link.web_element.text == "Special Offers", f'{car_slide.offers_link.text} differs from Special Offers'
            assert re.search('^\$[0-9]{2},[0-9]{3} as shown \*$', car_slide.as_shown_price.web_element.text), f'car_slide.as_shown_price assertion error'
            assert re.search('^\$[0-9]{2},[0-9]{3}\* Starting MSRP$', car_slide.msrp_price.web_element.text), f'car_slide.msrp_price assertion error'

#######################################################################################################################

class ToyotaShoppingPage(PageObjectCommonClass):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver)
        with open('resources/page_objects_definitions/toyota_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        self._load_page_object(explicit_wait)

    def verify_each_car_slide_has_correct_data(self, infos):
        shopping_slides_elements_lst = self.shopping_slides.web_elements
        for info, element in zip(infos, shopping_slides_elements_lst):
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            time.sleep(1)
            shipping_car_slide = ShoppingCarSlide(element)
            assert shipping_car_slide.info_txt.web_element.text == info, f'{shipping_car_slide.info_txt.web_element.text} differs from {info}'
