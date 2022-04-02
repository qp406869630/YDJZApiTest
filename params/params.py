# encoding = 'utf-8'
import os

imgpath = os.path.dirname(os.path.realpath(__file__))
img_sign = open(imgpath + '/sign.png', 'rb')
img_photo = open(imgpath + '/photo.png', 'rb')
# 接口api
url = 'http://192.168.1.45:94/EpicardCloudPlat_shandong'

# --------通用参数-data_curr--------
device_type = '0'
effectiveDate = '2099-12-31 00:00:00'
appid = 'f019c357bc9f256c24b9017c299456df'
version_code = '2'
deviceSAMId = ''
os = 'android'
version_name = '2.0.0'
device_id = '53ea7bf626ed9cd5'
app_type = '1'  # 1代表Android，支付的时候使用
type = '2'
deviceModelStr = ''  # 扫码墩标识码
unitClass = '1'
model = 'CT-TPC101'  # 手机厂商
user_push_id = '1104a8979261c7cb5f1'
access_token = 'Obr4CjMb1MnFmXQ6Ylj5sGbiq45/ZjGBinUTyf2XWzzwHUm5v6rMB7hXZ0OtCtEQrvZhCBysEUE\\u003d\\n'
idType = '03'
birth = ''
name = ''
sex = ''
type_health = 'APP03'
childInquiry = '1'
resultRemark = ''
deleteShotIds = ''
proofno = ''

# --------业务参数-data_bussi--------
# 受种者信息
login_name_01 = 'qp001'
login_password_01 = '2476821d34ec17e549a8f1b0d5396c65'
user_name_01 = '秦鹏001'
fchildno_01 = '370102010200000035'
cardId_01 = '3000'
login_name_02 = 'qp111'
login_password_02 = '2476821d34ec17e549a8f1b0d5396c65'
login_name_03 = 'qd_qp'
login_password_03 = '2476821d34ec17e549a8f1b0d5396c65'

# 门诊信息
station_name_01 = '十亩园社区卫生服务站预防接种门诊'
station_code_01 = '3701020102'
unitCode_01 = '3701020102'
unitCodeNew_01 = '3701020102'

# 健康状况询问
ansterList_01 = [{'showIndex': 2, 'answer': '否', 'healthid': 1},
                 {'showIndex': 2, 'answer': '否', 'healthid': 2},
                 {'showIndex': 2, 'answer': '否', 'healthid': 3},
                 {'showIndex': 2, 'answer': '否', 'healthid': 4},
                 {'showIndex': 2, 'answer': '否', 'healthid': 5},
                 {'showIndex': 2, 'answer': '否', 'healthid': 6},
                 {'showIndex': 2, 'answer': '否', 'healthid': 7},
                 {'showIndex': 2, 'answer': '否', 'healthid': 8},
                 {'showIndex': 2, 'answer': '否', 'healthid': 9},
                 {'showIndex': 2, 'answer': '否', 'healthid': 10},
                 {'showIndex': 2, 'answer': '否', 'healthid': 11},
                 {'showIndex': 2, 'answer': '否', 'healthid': 12},
                 {'showIndex': 2, 'answer': '否', 'healthid': 13}]
# 接种登记记录
data_01 = '[{\"bactcode\":\"02\",\"bactname\":\"乙肝疫苗\",\"corpcode\":\"33\",\"corpname\":\"华北金坦\",\"inocSource\":\"S\",\"jc\":\"1\",\"productname\":\"乙肝疫苗(CHO)\",\"productno\":\"0201\",\"result\":1,\"signid\":\"d30405660f7a41e9b10346729879d054\"}]'
monitorcode_01 = '88888888888888888888'

# 建档
unitName_01 = '十亩园社区卫生服务站预防接种门诊'
cardtype_01 = '03-护照'
mothercardtype_01 = '01-居民身份证'
fathercardtype_01 = '01-居民身份证'
cardid_01 = '4000'
name_01 = '接口自动化b'
sex_01 = '1'
birthday_01 = '2000-01-01'
resiType_01 = '1'
nationnality_01 = '156-中国'
nationnalityname_01 = '中国'
nationnalityDisabled_01 = 'false'
motherHbsag_01 = '9'
childHbsag_01 = '9'
childAntibody_01 = '9'
address_01 = '3700000000,3701000000,3701020000,3701020100,123123,山东省.济南市.历下区.解放路街道办事处.123123'
habiaddr_01 = '3700000000,3701000000,3701020000,3701020100,123123,山东省.济南市.历下区.解放路街道办事处.123123'
birthHour_01 = ''
birthMin_01 = ''
committeeCode_01 = '370102010201-12'
mobilephone_01 = '17500000000'
allPhone_01 = '17500000000'
peopleClass_01 = '01'
habiaddrDetail_01 = '123123'
addressDetail_01 = '123123'
birthtime_01 = ''

# 签核-接种端发起签核
classCode_01 = '02'
pad_id_01 = 'f019c357bc9f256c24b9017c299456df'
className_01 = '乙肝疫苗'
isOpenTakePhoto_01 = '1'
productname_01 = '乙肝疫苗(CHO)'
factoryName_01 = '华北金坦'
relation_01 = '本人'
productno_01 = '0201'
factorycode_01 = '33'
price_01 = ''
signType_01 = '1'
jc_01 = '1'

# 签核-签核端开始签核
access_token_qh = 'MdzCgSbPkac+HbIYmAlwFXEua+wA7k4zC5/WCmhPV0HzCZL3quSDzIvaVWnRs1vK/KhaKF+Cm40\\u003d\\n'
login_name_qh = 'bc3e6b0280669dac480c1d5ad1554def'
app_type_qh = '1'
version_name_qh = '2.0.0'
os_qh = 'android'
device_id_qh = 'f6aaa17a04e4012d'
sign_id_qh = 'bc3e6b0280669dac480c1d5ad1554def'
version_code_qh = '2'
model_qh = 'rk3368'
device_type_qh = '1002'

# 签核-签核端完成签核
user_name_qh = 'bc3e6b0280669dac480c1d5ad1554def'
vaccinecode_qh = '0201'
files = [('files', ('photo.png', img_photo, 'image/png')), ('files', ('sign.png', img_sign, 'image/png'))]