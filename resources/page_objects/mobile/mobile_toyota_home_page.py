import yaml
from resources.page_objects.common.page_object_common_class import PageObjectCommonClass


class MobileToyotaHomePage(PageObjectCommonClass):
    def __init__(self, driver, explicit_wait=20):
        super().__init__(driver)
        with open('resources/page_objects_definitions/mobile_toyota_pages.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.SafeLoader)
        # Create page elements
        self._load_page_object(explicit_wait)