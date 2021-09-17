"""继承unittest.Testcase"""
"""
Code description:unittest framework
Create time:
Developer:
"""
from retail.test_case.models.driver import WDriver
import logging
import unittest
from retail.test_case.page_obj.login_page import LoginPage
from retail.test_case.models.log import Logger
from selenium import webdriver

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class MyunitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:  # 一个测试类执行一次打开浏览器，节约每个用例打开一次浏览器的时间
        cls.driver = WDriver().ChromeDriver()
        cls.driver.maximize_window()
        log.logger.info('opened the browser successed!')

    def setUp(self) -> None:
        """

        :return:
        """
        self.login = LoginPage(self.driver)
        self.login.open()
        log.logger.info('************************starting run test cases************************')

    def tearDown(self) -> None:
        """
        :return:
        """
        self.driver.refresh()
        log.logger.info('************************test case run completed************************')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        log.logger.info('quit the browser success!')


if __name__ == '__main__':
    unittest.main()
