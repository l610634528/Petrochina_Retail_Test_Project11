"""
Code description: auto run test case
Create time:
Developer:
"""

import unittest
import time
from BeautifulReport import BeautifulReport
from retail.config.conf import *
from retail.test_case.models.testreport import testreport
from retail.test_case.models.sendmail import SendMail

if __name__ == '__main__':
    runner, fp, fileName = testreport()
    test_suite = unittest.defaultTestLoader.discover(tcPath, pattern='.*Tc.py')
    runner.run(test_suite)
    fp.close()
    # SendMail.sendEmail(fileName)
