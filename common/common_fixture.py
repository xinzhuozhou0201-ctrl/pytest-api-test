#common\common_fixture.py
import pytest
@pytest.fixture(scope='class',autouse=True)
def exe_database_sql():
    print('执行sql')
    yield
    print('关闭sql')