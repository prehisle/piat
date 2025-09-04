from olymat.plugin import get_conf
from olymat.utils.dict_helper import DotDict
from olymat.utils.utils import func_run_once


class Config(DotDict):
    pass

@func_run_once
def get_g_conf() -> Config:
    return Config(get_conf())


get_g_conf()  # 尽早初始化工具集配置, 避免拿不到默认配置default.yaml
