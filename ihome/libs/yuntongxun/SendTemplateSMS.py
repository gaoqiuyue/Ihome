#coding=gbk

#coding=utf-8

#-*- coding: UTF-8 -*-
import json

from ihome.libs.yuntongxun.CCPRestSDK import REST
#import ConfigParser

#���ʺ�
accountSid= '8aaf07086b211c22016b2b90bd160792'

#���ʺ�Token
accountToken= '710e210a203b4f2289c8f828adb1251f'

#Ӧ��Id
appId='8aaf07086b211c22016b2b90bd7a0799'

#�����ַ����ʽ���£�����Ҫдhttp://
serverIP='app.cloopen.com'

#����˿� 
serverPort='8883'

#REST�汾��
softVersion='2013-12-26'

  # ����ģ�����
  # @param to �ֻ�����
  # @param datas �������� ��ʽΪ���� ���磺{'12','34'}���粻���滻���� ''
  # @param $tempId ģ��Id
class CCP(object):
    #ʹ�õ���ģʽ���ж��Ƿ����Ѿ������õĶ��󣬱�֤��ʼ��ִֻ��һ��
    ##__init__()�������ʵ����������__init__()����֮ǰ��__new__()�����Ƿ� Ҫʹ�ø�__init__()��������Ϊ__new__()���Ե���������Ĺ��췽������ֱ�ӷ��ر�Ķ�������Ϊ���� ��ʵ��
    ##������������������
    isinstance=None
    def __new__(cls):
        if cls.isinstance is None:
            obj=super(CCP,cls).__new__(cls)
            # ��ʼ��REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)
            cls.isinstance=obj
        return obj

    def sendTemplateSMS(self,to,datas,tempId):
        results = self.rest.sendTemplateSMS(to,datas,tempId)
        print(results)
        status_code=results.get("statusCode")
        if status_code=="000000":
            #���ͳɹ�
            return 0
        else:
            return -1
    

if __name__ == '__main__':
    cpp=CCP()
    cpp.sendTemplateSMS("13688815040",["768","3"],1)
#sendTemplateSMS(�ֻ�����,��������,ģ��Id)