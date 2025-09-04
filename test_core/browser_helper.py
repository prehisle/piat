import json
import os
import sys
from pathlib import Path
from playwright.async_api import async_playwright


class SimpleBrowserAuth:
    def __init__(self, config):
        self.config = config.browser
        self.auth_dir = Path("./auth")
        self.auth_dir.mkdir(exist_ok=True)
        self.playwright = None
        self.browser = None
    
    def get_auth_file(self, site, user):
        return self.auth_dir / f"{site}_{user}.json"
    
    async def start_playwright(self):
        if not self.playwright:
            self.playwright = await async_playwright().start()
            # VSCode 测试环境或非交互式环境使用无头模式
            # headless = not self._is_interactive_env()
            headless = False
            self.browser = await self.playwright.chromium.launch(headless=headless)
    
    async def close_playwright(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
    
    async def _create_and_verify_login(self, site_config, auth_file=None):
        """创建浏览器上下文并验证登录状态
        
        Args:
            site_config: 网站配置信息
            auth_file: 认证文件路径，如果存在则尝试恢复状态
            
        Returns:
            tuple: (page, context, success) - 页面对象、上下文对象、是否成功
        """
        # 如果有状态文件，尝试恢复状态
        if auth_file and auth_file.exists():
            context = await self.browser.new_context(storage_state=str(auth_file))
        else:
            context = await self.browser.new_context()
        
        page = await context.new_page()
        await page.goto(site_config['login_url'])
        
        try:
            await page.wait_for_selector(site_config['success_selector'], timeout=300000)
            return page, context, True  # 登录成功
        except:
            await page.close()
            await context.close()
            return None, None, False  # 登录失败
    
    async def get_logged_in_page(self, site, user):
        await self.start_playwright()
        
        site_config = self.config.sites[site]
        auth_file = self.get_auth_file(site, user)

        print(f"\n正在检测登录状态 {site}-{user}，判断登录成功后会自动继续（5分钟超时）...")
        page, context, success = await self._create_and_verify_login(site_config, auth_file)
        if success:
            # 保存登录状态
            await context.storage_state(path=str(auth_file))
            return page, context
        else:
            raise Exception(f"登录 {site} 失败或超时")

        
