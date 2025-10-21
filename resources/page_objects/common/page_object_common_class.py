from resources.page_element import PageElement, PageElements


class PageObjectCommonClass(object):
    def __init__(self, driver):
        self.driver = driver
    
    def _load_page_object(self, explicit_wait):
        # Create page elements
        for obj_def in self.data[self.__class__.__name__]:
            page_element_class, page_element_def = list(obj_def.items())[0]
            locator_name = page_element_def['Locator-Name']
            locator_type = page_element_def['Locator-Type']
            locator_value = page_element_def['Locator-Value']
            wait = explicit_wait if page_element_def['Wait-For-Loaded'] else None
            setattr(self, locator_name, globals()[page_element_class](locator_type, locator_value, self.driver, wait))
