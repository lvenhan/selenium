# -*- coding:utf-8 -*-
from Public import operation
from Public import getCsv
from Public import LogManager

opreate=operation.Common()
getcsv=getCsv.GetCsv()
log=LogManager.LogMgr('addaccount')
class accountM():
    #读csv添加账户名称
    def addAccount(self):
        #获取文件路径
        csvpath=opreate.read_file('testData','account.csv')
        csvlist=getcsv.readCsv(csvpath)
        for list in csvlist:
            add_account={
                'account':list[0],
                'password':list[1],
                'confirmpassword':list[2],
                'name':list[3],
                'tel':list[4],
                'email':list[5]
            }
            self.addaccount_page(add_account)

    #添加账户
    def addaccount_page(self,dict):
        try:
            #进入子账号管理--添加子账号
            account=("ziUser","btn-form-add")
            opreate.tuple_click("id",account)
            #子账号
            opreate.element_input("xpath",".//*[@id='form-channel']//input[@data-field='account']",dict['account'])
            #密码
            opreate.element_input("id","form-pass",dict['password'])
            #确认密码
            opreate.element_input("xpath",".//*[@id='form-channel']//input[@data-match='#form-pass']",dict['confirmpassword'])
            #姓名
            opreate.element_input("xpath",".//*[@id='form-channel']//input[@data-field='user_name']",dict['name'])
            #手机号
            opreate.element_input("xpath",".//*[@id='form-channel']//input[@data-field='telephone']",dict['tel'])
            #邮箱
            opreate.element_input("id","text",dict['email'])
            #保存
            opreate.element_click("id","form-btn-save")
        except:
            log.error(u"添加用户失败")



if __name__ == '__main__':
    accountM().addAccount()