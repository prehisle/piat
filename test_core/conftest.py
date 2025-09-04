import pytest

from olymat.utils.ctx_helper import make_default_ctx

from .config import get_g_conf
from .browser_helper import SimpleBrowserAuth

@pytest.fixture(scope="session")
def cfg():
    return get_g_conf()


@pytest.fixture(scope="session")
def ctx():
    yield from make_default_ctx(__file__)


# 新增浏览器fixture
@pytest.fixture(scope="session")
def auth(cfg):
    auth = SimpleBrowserAuth(cfg.browser)
    auth.start_playwright()
    yield auth
    auth.close_playwright()


@pytest.fixture(scope="session")
def page_user_a(auth):
    page, context = auth.get_logged_in_page('baidu', 'user_a')
    yield page
    context.close()

@pytest.fixture(scope="session")
def page_user_b(auth):
    page, context = auth.get_logged_in_page('baidu', 'user_b')
    yield page
    context.close()
