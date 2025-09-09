def test_1(page):
    """测试百度首页登录状态 - user_a"""
    page.goto('https://wangxiao.xisaiwang.com/tiku2/list-zt131-1.html?1=1')
    pass

def test_2(page):
    page.get_by_role("link", name="系统架构设计师", exact=True).click()
    page.get_by_role("link", name="历年真题").click()

def test_3(page):
    page.get_by_role("link", name="2022", exact=True).click()
    # page.get_by_role("link", name="2023").click()
    # page.get_by_role("link", name="2024").click()
    # page.get_by_role("link", name="2025").click()


# def test_4(page):
#     page.get_by_role("link", name="2022").click()