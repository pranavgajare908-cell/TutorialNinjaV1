import configparser
import os.path

config = configparser.RawConfigParser()
config.read(os.path.join(os.path.abspath(os.curdir), "configurations", "config.ini"))


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = (config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def getBrowser():
        browser = config.get('commonInfo', 'browser')
        return browser

    @staticmethod
    def getEmail():
        browser = config.get('commonInfo', 'email')
        return browser

    @staticmethod
    def getPassword():
        browser = config.get('commonInfo', 'password')
