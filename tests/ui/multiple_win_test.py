import pytest

from pages.multiple_windows import MultipleWindow


class TestMultipleWindow:
    @pytest.mark.smoke
    def test_open_new_window(self, page):
        multiple_window = MultipleWindow(page)
        new_page = multiple_window.open_new_window()

        assert new_page.url == "https://the-internet.herokuapp.com/windows/new"
        assert new_page.get_by_role("heading", name="New Window").is_visible()
