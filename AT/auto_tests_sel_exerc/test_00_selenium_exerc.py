from selenium import webdriver
import pytest
import pywinauto


@pytest.mark.smoke
def test_one_is_one(separator, all_tests):
    print('hello morpheus')
    assert 1 == 1


@pytest.mark.skip('minor_defect')  ##Пропустить выполнение, указав причину.
def test_two_is_two(separator):
    print('hello trin')
    assert 2 == 1


@pytest.mark.regression
def test_three_is_three(separator):
    print('hello neo')
    assert 3 == 3
