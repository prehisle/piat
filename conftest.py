import pytest

from olymat.plugin import get_conf
from olymat.utils.dict_helper import DotDict
from olymat.utils.pytest_helper import update_olymat_conf, init_olymat_conf


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    if not update_olymat_conf(config, DotDict(get_conf())):
        return  # 进入保护模式
    init_olymat_conf(config)


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    if session.config.safeMode or session.config.olymat_conf.__debug:
        return
