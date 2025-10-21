import time
import re
from behave import step
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import ElementNotInteractableException
from resources.page_objects.toyota_cookie_page import ToyotaCookiesPage
from resources.page_objects.toyota_home_page import ToyotaHomePage, ToyotaVehiclesPage, ToyotaShoppingPage
from resources.page_objects.mobile.mobile_toyota_cookie_page import MobileToyotaCookiesPage
from resources.page_objects.mobile.mobile_toyota_home_page import MobileToyotaHomePage
from resources.page_objects.mobile.mobile_toyota_home_page_with_hamburger_options import MobileToyotaHomePagewithHamburgerOptions
from resources.page_objects.mobile.mobile_toyota_search_inventory_page import MobileToyotaSearchInventoryPage

chromedriver_path = "/home/luis/Documents/Projects/chromedriver/chromedriver"


@step('I open a chrome web browser and go to "{url}" url')
def create_webdriver(context, url):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Instanciate webdriver
    context.driver = webdriver.Chrome(options=options, service=ChromeService(executable_path=chromedriver_path))
    context.driver.get(url)

@step('the page "{page_name}" is loaded after "{timeout:d}" seconds')
@step('the page "{page_name}" is loaded after some time')
def load_page(context, page_name, timeout=20):
     context.page = globals()[page_name](context.driver, timeout)

@step('I accept the cookie')
def load_and_accept_cookie(context):
     context.page.accept()

@step('cookie banner is not displayed after some time')
def element_not_displayed_after_some_time(context, timeout=10):
     context.page.cookie_banner_not_displayed_after_some_time(timeout)

@step('the text of element "{element}" is equal to "{text}"')
def element_text_is_equal(context, element, text):
     webdriver_ele = getattr(context.page, element)
     assert webdriver_ele.web_element.text == text, f'Text {text} differs from {webdriver_ele.web_element.text}'

@step('the text of element "{element}" matches the regex "{reg_txt}"')
def element_text_is_equal(context, element, reg_txt):
     webdriver_ele = getattr(context.page, element)
     assert re.search(reg_txt, webdriver_ele.web_element.text), f'Regex {reg_txt} not found in {webdriver_ele.web_element.text}'
     
@step('the text of element "{element}" contains text "{text}"')
def element_text_contains(context, element, text):
     webdriver_ele = getattr(context.page, element)
     assert text in webdriver_ele.web_element.text, f'Text {text} not in {webdriver_ele.web_element.text}'

@step('the element "{element}" has attribute "{attr}" with value "{text}"')
def element_text_contains(context, element, attr, text):
     webdriver_ele = getattr(context.page, element)
     assert text == webdriver_ele.web_element.get_attribute(attr), f'Text {text} not in {webdriver_ele.web_element.text}'

@step('I type text "{text}" using the input element "{element}"')
def element_text_contains(context, text, element):
     webdriver_ele = getattr(context.page, element)
     webdriver_ele.web_element.send_keys(text)

@step('the element "{element}" is displayed after some time')
def waut_4_element_be_displayed(context, element, timeout=10):
     webdriver_ele = getattr(context.page, element)
     init_ts = int(time.time())
     while int(time.time()) < init_ts + timeout:
          try:
               webdriver_ele.web_element
               break
          except Exception as e:
               time.sleep(0.5)
     else:
          webdriver_ele.web_element

@step('I close webdriver')
def close_driver(context):
    # Example cleanup: close a browser, reset a database, etc.
    if hasattr(context, 'driver'):
            context.driver.quit()

@step('the cookie "{cookie}" is found in the browser cookies')
def get_browser_cookies(context, cookie):
     cookies_lst = context.driver.get_cookies()
     assert cookie in [item['domain'] for item in cookies_lst], f'List of current cookies: {cookies_lst}'

@step('I click on the "{element}" button')
def click_element(context, element):
     webdriver_ele = getattr(context.page, element)
     webdriver_ele.web_element.click()

@step('I safe click on the "{element}" button')
def click_element_expecting_failure_and_retry(context, element, timeout=10):
     init_ts = int(time.time())
     while int(time.time()) < init_ts + timeout:
          try:
               click_element(context, element)
               break
          except ElementNotInteractableException:
               time.sleep(0.5)
     else:
          click_element(context, element)


@step('there are "{count:d}" elements on the "{element_group}" elements list after some time')
def number_of_elements_on_list(context, count, element_group, timeout=10):
     init_ts = int(time.time())
     while int(time.time()) < init_ts + timeout:
          try:
               if len(getattr(context.page, element_group).web_elements) == count:
                    break
               time.sleep(1)
          except Exception:
               time.sleep
     else:
          assert False, f'Could not find {count} elements in element group {element_group}'

@step('the elements list "{elements_list}" contains the following texts in this order')
def list_text_contain(context, elements_list):
     for row, element in zip(context.table, getattr(context.page, elements_list).web_elements):
          assert row['content'] == element.text, f'{row["content"]} differs from {element.text}'

@step('each car slide has the correct info after moving the mouse to it')
def check_each_model(context):
     car_names = [row['name'] for row in context.table]
     hybrid_txts = [row['hybrid'] for row in context.table]

     context.page.verify_each_car_slide_has_correct_data(car_names, hybrid_txts)

@step('each shopping car slide has the correct info after moving the mouse to it')
def check_eachshopping_slide(context):
     car_names = [row['name'] for row in context.table]

     context.page.verify_each_car_slide_has_correct_data(car_names)