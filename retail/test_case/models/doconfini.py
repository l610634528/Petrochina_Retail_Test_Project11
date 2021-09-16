"""读配置文件"""
import logging
import configparser
from retail.test_case.models.log import Logger

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class DoConfIni(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()

    # 从ini文件中读取数据
    def getConfValue(self, filename, section, name):
        try:
            self.cf.read(filename)
            value = self.cf.get(section, name)
        except Exception as e:
            log.logger.exception('read file [%s] for [%s] failed , did not get the value' % (filename, section))
            raise e
        else:
            log.logger.info('read excel value [%s] successed! ' % value)
            return value

    # 向ini文件中写数据
    def writeConfValue(self, filename, section, name, value):
        try:
            self.cf.add_section(section)
            self.cf.set(section, name, value)
            self.cf.write(open(filename, 'w'))
        except Exception:
            log.logger.exception('section %s has been exist!' % section)
            raise configparser.DuplicateOptionError(section)
        else:
            log.logger.info('write section' + section + 'with value ' + value + ' successed!')


# if __name__ == '__main__':
#     print(1)
    # file_path = currPath
    # print(file_path)
    # read_config = DoConfIni()
    #
    # value = read_config.getConfValue(os.path.join(currPath, 'config.ini'), 'project', 'project_path')
    # print(value)
    #
    # read_config.writeConfValue(os.path.join(currPath, 'config.ini'), 'tesesection', 'name', 'hello word')
