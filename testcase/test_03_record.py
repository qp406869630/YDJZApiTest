# encoding = 'utf-8'
import allure
import pytest
from params import params
from common.utils import Utils
from common.api import Api


@allure.feature('建档模块')
class Test_Record(Api):
    url = params.url + '/app/childinfo'
    # 获取时间戳
    timestamp = Utils().get_timestamp()
    # 获取当前时间
    current_time = Utils().get_current_time()
    # 组装通用参数
    data_curr = {"proofno": params.proofno}
    # 组装业务参数
    data_bussi_01 = {"loginname": params.login_name_01, "unitCode": params.unitCode_01,
                     "unitName": params.user_name_01,
                     "cardtype": params.cardtype_01, "mothercardtype": params.mothercardtype_01,
                     "fathercardtype": params.fathercardtype_01, "cardid": params.cardid_01, "name": params.name_01,
                     "sex": params.sex_01, "birthday": params.birthday_01, "resiType": params.resiType_01,
                     "nationnality": params.nationnality_01,
                     "nationnalityname": params.nationnalityname_01,
                     "nationnalityDisabled": params.nationnalityDisabled_01, "createdate": current_time,
                     "motherHbsag": params.motherHbsag_01, "childHbsag": params.childHbsag_01,
                     "childAntibody": params.childAntibody_01,
                     "address": params.address_01,
                     "habiaddr": params.habiaddr_01,
                     "birthHour": params.birthHour_01, "birthMin": params.birthMin_01,
                     "committeeCode": params.committeeCode_01, "mobilephone": params.mobilephone_01,
                     "allPhone": params.allPhone_01, "peopleClass": params.peopleClass_01,
                     "habiaddrDetail": params.habiaddrDetail_01,
                     "addressDetail": params.addressDetail_01,
                     "birthtime": params.birthtime_01, "timestamp": timestamp}
    # 组合参数
    data_bussi_01.update(data_curr)
    data_01 = data_bussi_01
    headers = {"Referer": "http://192.168.1.45:94/EpicardCloudPlatWeb_shanDongAppH5/",
               "Content-Type": "application/x-www-form-urlencoded",
               "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.2; CT-TPC101 Build/2.6.1-21040120; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Safari/537.36",
               "X-Requested-With": "com.shensu.ymy_jz"}

    # 用例：建档成功
    @pytest.mark.parametrize('url,data,headers', [(url, data_01, headers)])
    def test_record_success(self, url, data, headers):
        result = Api.record(self, url, data)
        with allure.step('断言'):
            assert result[0].status_code == 200
            assert result[1]['name'] == '接口自动化b'
