import allure
import pytest
from api.api import mobile_query
from utils.read import base_data

url = base_data.read_ini()['host']['api_sit_url']
@allure.epic("数据进制项目")
@allure.feature('手机号模块')

class TestMobile:
    @allure.story('杭州的手机号story')
    @allure.title('c测试手机归属地title')
    @allure.testcase('www.baidu.com',name= '接口地址testcase')
    @allure.issue('www.baidu.com',name= '缺陷地址issue')
    @allure.link('www.baidu.com', name='链接地址link')
    @allure.description('当前手机号是13456755448，归属地是杭州的description')
    @allure.step('先进行归属地操作step')
    @allure.severity('重要')
    def test_mobile(self):
        param = base_data.read_data()["mobile_belong"]
        result = mobile_query(param)
        assert result.success is True

        assert result.body['status'] == 0
        assert result.body['msg'] == "ok"
        assert result.body['result']["shouji"] == "13456755448"
        assert result.body['result']["province"] == "浙江"
        assert result.body['result']["city"] == "杭州"
        assert result.body['result']["company"] == "中国移动"
        assert result.body['result']["cardtype"] is None
        assert result.body['result']["areacode"] == "0571"

    @allure.title('c测试手机归属地mobile2')
    @allure.testcase('www.baidu.com', name='接口地址testcase')
    @allure.issue('www.baidu.com', name='缺陷地址issue')
    @allure.link('www.baidu.com', name='链接地址link')
    @allure.description('当前手机号是13400000000，归属地是安徽的description')
    @allure.step('先进行归属地操作step')
    @allure.severity('重要')
    def test_mobile2(self):
        param = base_data.read_data()["mobile_belong"]
        result = mobile_query(param)
        assert result.success is True

        assert result.body['status'] == 0
        assert result.body['msg'] == "ok"
        assert result.body['result']["shouji"] == "13456755448"
        assert result.body['result']["province"] == "浙江12"
        assert result.body['result']["city"] == "杭州"
        assert result.body['result']["company"] == "中国移动"
        assert result.body['result']["cardtype"] is None
        assert result.body['result']["areacode"] == "0571"