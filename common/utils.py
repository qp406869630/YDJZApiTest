# encoding = 'utf-8'
import json
import time

import cx_Oracle
import pymysql

from params import params


class Utils:
    def to_json(self, result):
        result_string = str(result)
        result_json = json.loads(result_string)
        return result_json

    def get_timestamp(self):
        timestamp_ori = time.time()
        timestamp = int(round((timestamp_ori * 1000)))
        return timestamp

    def get_current_time(self):
        current_time = ((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())).split(' '))[0]
        return current_time

    def clear_shotlist(self):
        # 连接数据库
        db = pymysql.connect(host='192.168.1.45', user='root', password='epi_ningxia', db='epicloud_shandong_3701')
        # 获取操作游标
        cursor = db.cursor()

        # 查询接种记录
        fchildno = params.fchildno_01
        cursor.execute(f'select * from 3701_child_shotlist where fchildno="{fchildno}" and PRODUCTNO="0201"')
        result = cursor.fetchall()
        if result is ():
            pass
        else:
            try:
                # 删除接种记录
                cursor.execute(f'delete from 3701_child_shotlist where fchildno="{fchildno}" and PRODUCTNO="0201"')
                db.commit()
            except:
                pass

        # 断开数据库
        cursor.close()
        db.close()

    def clear_inquiry(self):
        # 连接数据库
        db = pymysql.connect(host='192.168.1.45', user='root', password='epi_ningxia', db='epicloud_shandong_3701')
        oracle = cx_Oracle.connect('data_center_test2021', 'data_center_test2021', '192.168.1.6:1521/devdb')
        # 获取操作游标
        cursor = db.cursor()
        cursor_oracle = oracle.cursor()

        # 查询健康询问记录
        fchildno = params.fchildno_01
        cursor.execute(f'select inquiryid from 3701_child_inquiry where fchildno="{fchildno}"')
        result = cursor.fetchall()
        if result is ():
            pass
        else:
            # 删除移动库健康询问记录
            try:
                cursor.execute(
                    f'delete from 3701_child_inquiry_answer where inquiryid in (select inquiryid from 3701_child_inquiry where fchildno="{fchildno}")')
                # db.commit()
                cursor.execute(f'delete from 3701_child_inquiry where fchildno="{fchildno}"')
                db.commit()
            except:
                pass
        cursor_oracle.execute(f'select * from NEW_EPI_SHANDONG.vaccine_log_answers where fchildno = {fchildno}')
        result1 = cursor_oracle.fetchall()
        cursor_oracle.execute(f'select id from NEW_EPI_SHANDONG.vaccine_reply_records where fchildno = {fchildno}')
        result2 = cursor_oracle.fetchall()
        if result1 is ():
            pass
        else:
            cursor_oracle.execute(f'delete from NEW_EPI_SHANDONG.vaccine_log_answers where fchildno = {fchildno}')
            oracle.commit()

        if result2 is ():
            pass
        else:
            cursor_oracle.execute(
                f'delete from NEW_EPI_SHANDONG.vaccine_question_answers where record_id in (select id from NEW_EPI_SHANDONG.vaccine_reply_records where fchildno = {fchildno})')
            # oracle.commit()
            cursor_oracle.execute(f'delete from NEW_EPI_SHANDONG.vaccine_reply_records where fchildno = {fchildno}')
            oracle.commit()
        # 断开数据库
        cursor.close()
        db.close()

    def clear_record(self):
        # 连接数据库
        db = pymysql.connect(host='192.168.1.45', user='root', password='epi_ningxia', db='epicloud_shandong_3701')
        oracle = cx_Oracle.connect('data_center_test2021', 'data_center_test2021', '192.168.1.6:1521/devdb')
        # 获取操作游标
        cursor = db.cursor()
        cursor_oracle = oracle.cursor()
        name_01 = params.name_01
        cursor.execute(f'SELECT fchildno FROM 3701_child_info WHERE NAME = "{name_01}"')
        result = cursor.fetchall()
        if result is ():
            pass
        else:
            try:
                cursor.execute(f'delete from 3701_child_info where NAME = "{name_01}"')
                # db.commit()
                cursor.execute(
                    f'delete from child_cid_ind where cardid in (select cardid from child_info_ind where fchildno in (SELECT fchildno FROM 3701_child_info WHERE NAME = "{name_01}"))')
                # db.commit()
                cursor.execute(
                    f'delete from child_info_ind where fchildno in (SELECT fchildno FROM 3701_child_info WHERE NAME = "{name_01}")')
                db.commit()
                cursor_oracle.execute(f"delete from NEW_EPI_SHANDONG.EPI_CHILDINFO where NAME = '{name_01}'")
                oracle.commit()
            except:
                pass
        cursor.close()
        cursor_oracle.close()
        # 断开数据库
        db.close()
        oracle.close()
