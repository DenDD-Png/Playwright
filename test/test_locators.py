from playwright.sync_api import Page, expect

def test_locator_role(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_role("link", name="С чего начать").click()
    expect(page).to_have_title("Рекомендации для вас- ищите на Литрес")
    page.get_by_role("button", name="Найти").click()
    expect(page.get_by_text("александра маринина")).to_be_visible()

def test_locator_but(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_role("button", name="Найти").click()
    expect(page.get_by_text("александра маринина")).to_be_visible()

def test_locator_placeholder(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_placeholder("Искать на Литрес").fill("Игра Престолов")
    page.keyboard.press("Enter")
    expect(page.get_by_text("Результаты поиска «игра престолов»")).to_be_visible()

def test_locator_id(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_test_id("tab-login").click()
    expect(page.get_by_text("Почта или логин")).to_be_visible()

def test_locator_alt(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_role("link", name="С чего начать").click()
    expect(page).to_have_title("Рекомендации для вас- ищите на Литрес")
    page.get_by_alt_text("Логотип Литрес").click()
    expect(page).to_have_title("Рекомендации для вас- ищите на Литрес")

def test_locator_altushka(page: Page):
    page.goto("https://www.litres.ru/landing/PROMOTIONS2025/")
    page.get_by_alt_text("Логотип Литрес").click()
    expect(page).to_have_url("https://www.litres.ru/")
    expect(page.get_by_text("С чего начать")).to_be_visible()

def test_locator_yuotub(page: Page):
    page.goto("https://www.litres.ru/")
    expect(page.locator("xpath= //img[ @ alt = \"YouTube\"]")).to_be_visible()




