# encoding = 'utf-8'
import pytest


def read():
    return ['胡歌', '彭于晏', '秦鹏', '张学友']


@pytest.fixture(scope='function', autouse=False, params=read())
def exe_database_sql(request):
    print('在方法之前执行')
    yield request.param
    print('在方法之后执行')


class Test:
    def test(self, exe_database_sql):
        print('测试fixture前后置')
        print(exe_database_sql)
