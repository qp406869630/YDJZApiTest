# encoding = 'utf-8'
import allure
import pytest

from common.api import Api
from params import params


@allure.feature('识别模块')
class Test_Recog(Api):
    url = params.url + '/home/childinfo'
    # 组装通用参数
    data_curr = {"device_type": params.device_type, "appid": params.appid, "idType": params.idType,
                 "version_code": params.version_code, "deviceSAMId": params.deviceSAMId, "os": params.os,
                 "version_name": params.version_name, "device_id": params.device_id, "birth": params.birth,
                 "name": params.name, "app_type": params.app_type, "sex": params.sex,
                 "deviceModelStr": params.deviceModelStr, "unitClass": params.unitClass, "model": params.unitClass,
                 "access_token": params.access_token}
    # 组装业务参数
    data_bussi_01 = {"user_name": params.user_name_01,
                     "login_name": params.login_name_01, "cardId": params.cardId_01,
                     "station_name": params.station_name_01,
                     "station_code": params.station_code_01}
    # 组合参数
    data_bussi_01.update(data_curr)
    data_01 = data_bussi_01

    # 用例：成功识别受种者
    @pytest.mark.parametrize('url,data', [(url, data_01)])
    def test_recog_success(self, url, data):
        result = Api.recog(self, url, data)
        with allure.step('断言'):
            assert result[0].status_code == 200
            assert result[1]['code'] == 0
            assert result[1]['data']['childinfos'][0]['cardId'] == self.data_01['cardId']
