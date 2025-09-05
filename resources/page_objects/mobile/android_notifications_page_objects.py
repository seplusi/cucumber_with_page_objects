from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy


WITHOUT_ACC = 'com.android.chrome:id/signin_fre_dismiss_button'
WITH_ACC = 'com.android.chrome:id/signin_fre_continue_button'


class SelectWithOrWithoutAccount(object):
    def __init__(self, driver, explicit_wait=10):
        self.driver = driver
        self.wait_driver = WebDriverWait(self.driver, explicit_wait)
        self.without_acc = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.ID, WITHOUT_ACC)))
        self.with_acc = self.wait_driver.until(EC.element_to_be_clickable((AppiumBy.ID, WITH_ACC)))

    def select_without_acc(self):
        self.without_acc.click()
