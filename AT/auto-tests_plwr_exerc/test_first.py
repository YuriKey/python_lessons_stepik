from playwright.sync_api import Page, expect

#@pytest.mark.plwr()
def test_wiki(page: Page):
    page.goto('https://www.wikipedia.org/')
    page.get_by_role('link', name='русский').click()
    expect(page.get_by_text('Добро пожаловать в Википедию')).to_be_visible()

#@pytest.mark.plwr()
def test_wiki2(page: Page):
    page.goto('https://ru.wikipedia.org/wiki/Обсуждение_Википедии:Содержание')
    expect(page.get_by_text('Обсуждение Википедии:Содержание')).to_be_visible()

#@pytest.mark.plwr()
def test_wiki3(page: Page):
    page.goto('https://www.wikipedia.org/') #Открыть страницу.
    page.get_by_role('link', name='русский').click() #Найти и кликнуть на ссылку с текстом "русский".
    page.get_by_role('link', name='содержание').click() #Найти и кликнуть на ссылку с текстом "содержание".
    page.locator('#ca-talk').click() #Найти и кликнуть на элемент с id = ca-talk.
    expect(page.locator('#firstHeading')).to_have_text('Обсуждение Википедии:Содержание') #Проверить содержится ли в
    # элементе с id = firstHeading текст 'Обсуждение Википедии:Содержание'.

