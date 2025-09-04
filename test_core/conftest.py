import pytest
import pytest_asyncio

from olymat.utils.ctx_helper import make_default_ctx
from olymat.utils.ssh_helper import init_ssh_fixtures

from .config import get_g_conf
from .browser_helper import SimpleBrowserAuth

init_ssh_fixtures(globals(), get_g_conf().env.servers, groups=[
    ["all", ["main", "pkgs"]],
])

@pytest.fixture(scope="session")
def cfg():
    return get_g_conf()


@pytest.fixture(scope="session")
def ctx():
    yield from make_default_ctx(__file__)


# 新增浏览器fixture
@pytest_asyncio.fixture
async def logged_in_page(request, cfg):
    site = request.param['site']
    user = request.param['user']
    
    auth = SimpleBrowserAuth(cfg)
    page, context = await auth.get_logged_in_page(site, user)
    
    yield page
    
    # 清理资源
    await context.close()
    await auth.close_playwright()
