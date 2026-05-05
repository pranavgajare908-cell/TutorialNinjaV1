import os.path
import time

import pytest
from webdriver_manager.core import driver

from testCases.conftest import setup
from pageObjects.AccountRegisterPage import AccountRegisterPage
from pageObjects.HomePage import HomePage
from utilities.data_generator import DataGenerator
from utilities.readProperties import ReadConfig

from utilities.screenshot import Screenshot
from utilities.customLogger import LogGen


class Test001AccountRegistration:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.logger()  # for logging

    @pytest.mark.regression
    def test_account_reg(self, setup):
        self.logger.info("***** test_001_AccountRegistration Started *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("***** Launching Application *****")
        self.hp = HomePage(self.driver)
        self.logger.info("***** Clicking on MyAccount --> Registration Page *****")
        self.hp.clickMyAccount()
        self.hp.clickRegister()

        self.logger.info("***** Providing Customer Details for Registration *****")
        self.regpage = AccountRegisterPage(self.driver)
        self.regpage.setFirstName("John")
        self.regpage.setLastName("Candey")
        self.email = DataGenerator.generate_email()
        self.regpage.setEmail(self.email)
        self.regpage.setTelephone("1234567890")
        self.regpage.setPassword("1234")
        self.regpage.setConfirmPassword("1234")
        self.regpage.setPrivacyPolicy()
        self.regpage.clickContinue()
        time.sleep(5)
        self.confirmsg = self.regpage.getConfirmationMsg()
        print("Confirmation Message:", self.confirmsg)

        if "Your Account Has Been Created!" in self.confirmsg:
            self.logger.info("***** Account Has Been Created *****")
            assert True
        else:
            Screenshot.capture(self.driver, "test_001_AccountRegistration")
            self.logger.error("***** Account Has Been Failed *****")
            assert False
        self.logger.info("***** test_001_AccountRegistration Ended *****")
