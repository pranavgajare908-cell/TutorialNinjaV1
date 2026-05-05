from selenium.webdriver.common.by import By


class MyAccount:
    lnk_logout_xpath = "//ul[@class='dropdown-menu dropdown-menu-right']//a[text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogout(self):
        self.driver.find_elemeent(By.XPATH, self.lnk_logout_xpath).click() 
