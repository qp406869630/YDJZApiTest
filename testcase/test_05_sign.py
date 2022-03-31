# encoding = 'utf-8'
import allure
import pytest
from params import params
from common.api import Api


@allure.feature('签核模块')
class Test_Sign(Api):
    data_start_sign = {"device_type": params.device_type, "fchildno": params.fchildno_01,
                       "classCode": params.classCode_01,
                       "pad_id": params.pad_id_01, "station_code": params.station_code_01,
                       "login_name": params.login_name_01,
                       "station_name": params.station_name_01, "version_name": params.version_name,
                       "className": params.className_01, "isOpenTakePhoto": params.isOpenTakePhoto_01,
                       "app_type": params.app_type, "productname": params.productname_01,
                       "factoryName": params.factoryName_01,
                       "user_name": params.user_name_01, "deviceModelStr": params.deviceModelStr,
                       "relation": params.relation_01, "productno": params.productno_01, "appid": params.appid,
                       "version_code": params.version_code, "factorycode": params.factorycode_01,
                       "deviceSAMId": params.deviceSAMId, "os": params.os, "price": params.price_01,
                       "signType": params.signType_01, "device_id": params.device_id,
                       "access_token": params.access_token,
                       "jc": params.jc_01, "unitClass": params.unitClass, "model": params.model}
    data_get_sign = {"access_token": params.access_token_qh, "login_name": params.login_name_qh,
                     "app_type": params.app_type_qh, "version_name": params.version_name_qh, "os": params.os_qh,
                     "device_id": params.device_id_qh, "sign_id": params.sign_id_qh,
                     "version_code": params.version_code_qh, "model": params.model_qh,
                     "device_type": params.device_type_qh}
    data_saveTmp_sign = {"os": params.os_qh, "device_id": params.device_id_qh, "fchildno": params.fchildno_01,
                         "sign_id": params.sign_id_qh,
                         "user_name": params.user_name_qh, "vaccinecode": params.vaccinecode_qh,
                         "device_type": params.os_qh, "relation": params.relation_01,
                         "access_token": params.access_token_qh, "factorycode": params.factorycode_01,
                         "version_name": params.version_name_qh, "price": params.price_01, "jc": params.jc_01,
                         "model": params.model_qh}
    data_issign_down = {"device_type": params.device_type, "fchildno": params.fchildno_01, "appid": params.appid,
                        "version_code": params.version_code, "deviceSAMId": params.deviceSAMId,
                        "station_code": params.station_code_01, "station_name": params.station_name_01,
                        "login_name": params.login_name_01, "os": params.os, "version_name": params.version_name,
                        "device_id": params.device_id, "access_token": params.access_token, "app_type": params.app_type,
                        "user_name": params.user_name_01, "deviceModelStr": params.deviceModelStr,
                        "unitClass": params.unitClass, "model": params.model, "factorycode": params.factorycode_01,
                        "jc": params.jc_01}
    data_save_sign = {"device_type": params.device_type, "fchildno": params.fchildno_01, "relation": params.relation_01,
                      "pad_id": params.pad_id_01, "factorycode": params.factorycode_01,
                      "login_name": params.login_name_01, "os": params.os, "version_name": params.version_name,
                      "class_code": params.classCode_01, "price": params.price_01, "signType": params.signType_01,
                      "device_id": params.device_id, "vaccinecode": params.vaccinecode_qh,
                      "access_token": params.access_token, "jc": params.jc_01,
                      "isOpenTakePhoto": params.isOpenTakePhoto_01, "model": params.model}
    files = params.files

    # 用例：签核成功
    @pytest.mark.parametrize('url,data_start,data_get,data_saveTmp,data_issign,data_save,files',
                             [(params.url, data_start_sign, data_get_sign, data_saveTmp_sign, data_issign_down,
                               data_save_sign, files)])
    def test_sign_success(self, url, data_start, data_get, data_saveTmp, data_issign, data_save, files):
        # 接种端发起签核
        url1 = url + '/sign/start_tmp_sign_info'
        with allure.step('!--接种端发起签核--!'):
            result01 = Api.start_sign(self, url1, data_start)
        with allure.step('断言'):
            assert result01[0].status_code == 200
            assert result01[1]['success'] is True
        print('接种端发起签核')
        # 签核端开始签核
        url2 = url + '/sign/get_tmp_sign_info'
        with allure.step('！--签核端开始签核--！'):
            result02 = Api.get_sign(self, url2, data_get)
        with allure.step('断言'):
            assert result02[0].status_code == 200
            assert result02[1]['success'] is True
            assert result02[1]['data']['vaccineName'] == '乙肝疫苗(CHO)'
            assert result02[1]['data']['vaccineCode'] == '0201'
            assert result02[1]['data']['factoryName'] == '华北金坦'
        print('签核端开始签核')
        # 签核端完成签核
        url3 = url + '/sign/saveTmpSign'
        with allure.step('！--签核端完成签核--！'):
            result03 = Api.saveTmp_sign(self, url3, data_saveTmp, files)
        with allure.step('断言'):
            assert result02[0].status_code == 200
            assert result03[1]['popMsg'] == '上传成功'
        print('签核端完成签核')
        # 接种端轮询接收签核结果
        url4 = url + '/sign/is_sign_done'
        with allure.step('！--接种端轮询接收签核结果--！'):
            result04 = Api.issign_down(self, url4, data_issign)
        with allure.step('断言'):
            assert result04[0].status_code == 200
            assert result04[1]['success'] is True
            assert result04[1]['data']['vaccineName'] == '乙肝疫苗(CHO)'
            assert result04[1]['data']['vaccineCode'] == '0201'
            assert result04[1]['data']['factoryName'] == '华北金坦'
        print('接种端收到签核结果')
        # 接种端提交签核结果
        url5 = url + '/sign/saveSign'
        with allure.step('！--接种端收到签核结果--！'):
            result05 = Api.save_sign(self, url5, data_save, files)
        with allure.step('断言'):
            assert result05[0].status_code == 200
            assert result05[1]['success'] is True
            assert result05[1]['data']['vaccineName'] == '乙肝疫苗(CHO)'
            assert result05[1]['data']['vaccineCode'] == '0201'
            assert result05[1]['data']['factoryName'] == '华北金坦'
        print('接种端提交签核结果成功')
