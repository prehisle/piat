import pytest

from olymat.utils.ctx_helper import make_default_ctx
from olymat.utils.ssh_helper import init_ssh_fixtures

from .config import get_g_conf

init_ssh_fixtures(globals(), get_g_conf().env.servers, groups=[
    ["all", ["main", "pkgs"]],
])

@pytest.fixture(scope="session")
def cfg():
    return get_g_conf()


@pytest.fixture(scope="session")
def ctx():
    yield from make_default_ctx(__file__)
