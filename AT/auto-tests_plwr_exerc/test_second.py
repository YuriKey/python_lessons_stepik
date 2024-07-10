import pytest
import time
from playwright.sync_api import Page, expect


@pytest.mark.plwr()
def test_wiki(page: Page):
    page.goto('https://gymlog.ru/profile/login/') #Перейди по адресу.
    page.locator('#email').fill('User412') #Заполни элемент с id = email значением User412.
    page.locator('#password').fill('k9L-hL') #Заполни элемент с id = password значением k9L-hL.
    page.get_by_role('button', name='Войти').click() #Нажми кнопку с текстом "Войти".
    time.sleep(10) #Подожди 10 секунд.

