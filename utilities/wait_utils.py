from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class WaitUtils:
    def __init__(self, driver, timeout=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_clickable(self, locator_type, locator):
        return self.wait.until(
            EC.element_to_be_clickable((locator_type, locator))
        )

    def wait_for_visible(self, locator_type, locator):
        return self.wait.until(
            EC.visibility_of_element_located((locator_type, locator))
        )
