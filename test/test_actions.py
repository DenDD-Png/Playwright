from playwright.sync_api import Page, expect

def test_main_actions(home, result):
    #page.get_by_placeholder("Искать на Литрес").fill("python")
    #page.get_by_role("button", name="Найти").click()
    #expect(page).to_have_url(f"https://www.litres.ru/search/?q={query}")
    #books = page.get_by_test_id("art__wrapper")
    #page.check("label[for='languages-ru']")
    query = "Игра Престолов"
    home.search(query, submit_with_enter=True)
    result.should_be_opened(query)
    expect(result.result_title).to_contain_text(query)
    expect(result.books).to_have_count(24, timeout=5000)
    result.apply_russian_filter()
    expect(result.russian_chip).to_be_visible()


def test_main_actions_with_dblclic(page: Page):
    page.get_by_placeholder("Искать на Литрес").fill("python")
    page.get_by_role("button", name="Найти").click()
    expect(page).to_have_url("https://www.litres.ru/search/?q=python")
    page.locator("xpath=(//div[@class='uik-toggle-KN8WZd'])[1]").dblclick()
    page.wait_for_timeout(timeout=1500)
    page.screenshot(path="screenshot/litresscren.png")
    page.locator("xpath=//*[@aria-description='Книги, которые можно взять по Литрес: Абонементу']").click()
    page.wait_for_timeout(timeout=1500)
    page.screenshot(path="screenshot/litresscrendb.png")
    page.pause()

#В случае с литрес этот метод почему то не работает, но выдает успешный ответ
def test_checkbox_litres(page: Page):
    page.get_by_placeholder("Искать на Литрес").fill("python")
    page.get_by_role("button", name="Найти").click()
    expect(page).to_have_url("https://www.litres.ru/search/?q=python")
    page.locator("xpath=//*[@id='languages-ru']")
    page.pause()

def test_page_check(page: Page):
    page.get_by_placeholder("Искать на Литрес").fill("python")
    page.get_by_role("button", name="Найти").click()
    expect(page).to_have_url("https://www.litres.ru/search/?q=python")
    page.check("label[for='languages-ru']")
    # Закрывает всплывающие окно
    page.locator("button:has-text('Принять')").click()
    page.wait_for_timeout(timeout=1500)
    page.screenshot(path="screenshot/litrescheck.png")

