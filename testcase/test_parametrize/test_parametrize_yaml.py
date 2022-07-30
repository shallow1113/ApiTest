import pytest

from utils.read_data import get_data

#
# @pytest.mark.parametrize('name',get_data['heros_name'])
# def test_parametrize_02(name):
#     print(name)
#

@pytest.mark.parametrize('name,word',get_data['heros_name_word'])
def test_parametrize_02(name,word):
    print(f'{name}的台词是{word}')