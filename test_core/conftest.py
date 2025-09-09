import pytest

from olymat.utils.ctx_helper import make_default_ctx

from .config import get_g_conf


@pytest.fixture(scope="session")
def cfg():
    return get_g_conf()


@pytest.fixture(scope="session")
def ctx():
    yield from make_default_ctx(__file__)






