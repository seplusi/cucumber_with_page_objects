from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.action_chains import ActionChains


class W3CMobileActions:
    """
    Code based in appium/webdriver/extensions/action_helpers.py (Appium 3)
    """
    def __init__(self, driver):
        self.driver = driver

    def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 100):
        """Swipe from one point to another point, for an optional duration.

        Args:
            start_x: x-coordinate at which to start
            start_y: y-coordinate at which to start
            end_x: x-coordinate at which to stop
            end_y: y-coordinate at which to stop
            duration: defines the swipe speed as time taken to swipe from point a to point b, in ms.

        Usage:
            driver.swipe(100, 100, 100, 400)

        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        touch_input = PointerInput(interaction.POINTER_TOUCH, 'finger')

        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=touch_input, duration=duration)
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return self


class W3CMobileGestures(object):
    """
    Code based in appium/webdriver/extensions/action_helpers.py (Appium 3)
    """
    def __init__(self, driver):
        self.driver = driver
        self.width = self.driver.get_window_size()['width']
        self.height = self.driver.get_window_size()['height']

    def swipe(self, swipe_motion, percent: int, speed: int = 5000):
        self.driver.execute_script('mobile: swipeGesture', {'left': 1, 'top': 1, 'width': self.width, 'height': self.height, 'direction': swipe_motion, 'percent': percent/100, 'speed': speed})
