# encoding = 'utf-8'
import pytest


@pytest.fixture(scope='session', autouse=True)
def exe_all():
    print('开始执行测试！')
    yield
    print('测试结束')
