import logging
import time


def scroll_page_incrementally(page, scroll_increment=200, pause_time=2):
    """
    逐步向下滚动页面，直到到达底部并且没有新内容加载。

    :param page: Playwright 的 Page 对象。
    :param scroll_increment: 每次滚动的像素值。
    :param pause_time: 每次滚动后暂停的秒数。
    """

    while True:
        # 记录滚动前的页面高度
        previous_height = page.evaluate("document.body.scrollHeight")

        # 向下滚动指定的像素值
        page.evaluate(f"window.scrollBy(0, {scroll_increment})")
        logging.info(f"已滚动 {scroll_increment} 像素。")
        # 等待新内容加载
        time.sleep(pause_time)

        # 获取滚动后的新页面高度
        new_height = page.evaluate("document.body.scrollHeight")

        # 检查页面是否还在加载新内容
        # 如果滚动后页面高度没有变化，说明可能到达底部
        if new_height == previous_height:
            # 进一步检查：当前滚动位置+视口高度 是否等于或超过 页面总高度
            # 这可以确认我们确实在页面的最底部
            scroll_position = page.evaluate("window.pageYOffset + window.innerHeight")
            if scroll_position + 10 >= new_height:
                logging.info("已滚动到页面底部，且无新内容加载。")
                break



def test_go(page):
    page.goto("https://linux.do/unread")
    time.sleep(2)

    # 首先，创建定位器
    links_locator = page.locator(".topic-list-body .topic-list-item .main-link .link-top-line a")

    # 然后，使用列表推导式遍历所有匹配的元素并获取href属性
    all_hrefs = [link.get_attribute("href") for link in links_locator.all()]
    all_hrefs = set(all_hrefs)
    for url in all_hrefs:
        if not url:
            continue
        logging.info(url)
        page.goto("https://linux.do" + url, timeout=30000)
        time.sleep(1)
        scroll_page_incrementally(page, scroll_increment=500, pause_time=1.5)
