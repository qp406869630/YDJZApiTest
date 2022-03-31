# encoding = 'utf-8'
import os
from common.utils import Utils

import pytest

os.system('chcp 65001')
timestamp = Utils().get_timestamp()
cmd1 = 'cmd.exe /k rd/s/q report\\my_allure_results'
cmd2 = f'cmd.exe /k allure generate report\\my_allure_results -o report\\html_{timestamp} --clean'
if __name__ == '__main__':
    # 删除上次生成的json文件
    os.popen(cmd1)
    pytest.main()
    # 生成HTML测试报告
    os.popen(cmd2)
