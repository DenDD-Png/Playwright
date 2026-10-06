from playwright.sync_api import Page, expect

def test_main_actions(page: Page):
    page.get_by_placeholder("Искать на Литрес").fill("python")
    page.get_by_role("button", name="Найти").click()
    expect(page).to_have_url("https://www.litres.ru/search/?q=python")

