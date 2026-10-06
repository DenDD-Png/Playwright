from playwright.sync_api import sync_playwright


def test_run():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://demoqa.com/text-box")

        page.fill("#userName", "John Doe")
        page.fill("#userEmail", "john.doe@example.com")
        page.fill("#currentAddress", "123 Elm St")
        page.fill("#permanentAddress", "456 Oak St")

        page.click("#submit")

        output = page.locator("#output")
        output.wait_for(timeout=5000)

        assert output.text_content().strip() == (
            "Name:John Doe\n"
            "Email:john.doe@example.com\n"
            "Current Address:123 Elm St\n"
            "Permanent Address:456 Oak St"
        )

        browser.close()