# -*- coding:utf-8 -*-
import csv,os,sys
from Public import LogManager

log=LogManager.LogMgr('csv')
class GetCsv():
    def readCsv(self,csvpath):
        try:
            data=[]
            with open(csvpath,'rb')as csvfile:
                account_list=csv.reader(csvfile)
                for list in account_list:
                    data.append(list)
                return data
        except:
            log.debug(u"读取csv出错")

if __name__ == '__main__':
    csvpath=os.path.join(sys.path[1],'testData','account.csv')
    GetCsv().readCsv(csvpath)