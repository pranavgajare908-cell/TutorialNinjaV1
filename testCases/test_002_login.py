import os.path

import pytest
from webdriver_manager.core import driver

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.screenshot import Screenshot


class Test_Login():
    base_url = ReadConfig.getApplicationURL()
    logger = LogGen.logger()  # looger

    user = ReadConfig.getEmail()
    user = ReadConfig.getPassword()

    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("********** Starting Test_002_login **********")
        self.driver = driver
        self.driver.get(set, baseurl=self.base_url)


        self.hp = HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.user)
        self.lp.clickLogin()

        self.targetPage=self.lp.isMyAccountExists()
        if self.targetPage==True:
            assert True
        else:
            Screenshot.capture(self.driver, "test_001_login.png")
            assert False
        self.logger.info("********** End of Test_002_login **********")
