"""存放driver"""
"""
Code description:save all driver info
Create time:
Developer:
"""

from selenium import webdriver
import logging
import sys
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class WDriver(object):
    # driver: WebDriver
    # Chrome driver
    def __init__(self):
        self.chromedriver = webdriver.Chrome()
        self.firefoxdriver = webdriver.Firefox()
        self.iedriver = webdriver.Ie()

    def ChromeDriver(self):
        """

        :return:
        """
        try:
            pass
        except Exception as e:
            log.logger.exception('FireFoxDriverServer.exe executable needs to be in PATH. Please download!',
                                 exc_info=True)
            raise e
        else:
            log.logger.info(
                '%s:found the Firefox driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.chromedriver

    # Firefox driver

    def FirefoxDriver(self):
        """

        :return:
        """
        try:
            pass
        except Exception as e:
            log.logger.exception('FireFoxDriverServer.exe executable needs to be in PATH. Please download!',
                                 exc_info=True)
            raise e
        else:
            log.logger.info(
                '%s:found the Firefox driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.firefoxdriver

    # Ie driver

    def IeDriver(self):
        """

        :return:
        """
        try:
            pass
        except Exception as e:
            log.logger.exception('FireFoxDriverServer.exe executable needs to be in PATH. Please download!',
                                 exc_info=True)
            raise e
        else:
            log.logger.info(
                '%s:found the Firefox driver [%s] successed !' % (sys._getframe().f_code.co_name, self.driver))
            return self.iedriver


if __name__ == '__main__':
    WDriver = WDriver()
    WDriver.ChromeDriver()
