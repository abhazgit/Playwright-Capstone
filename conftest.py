from datetime import datetime, timezone
from pathlib import Path
import re

import pytest
import requests


@pytest.fixture
def api_client():
    session = requests.Session()
    yield session
    session.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    page = item.funcargs.get("page")
    if page is None or page.is_closed():
        return

    screenshots_dir = Path(item.config.rootpath) / "screenshots"
    screenshots_dir.mkdir(exist_ok=True)
    test_name = re.sub(r"[^A-Za-z0-9_\-]", "_", item.name)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    page.screenshot(path=str(screenshots_dir / f"{test_name}_{timestamp}.png"), full_page=True)
