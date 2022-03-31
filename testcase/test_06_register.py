# encoding = 'utf-8'
import allure
import pytest

from common.api import Api
from params import params


@allure.feature('接种登记模块')
class Test_Register(Api):
    url = params.url + '/appshot/shotinfo'
    # 组装通用参数
    data_curr = {"device_type": params.device_type, "appid": params.appid, "version_code": params.version_code,
                 "deviceSAMId": params.deviceSAMId,
                 "deleteShotIds": params.deleteShotIds, "os": params.os, "version_name": params.version_name,
                 "device_id": params.device_id,
                 "app_type": params.app_type, "deviceModelStr": params.deviceModelStr,
                 "unitClass": params.unitClass,
                 "model": params.model, "access_token": params.access_token}
    # 组装业务参数
    data_bussi_01 = {"fchildno": params.fchildno_01,
                     "data": params.data_01,
                     "login_name": params.login_name_01, "station_name": params.station_name_01,
                     "station_code": params.station_code_01,
                     "user_name": params.user_name_01}
    # 组合参数
    data_bussi_01.update(data_curr)
    data_01 = data_bussi_01

    # 用例：成功登记（乙肝CHO）
    @pytest.mark.parametrize('url,data', [(url, data_01)])
    def test_register_success(self, url, data):
        result = Api.register(self, url, data)
        with allure.step('断言'):
            assert result[0].status_code == 200
            assert result[1]['code'] == 0
            assert result[1]['popMsg'] == '新增成功！'
