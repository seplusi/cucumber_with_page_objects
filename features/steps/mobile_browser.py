import time
from behave import step
from appium.webdriver.client_config import AppiumClientConfig
from appium import webdriver as appiumdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from resources.page_objects.mobile.android_notifications_page_objects import SelectWithOrWithoutAccount


@step('I open an android chrome web browser and go to "{url}" url')
def create_webdriver(context, url):
    appium_server_url = 'http://localhost:4723/wd/hub'

    options = UiAutomator2Options()
    appium_capabilities = {"deviceName": "RZCX10WSYZF", "platformVersion": "15"}
    appium_capabilities.update({"appPackage": "com.android.chrome", "appActivity": "com.google.android.apps.chrome.Main", 
                                "newCommandTimeout": "180", "NoReset": "true", "autoGrantPermissions": "true"})

    options.load_capabilities(appium_capabilities)
    context.driver = appiumdriver.Remote(appium_server_url, options=options)

    context.driver.get('https://www.toyota.com')

@step('I change the context to "{context_name}"')
def change_context_to(context, context_name, timeout=20):
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
