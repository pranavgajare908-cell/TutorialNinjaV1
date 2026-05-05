from selenium.webdriver.common.by import By
from utilities.wait_utils import WaitUtils


class HomePage():
    lnk_myaccount_xpath = "//span[text()='My Account']"
    lnk_register_xpath = "//a[text()='Register']"
    lnk_login_xpath = "//a[text()='Login']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def clickMyAccount(self):
        self.wait.wait_for_clickable(By.XPATH, self.lnk_myaccount_xpath).click()

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.lnk_register_xpath).click()

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.lnk_login_xpath).click()

