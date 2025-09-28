from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageElement(object):
    def __init__(self, by, value, driver, wait4load=None):
        self.locator = (by, value)
        self.driver = driver
        if wait4load:
            WebDriverWait(self.driver, wait4load).until(EC.visibility_of_element_located((self.locator)))

    @property
    def web_element(self):
        """Find WebElement using element locator

        :returns: web element object
        :rtype: selenium.webdriver.remote.webelement.WebElement or appium.webdriver.webelement.WebElement
        """
        try:
            web_element = self.driver.find_element(*(self.locator))
        except NoSuchElementException as exception:
            parent_msg = f" and parent locator {self.parent_locator_str()}" if self.parent else ''
            msg = "Page element of type '%s' with locator %s%s not found"
            self.logger.error(msg, type(self).__name__, self.locator, parent_msg)
            exception.msg += "\n  {}".format(msg % (type(self).__name__, self.locator, parent_msg))
            raise exception
        return web_element