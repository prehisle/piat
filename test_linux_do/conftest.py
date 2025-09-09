import pytest
from olymat.utils.ctx_helper import make_default_ctx

from comm.pw.browser_helper import auth_page
from .config import get_g_conf


@pytest.fixture(scope="session")
def cfg():
    return get_g_conf()


@pytest.fixture(scope="session")
def ctx():
    yield from make_default_ctx(__file__)


@pytest.fixture(scope="session")
def page(auth_page, cfg):
    page, context = auth_page.get_logged_in_page('linux_do', cfg.user.name)
    yield page
    context.close()
