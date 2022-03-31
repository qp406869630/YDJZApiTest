# encoding = 'utf-8'
import allure
import pytest
from params import params
from common.api import Api

@allure.feature('登录模块')
class Test_Login(Api):
    url = params.url + '/Account/Login'
    # 组装通用参数
    data_curr = {"device_type": params.device_type, "effectiveDate": params.effectiveDate, "appid": params.appid,
                 "version_code": params.version_code, "deviceSAMId": params.deviceSAMId, "os": params.os,
                 "version_name": params.version_name, "device_id": params.device_id, "app_type": params.app_type,
                 "type": params.type, "deviceModelStr": params.deviceModelStr, "unitClass": params.unitClass,
                 "model": params.model, "user_push_id": params.user_push_id, "access_token": params.access_token}
    # 组装业务参数
    data_bussi_01 = {"login_name": params.login_name_01, "login_password": params.login_password_01}
    # 组合参数
    data_bussi_01.update(data_curr)
    data_01 = data_bussi_01

    # 用例：用户登录成功
    @pytest.mark.parametrize('url,data', [(url, data_01)])
    @pytest.mark.run(order=1)
    def test_login_success(self, url, data):
        result = Api.login(self, url, data)
        with allure.step('断言'):
            assert result[0].status_code == 200
            assert result[1]['code'] == 0

    # 组装业务参数
    data_bussi_02 = {"login_name": params.login_name_02, "login_password": params.login_password_02}
    # 组合参数
    data_bussi_02.update(data_curr)
    data_02 = data_bussi_02

    # 用例：账号密码错误
    @pytest.mark.parametrize('url,data', [(url, data_02)])
    @pytest.mark.run(order=3)
    def test_login_error(self, url, data):
        result = Api.login(self, url, data)
        with allure.step('断言'):
            assert result[0].status_code == 200
            assert result[1]['code'] == 1

    # 组装业务参数
    data_bussi_03 = {"login_name": params.login_name_03, "login_password": params.login_password_03}
    # 组合参数
    data_bussi_03.update(data_curr)
    data_03 = data_bussi_03

    # 用例：非法设备
    @pytest.mark.parametrize('url,data', [(url, data_03)])
    @pytest.mark.run(order=2)
    def test_login_illegal(self, url, data):
        result = Api.login(self, url, data)
        with allure.step('断言'):
            assert result[0].status_code == 200
            assert result[1]['popMsg'] == '非法设备！'
