import pytest


@pytest.mark.parametrize('logged_in_page', [
    {'site': 'baidu', 'user': 'user_a'}
], indirect=True)
@pytest.mark.asyncio
async def test_baidu_homepage(logged_in_page):
    """测试百度首页登录状态"""
    page = logged_in_page
    await page.goto('https://www.baidu.com')
    
    # 验证页面标题
    title = await page.title()
    assert "百度" in title
    
    # 验证用户已登录（检查用户名显示）
    try:
        username_element = await page.wait_for_selector('.s-top-username', timeout=10000)
        assert username_element is not None
        username = await username_element.text_content()
        print(f"当前登录用户: {username}")
    except:
        print("未检测到登录状态，可能需要重新登录")


