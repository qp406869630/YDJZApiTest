#!/user/bin/env python
# coding=utf-8

import os
from jpype import *


class SMUtil_YMY:
    def jvm_load(self):
        # java虚拟机的路径
        # jvmPath = r"E:\jdk1.8.0_65\jre\bin\server\jvm.dll"
        jvmPath = getDefaultJVMPath()
        # 所有调用的方法的绝对路径
        ext_classpath = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'SM_YMY.jar')

        # 加载进方法,如果JVM没有启动，就启动JVM
        if not isJVMStarted():  # 这个判断非常重要，因为JVM在一个进程内就会自动关闭，后面在调用就会报错
            startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % ext_classpath)
        # 完整的包名.类名
        RcpClass = JClass("SM_YMY.Sm4Util")
        return RcpClass

    def YMY_Encrypt(self, text):
        rcp = self.jvm_load()
        EncryptData = rcp.encrypt(text)
        return EncryptData
        # 关闭java虚拟机
        shutdownJVM()

    def YMY_Decrypt(self, text):
        rcp = self.jvm_load()
        DecryptData = rcp.decrypt(text)
        return DecryptData
