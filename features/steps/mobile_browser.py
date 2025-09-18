import time
from behave import step
from appium.webdriver.client_config import AppiumClientConfig
from appium import webdriver as appiumdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from resources.page_objects.mobile.android_notifications_page_objects import SelectWithOrWithoutAccount
from resources.objects.mobile.w3c_mobile_actions import W3CMobileActions, W3CMobileGestures
from appium.webdriver.common.appiumby import AppiumBy


@step('I open an android chrome web browser and go to "{url}" url')
def create_webdriver(context, url):
    appium_server_url = 'http://localhost:4723/wd/hub'

    options = UiAutomator2Options()
    appium_capabilities = {"deviceName": "RZCX10WSYZF", "platformVersion": "15"}
    appium_capabilities.update({"appPackage": "com.android.chrome", "appActivity": "com.google.android.apps.chrome.Main", 
                                "newCommandTimeout": "180", "NoReset": "true", "autoGrantPermissions": "true", "W3C":"true"})

    options.load_capabilities(appium_capabilities)
    context.driver = appiumdriver.Remote(appium_server_url, options=options)

    context.driver.get('https://www.toyota.com')

@step('I change the context to "{context_name}"')
def change_context_to(context, context_name, timeout=30):
    new_context = None
    init_ts = int(time.time())
    while int(time.time()) < init_ts + timeout and not new_context:
        for context_item in context.driver.contexts:
            if context_name in context_item:
                new_context = context_item
                break
        else:
            continue
        break
    else:
        assert False, f'Could not set context to {context_name} within {timeout} seconds'
    context.driver.switch_to.context(context_item)

@step('I accept to open chrome browser without account')
def continue_chrome_without_acc(context):
    SelectWithOrWithoutAccount(context.driver).select_without_acc()

@step('I perform a full swipe up')
def swipe_up(context):
    height = context.driver.get_window_size()['height'] - 50

    W3CMobileActions(context.driver).swipe(100, height, 10, 100, 300)

@step('I perform a swipe "{motion}" with percentage "{num:f}" of total screen')
def swipe_up_with_gesture(context, motion, num):
    W3CMobileGestures(context.driver).swipe(motion, num)

@step('I scroll to element "{element}"')
def scroll2element(context, element):
    webdriver_ele = context.driver.find_element(AppiumBy.CSS_SELECTOR, 'h2[class="ttac-headline align-center spacing-none-d spacing-none-d-p"]')
    can_scroll_more = context.driver.execute_script('mobile: scrollGesture', {'elementId': webdriver_ele.id, 'direction': 'down', 'percent': 3.0})
