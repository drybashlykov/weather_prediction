from playwright.sync_api import sync_playwright

def get_table():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://www.wunderground.com/history/daily/il/haifa/LLHA/date/2015-1-7')
        
        # Wait for the table to appear
        page.wait_for_selector('table')
        
        # Get the table's HTML
        table_html = page.inner_html('table')
        print(table_html)
        
        browser.close()