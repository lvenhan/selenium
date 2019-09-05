# -*- coding:utf-8 -*-
import logging
import os,sys
from datetime import datetime
now=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
filename=now+".log"
class LogMgr():
    def __init__(self,name):
        self.path = os.path.join(os.path.join(sys.path[1],"logger",name+".log"))
        self.logger=logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        #创建formarter
        self.formatString=logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
        #创建一个Handler,输出到控制台
        self.sh=logging.StreamHandler()
        self.sh.setLevel(logging.DEBUG)
        self.sh.setFormatter(self.formatString)
        self.logger.addHandler(self.sh)
        #创建一个日志文件，写到日志文件
        self.fh=logging.FileHandler(self.path, encoding='utf-8')
        self.fh.setFormatter(self.formatString)
        self.logger.addHandler(self.fh)

    def error(self,msg):
        self.logger.error(msg)

    def info(self,msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)