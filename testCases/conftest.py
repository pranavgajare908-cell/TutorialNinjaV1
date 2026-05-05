from datetime import datetime
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.readProperties import ReadConfig


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    # browser = ReadConfig.getBrowser()
    if browser == "edge":
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
        )
        print("Launching Edge browser.............")
    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
        print("Launching Chrome browser.............")
    else:
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        print("Launching Chrome browser.............")
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


############# Pytest HTML Report ################
# it is hook for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Tutorial Ninja'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pranav'


# it is hook for delete/modify environment info into HTML Report
@pytest.mark.optioalhook
def pytest_metadata(metadata):
    metadata.pop("Java_Home", None)
    metadata.pop("Plugins", None)


# specifying Report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime(
        "%Y%m%d%H%M%S") + ".html"

    # ================== 🔥 AUTO SCREENSHOT ON FAILURE ==================
    # @pytest.hookimpl(hookwrapper=True)
    # def pytest_runtest_makereport(item):
    #     outcome = yield
    #     rep=outcome.get_result()
    #     print("HOOK EXECUTED:", item.name, rep.when, rep.failed)  # 👈 DEBUG
    #
    #     # Take screenshot only when test fails
    #     if rep.when == 'call' and rep.failed:
    #         print("TEST FAILED - TAKING SCREENSHOT")  # 👈 DEBUG
    #         driver=item.funcargs.get("setup")  # get driver from fixture
    #         if driver:
    #             Screenshot.capture(driver, item.name)
    #         else:
    #             print("DRIVER NOT FOUND ❌")
