# encoding = 'utf-8'
import pytest


@pytest.fixture(scope='function', autouse=False)
def exe_database_sql():
    print('在方法之前执行')
    yield
    print('在方法之后执行')


@pytest.fixture(scope='class', autouse=False)
def connect_to_database():
    print('在类之前执行')
    yield
    print('在方法后执行')


@pytest.mark.usefixtures('connect_to_database')
class Test:
    def test(self, exe_database_sql):
        print('测试fixture前后置')
