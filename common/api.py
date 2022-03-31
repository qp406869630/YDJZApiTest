# encoding = 'utf-8'
import json
from common.utils import Utils
import requests
from common.SMUtil_YMY import SMUtil_YMY
import allure

class Api:
    def login(self, url, data):
        with allure.step('把data转换为json_str'):
            data_json = json.dumps(data, ensure_ascii=False)
        with allure.step('参数加密'):
            param_enc = SMUtil_YMY().YMY_Encrypt(data_json)
        with allure.step('组装请求参数'):
            param = str(param_enc)
            params = {'params': param}
        with allure.step('发送请求'):
            response = requests.get(url, params=params)
        with allure.step('解密'):
            result = SMUtil_YMY().YMY_Decrypt(response.text)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(result)
        return [response, result_json]

    def recog(self, url, data):
        with allure.step('把data转换为json_str'):
            data_json = json.dumps(data, ensure_ascii=False)
        with allure.step('参数加密'):
            param_enc = SMUtil_YMY().YMY_Encrypt(data_json)
        with allure.step('组装请求参数'):
            param = str(param_enc)
            params = {'params': param}
        with allure.step('发送请求'):
            response = requests.get(url, params=params)
        with allure.step('解密'):
            result = SMUtil_YMY().YMY_Decrypt(response.text)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(result)
        return [response, result_json]

    def health(self, url, data, fchildno):
        with allure.step('把data转换为json_str'):
            data_json = json.dumps(data, ensure_ascii=False)
        with allure.step('参数加密'):
            param_enc = SMUtil_YMY().YMY_Encrypt(data_json)
        with allure.step('组装请求参数'):
            param = str(param_enc)
            params = {'params': param}
            childno = {'fchildno': fchildno}
            params.update(childno)
        with allure.step('发送请求'):
            response = requests.post(url, data=params)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(response.text)
        return [response, result_json]

    def register(self, url, data):
        with allure.step('把data转换为json_str'):
            data_json = json.dumps(data, ensure_ascii=False)
        with allure.step('参数加密'):
            param_enc = SMUtil_YMY().YMY_Encrypt(data_json)
        with allure.step('组装请求参数'):
            param = str(param_enc)
            params = {'params': param}
        with allure.step('发送请求'):
            response = requests.post(url, data=params)
        with allure.step('解密'):
            result = SMUtil_YMY().YMY_Decrypt(response.text)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(result)
        return [response, result_json]

    def scan(self, url, data):
        with allure.step('把data转换为json_str'):
            data_json = json.dumps(data, ensure_ascii=False)
        with allure.step('参数加密'):
            param_enc = SMUtil_YMY().YMY_Encrypt(data_json)
        with allure.step('组装请求参数'):
            param = str(param_enc)
            params = {'params': param}
        with allure.step('发送请求'):
            response = requests.get(url, params=params)
        with allure.step('解密'):
            result = SMUtil_YMY().YMY_Decrypt(response.text)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(result)
        return [response, result_json]

    def record(self, url, data):
        with allure.step('把data转换为json_str'):
            data_json = json.dumps(data, ensure_ascii=False)
        with allure.step('参数加密'):
            param_enc = SMUtil_YMY().YMY_Encrypt(data_json)
        with allure.step('组装请求参数'):
            param = str(param_enc)
            params = {'params': param}
        with allure.step('发送请求'):
            response = requests.post(url, data=params)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(response.text)
        return [response, result_json]

    def start_sign(self, url, data):
        with allure.step('把data转换为json_str'):
            data_json = json.dumps(data, ensure_ascii=False)
        with allure.step('参数加密'):
            param_enc = SMUtil_YMY().YMY_Encrypt(data_json)
        with allure.step('组装请求参数'):
            param = str(param_enc)
            params = {'params': param}
        with allure.step('发送请求'):
            response = requests.get(url, params=params)
        with allure.step('解密'):
            result = SMUtil_YMY().YMY_Decrypt(response.text)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(result)
        return [response, result_json]

    def get_sign(self, url, data):
        with allure.step('把data转换为json_str'):
            data_json = json.dumps(data, ensure_ascii=False)
        with allure.step('参数加密'):
            param_enc = SMUtil_YMY().YMY_Encrypt(data_json)
        with allure.step('组装请求参数'):
            param = str(param_enc)
            params = {'params': param}
        with allure.step('发送请求'):
            response = requests.get(url, params=params)
        with allure.step('解密'):
            result = SMUtil_YMY().YMY_Decrypt(response.text)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(result)
        return [response, result_json]

    def saveTmp_sign(self, url, data, files):
        with allure.step('发送请求'):
            response = requests.post(url, data=data, files=files)
        with allure.step('解密'):
            result = SMUtil_YMY().YMY_Decrypt(response.text)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(result)
        return [response, result_json]

    def issign_down(self, url, data):
        with allure.step('把data转换为json_str'):
            data_json = json.dumps(data, ensure_ascii=False)
        with allure.step('参数加密'):
            param_enc = SMUtil_YMY().YMY_Encrypt(data_json)
        with allure.step('组装请求参数'):
            param = str(param_enc)
            params = {'params': param}
        with allure.step('发送请求'):
            response = requests.get(url, params=params)
        with allure.step('解密'):
            result = SMUtil_YMY().YMY_Decrypt(response.text)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(result)
        return [response, result_json]

    def save_sign(self, url, data, files):
        with allure.step('发送请求'):
            response = requests.post(url, data=data, files=files)
        with allure.step('解密'):
            result = SMUtil_YMY().YMY_Decrypt(response.text)
        with allure.step('返回请求结果'):
            result_json = Utils().to_json(result)
        return [response, result_json]
