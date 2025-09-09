import pytest

from comm.pw.browser_helper import auth_page



@pytest.fixture(scope="session")
def page(auth_page):
    page, context = auth_page.get_logged_in_page('educity', '17775747276')
    yield page
    context.close()

