"""
Code description:base page 封装一些工共方法
Create time:
Developer:
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import logging
import sys
from retail.test_case.models.log import Logger
from retail.config import conf
from retail.test_case.models.doexcel import ReadExcel

eleData = ReadExcel()  # 存储系统所有的元素数据
testLoginData = ReadExcel('elementData.xlsx', 'userNamePw')  # 登录模块测试数据
modifyPwData = ReadExcel('elementData.xlsx', 'modifyPw')  # 修改密码模块测试数据
queryData = ReadExcel('elementData.xlsx', 'queryData')
log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class BasePage(object):
    """主单元"""
    menuList = \
        [(By.LINK_TEXT, eleData.readExcel(7, 3)),  # 权限管理
         (By.LINK_TEXT, eleData.readExcel(8, 3)),  # 会员档案
         (By.LINK_TEXT, eleData.readExcel(9, 3)),  # 积分消费查询
         (By.LINK_TEXT, eleData.readExcel(10, 3)),  # 功能演示
         (By.LINK_TEXT, eleData.readExcel(11, 3)),  # 待办工作
         (By.LINK_TEXT, eleData.readExcel(12, 3)),  # 报表
         (By.LINK_TEXT, eleData.readExcel(13, 3)),  # 积分规则/活动查询
         (By.LINK_TEXT, eleData.readExcel(14, 3))]  # 积分规则/活动申请

    def __init__(self, driver, url='http://11.11.164.134:9081/rmms/modules/ep.rmms.portal/login/login.jsp'):
        """

        :param driver:
        :param url:
        """
        self.driver = driver
        self.base_url = url

    def _open(self, url):
        """

        :param url:
        :return:
        """
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
