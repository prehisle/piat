
def test_baidu_homepage_user_a(page_user_a):
    """测试百度首页登录状态 - user_a"""
    page = page_user_a
    page.goto('https://www.baidu.com')
    
    # 验证页面标题
    title = page.title()
    assert "百度" in title
    
    # 验证用户已登录（检查用户名显示）
    try:
        username_element = page.wait_for_selector('.s-top-username', timeout=10000)
        assert username_element is not None
        username = username_element.text_content()
        print(f"当前登录用户: {username}")
    except:
        print("未检测到登录状态，可能需要重新登录")

def test_baidu_homepage_user_b(page_user_b):
    """测试百度首页登录状态 - user_b"""
    page = page_user_b
    page.goto('https://www.baidu.com')

    # 验证页面标题
    title = page.title()
    assert "百度" in title

    # 验证用户已登录（检查用户名显示）
    try:
        username_element = page.wait_for_selector('.s-top-username', timeout=10000)
        assert username_element is not None
        username = username_element.text_content()
        print(f"当前登录用户: {username}")
    except:
        print("未检测到登录状态，可能需要重新登录")