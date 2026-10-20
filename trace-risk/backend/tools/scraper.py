from playwright.sync_api import sync_playwright

def scrape_zaubacorp(url: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        content = page.content()
        browser.close()
        return content[:10000]  # first 10k chars