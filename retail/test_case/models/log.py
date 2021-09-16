import logging
import time


class Logger(object):
    def __init__(self, logger, CmdLevel=logging.INFO, FileLevel=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # 设置日志输出的默认级别
        # 日志输出格式
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        # 日志文件名称
        currTime = time.strftime("%Y-%m-%d")
        self.LogFileName = r'F:\25906\Petrochina_Retail_Test_Project\retail\report\Log\log'+currTime+'.log'
        # 设置文件输出
        fh = logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)  # 日志级别
        self.logger.addHandler(fh)


if __name__ == '__main__':
    logger = Logger("fox", CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG)
    logger.logger.debug("debug")
    logger.logger.log(logging.ERROR, '%(module)s %(info)s', {'module': 'log日志', 'info': 'error'})
