import pytest
@pytest.fixture()  ## pre-conditions
def separator():
    print('=' * 10)
    yield 'value'
    print(' test finished')


@pytest.fixture(scope='session')  ##Функция выполняется, когда ее вызвали, работает в рамках одной сессии. По
# умолчанию scope = 'function'
def all_tests():
    print('DataBaseEnable')
    yield
    print('DataBaseDisable')

