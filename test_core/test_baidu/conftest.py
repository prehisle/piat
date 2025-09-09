import pytest


@pytest.fixture(scope="session")
def page_user_a(auth_page):
    page, context = auth_page.get_logged_in_page('baidu', 'user_a')
    yield page
    context.close()

@pytest.fixture(scope="session")
def page_user_b(auth_page):
    page, context = auth_page.get_logged_in_page('baidu', 'user_b')
    yield page
    context.close()