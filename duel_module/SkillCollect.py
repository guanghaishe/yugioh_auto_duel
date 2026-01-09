import time

import pyautogui

from constant import SkillCollectConstants
from util import ClickUtils


class SkillCollect:
    def __init__(self, config, runtime_context):
        self.config = config
        self.runtime_context = runtime_context

    def collect_skill(self):
        """
        执行一次技能领取流程
        
        Returns:
            bool: 是否成功领取技能，如果找不到技能图标则返回False
        """
        print("开始执行技能领取流程")
        
        # 1. 点击技能图标（如果找不到则返回False，结束循环）
        skill_icon_location = ClickUtils.get_img_location(SkillCollectConstants.skill_icon_img)
        if skill_icon_location is None:
            print("未找到技能图标，技能领取完成")
            return False
        
        ClickUtils.click_by_img(SkillCollectConstants.skill_icon_img)
        print("成功点击技能图标")
        time.sleep(1.5)
        
        # 2. 点击可交易图片（如果没找到就向下滑动直到出现）
        if not self._find_and_click_tradeable():
            print("未找到可交易图片")
            return False
        print("成功点击可交易图片")
        time.sleep(1.5)
        
        # 3. 点击交易
        if not self._wait_and_click(SkillCollectConstants.trade_button_img, "交易按钮"):
            return False
        print("成功点击交易按钮")
        time.sleep(3)  # 点击交易后暂停3秒
        
        # 4. 点击确定
        if not self._wait_and_click(SkillCollectConstants.confirm_button_img, "确定按钮"):
            return False
        print("成功点击确定按钮")
        time.sleep(1.5)
        
        print("技能领取流程执行完成")
        return True

    def _find_and_click_tradeable(self):
        """
        查找并点击可交易图片，如果没找到就向下滑动直到出现
        
        Returns:
            bool: 是否成功点击
        """
        print("正在查找可交易图片...")
        max_scroll_attempts = 20  # 最大滑动次数
        scroll_attempts = 0
        
        while scroll_attempts < max_scroll_attempts:
            location = ClickUtils.get_img_location(SkillCollectConstants.tradeable_img)
            if location is not None:
                # 找到可交易图片，点击它
                success = ClickUtils.click_by_img(SkillCollectConstants.tradeable_img)
                if success:
                    return True
            
            # 向下滑动
            self._scroll_down()
            scroll_attempts += 1
            print(f"向下滑动第 {scroll_attempts} 次")
            time.sleep(1)
        
        print("达到最大滑动次数，未找到可交易图片")
        return False

    def _scroll_down(self):
        """
        从屏幕中心向下滑动
        """
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width // 2
        center_y = screen_height // 2
        
        # 从屏幕中心向下滑动
        pyautogui.moveTo(center_x, center_y)
        pyautogui.drag(0, -300, duration=0.5)

    def _wait_and_click(self, img_path, step_name, max_wait_time=30):
        """
        等待并点击图片
        
        Args:
            img_path: 图片路径
            step_name: 步骤名称，用于日志输出
            max_wait_time: 最大等待时间（秒）
            
        Returns:
            bool: 是否成功点击
        """
        print(f"正在查找并点击：{step_name}")
        wait_time = 0
        
        while wait_time < max_wait_time:
            location = ClickUtils.get_img_location(img_path)
            if location is not None:
                success = ClickUtils.click_by_img(img_path)
                if success:
                    return True
            time.sleep(1)
            wait_time += 1
        
        print(f"等待超时，未找到：{step_name}")
        return False

    def run(self):
        """
        无限循环执行技能领取功能，直到没有技能图标为止
        """
        print("=" * 50)
        print("开始执行自动领取技能功能")
        print("=" * 50)
        
        count = 0
        while True:
            count += 1
            print(f"\n--- 第 {count} 次技能领取 ---")
            
            success = self.collect_skill()
            if not success:
                print(f"\n技能领取结束，共领取 {count - 1} 个技能")
                break
            
            print(f"第 {count} 次技能领取完成")
        
        print("=" * 50)
        print("自动领取技能功能执行完毕")
        print("=" * 50)


