# encoding = 'utf-8'
import allure
import pytest
from params import params
from common.utils import Utils
from common.api import Api


@allure.feature('健康询问模块')
class Test_Health(Api):
    url = params.url + '/HealthStatus/save'
    fchildno = params.fchildno_01
    # 获取时间戳
    timestamp = Utils().get_timestamp()
    # 组装通用参数
    data_curr = {'type': params.type_health, 'childInquiry': params.childInquiry,
                 'resultRemark': params.resultRemark, "access_token": params.access_token}
    # 组装业务参数
    data_bussi_01 = {'fchildno': fchildno, 'unitCode': params.unitCode_01,
                     'unitCodeNew': params.unitCodeNew_01, 'loginName': params.login_name_01,
                     'timestamp': timestamp,
                     'ansterList': params.ansterList_01}
    # 组合参数
    data_bussi_01.update(data_curr)
    data_01 = data_bussi_01

    # 用例：成功提交询问结果
    @pytest.mark.parametrize('url,data,fchildno', [(url, data_01, fchildno)])
    def test_health_success(self, url, data, fchildno):
        result = Api.health(self, url, data, fchildno)
        with allure.step('断言'):
            assert result[0].status_code == 200
            assert result[1]['success'] is True
