class MultipleWindow:
    def __init__(self, page):
        self.page = page
        self.click_here_link = page.get_by_role("link", name="Click Here")

    def open_new_window(self):
        self.page.goto("https://the-internet.herokuapp.com/windows")
        self.click_here_link.wait_for(timeout=60_000)
        with self.page.context.expect_page() as new_page_info:
            self.click_here_link.click()
        new_page = new_page_info.value
        new_page.get_by_role("heading", name="New Window").wait_for(timeout=60_000)
        return new_page

    def open_url(self, url):
        self.page.goto(url, wait_until="commit")
