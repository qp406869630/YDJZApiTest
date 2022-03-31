# encoding = 'utf-8'
import pytest
from common.utils import Utils


@pytest.fixture(scope='function', autouse=False)
def exe_func():
    print('每一个测试用例执行前')
    yield
    print('每一个测试用例执行后')


@pytest.fixture(scope='session', autouse=True)
def clear_all():
    Utils().clear_shotlist()
    Utils().clear_inquiry()
    Utils().clear_record()
    print('数据已初始化')
    yield
    Utils().clear_shotlist()
    Utils().clear_inquiry()
    Utils().clear_record()
    print('数据已清空')
