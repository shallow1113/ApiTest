import pytest

# @pytest.mark.parametrize('key',['values'])
# def test_parametrize_01(key):
#      print('我是'+ key)


# @pytest.mark.parametrize(key,values)
# @pytest.mark.parametrize("name", ["老武"])
# def test_parametrize_01(name):
#     print("我是" + name)

#
# @pytest.mark.parametrize("name", ["老武"])
# def test_parametrize_01(name):
#     assert name == "老武"

# 一个参数，多个值，测试用例会把每个值赋给参数，进行测试用例的执行，有
# 几个值，测试用例执行几次
# @pytest.mark.parametrize("hero_name", ["安琪拉", "黄忠", "小乔"])
# def test_parametrize_01(hero_name):
#     assert hero_name == "安琪拉"

# 参数值为字典
@pytest.mark.parametrize("hero", [{"name": "安琪拉", "word": "火焰是我最喜欢的玩具"}, {"name": "黄忠"}, {"name": "小乔"}])
def test_parametrize_01(hero):
    print(hero["name"])
    print(hero["word"])

# @pytest.mark.parametrize("hero", [{"name": "安琪拉",}, {"name": "黄忠"}, {"name": "小乔"}])
# def test_parametrize_01(hero):
#     print(hero["name"])
#
