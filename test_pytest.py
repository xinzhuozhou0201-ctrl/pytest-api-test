import pytest

@pytest.fixture(scope ="function",name = 'data')
def person_data(request):
    print("前置")
    yield 's'
    print('后置')


class TestParams:
    def test_demo(self,data):
        print(data)
        print("test_demo测试用例")
