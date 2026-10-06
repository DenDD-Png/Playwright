from playwright.sync_api import Page, expect


def test_mani_page_title(page: Page):
    page.goto("https://www.litres.ru/")
    assert page.title() == 'Литрес – сервис электронных и аудиокниг, скачать в fb2 и mp3, читать и слушать онлайн на Litres'

def test_audiobook_page_title(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_role("link", name="Аудиокниги").first.click()
    expect(page).to_have_title("Аудиокниги – слушать онлайн или скачать в mp3 на Литрес")


def test_audiobook_page_title_xpath(page: Page):
    page.goto("https://www.litres.ru/")
    page.locator("xpath=//a[@class=\"LowerMenu-module-scss-module__Sc38ga__lowerMenu__item\"][contains(text(),\"Аудиокниги\")]").click()
    expect(page).to_have_title("Аудиокниги – слушать онлайн или скачать в mp3 на Литрес")
