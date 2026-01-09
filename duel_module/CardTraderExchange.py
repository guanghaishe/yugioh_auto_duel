import time

from constant import CardTraderConstants
from util import ClickUtils


class CardTraderExchange:
    def __init__(self, config, runtime_context):
        self.config = config
        self.runtime_context = runtime_context

    def exchange_cards(self, card_rarity="precious"):
        """
        卡片商人兑换卡片功能
        
        Args:
            card_rarity: 卡片稀有度，可选值：precious(珍贵), rare(稀有), super_rare(超凡), normal(普通)
        """
        print(f"开始执行卡片商人兑换卡片功能，稀有度：{card_rarity}")
        
        # 1. 点击卡片兑换商店
        if not self._wait_and_click(CardTraderConstants.card_exchange_shop_img, "卡片兑换商店"):
            return False
        
        # 2. 点击更多选项（倒三角形）
        if not self._wait_and_click(CardTraderConstants.more_options_triangle_img, "更多选项"):
            return False
        
        # 3. 点击筛选条件
        if not self._wait_and_click(CardTraderConstants.filter_conditions_img, "筛选条件"):
            return False
        
        # 4. 一直往下滑动，直到找到对应稀有度，点击筛选
        if not self._select_card_rarity(card_rarity):
            return False
        
        # 5. 点击筛选条件确认按钮
        if not self._wait_and_click(CardTraderConstants.filter_conditions_confirm_img, "筛选条件确认"):
            return False
        
        # 暂停2秒等待界面加载
        print("等待界面加载...")
        time.sleep(2)
        
        # 检查卡片数量，如果找不到数量为2的图片，说明所有卡片已满三，停止脚本
        if not self._check_card_quantity():
            print("所有卡片已满三，无需继续兑换，脚本停止")
            return False
        
        # 6. 点击收取卡片下面固定位置偏差的卡片
        if not self._click_collect_cards_with_offset():
            return False
        
        # 7. 点击添加（使用与收取卡片位置偏差值的方式）
        if not self._click_add_button_with_offset():
            return False
        
        # 8. 点击返回
        if not self._wait_and_click(CardTraderConstants.back_button_img, "返回按钮"):
            return False
        
        # 9. 点击确认
        if not self._wait_and_click(CardTraderConstants.confirm_button_img, "确认按钮"):
            return False
        
        # 10. 点击交易
        if not self._wait_and_click(CardTraderConstants.trade_button_img, "交易按钮"):
            return False
        
        # 11. 暂停5秒
        print("等待5秒...")
        time.sleep(5)
        
        print(f"卡片商人兑换卡片功能执行完成，稀有度：{card_rarity}")
        return True

    def _wait_and_click(self, img_path, step_name):
        """
        等待并点击图片，使用while循环直到找到为止
        
        Args:
            img_path: 图片路径
            step_name: 步骤名称，用于日志输出
            
        Returns:
            bool: 是否成功点击
        """
        print(f"正在查找并点击：{step_name}")
        while True:
            location = ClickUtils.get_img_location(img_path)
            if location is not None:
                success = ClickUtils.click_by_img(img_path)
                if success:
                    print(f"成功点击：{step_name}")
                    time.sleep(1.5)  # 每个步骤之间暂停1.5秒
                    return True
            time.sleep(1)  # 如果没找到，等待1秒后重试

    def _select_card_rarity(self, card_rarity):
        """
        选择卡片稀有度
        
        Args:
            card_rarity: 卡片稀有度
            
        Returns:
            bool: 是否成功选择
        """
        print(f"正在选择卡片稀有度：{card_rarity}")
        
        # 根据稀有度选择对应的图片
        rarity_img_map = {
            "precious": CardTraderConstants.precious_filter_img,
            "rare": CardTraderConstants.rare_filter_img,
            "super_rare": CardTraderConstants.super_rare_filter_img,
            "normal": CardTraderConstants.normal_filter_img
        }
        
        target_img = rarity_img_map.get(card_rarity)
        if target_img is None:
            print(f"不支持的卡片稀有度：{card_rarity}")
            return False
        
        # 一直往下滑动，直到找到对应稀有度
        max_scroll_attempts = 20  # 最大滑动次数
        scroll_attempts = 0
        
        while scroll_attempts < max_scroll_attempts:
            location = ClickUtils.get_img_location(target_img)
            if location is not None:
                # 找到目标稀有度，点击它
                success = ClickUtils.click_by_img(target_img)
                if success:
                    print(f"成功选择稀有度：{card_rarity}")
                    time.sleep(1.5)
                    return True
            
            # 向下滑动
            self._scroll_down()
            scroll_attempts += 1
            time.sleep(1)
        
        print(f"未找到稀有度：{card_rarity}")
        return False

    def _scroll_down(self):
        """
        向下滑动屏幕
        """
        import pyautogui
        # 获取屏幕中心位置
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width // 2 - 20
        center_y = screen_height // 2
        
        # 从屏幕中心向下滑动
        pyautogui.moveTo(center_x, center_y)
        pyautogui.drag(0, -300, duration=0.5)

    def _click_collect_cards_with_offset(self):
        """
        点击收取卡片按钮，并应用预设的偏移量
        
        Returns:
            bool: 是否成功点击
        """
        # 预设的偏移量，您可以根据实际情况修改这些值
        x_offset = 0  # x轴偏移量（像素）
        y_offset = 900  # y轴偏移量（像素）
        
        print(f"正在点击收取卡片按钮，偏移量：({x_offset}, {y_offset})")
        
        while True:
            location = ClickUtils.get_img_location(CardTraderConstants.collect_cards_img)
            if location is not None:
                # 应用偏移量
                target_x = location.x + x_offset
                target_y = location.y + y_offset
                
                success = ClickUtils.click_by_pos(target_x, target_y)
                if success:
                    print(f"成功点击收取卡片按钮，位置：({target_x}, {target_y})")
                    time.sleep(1.5)
                    return True
            time.sleep(1)

    def _check_card_quantity(self):
        """
        检查卡片数量，如果找不到数量为0、1、2的图片，说明所有卡片已满三
        
        Returns:
            bool: 如果找到数量为0、1、2的卡片返回True，否则返回False
        """
        print("正在检查卡片数量...")
        
        # 尝试查找数量为0、1、2的图片
        quantity_0_location = ClickUtils.get_img_location(CardTraderConstants.card_quantity_0_img)
        quantity_1_location = ClickUtils.get_img_location(CardTraderConstants.card_quantity_1_img)
        quantity_2_location = ClickUtils.get_img_location(CardTraderConstants.card_quantity_2_img)
        
        if quantity_0_location is not None:
            print("找到数量为0的卡片，可以继续兑换")
            return True
        elif quantity_1_location is not None:
            print("找到数量为1的卡片，可以继续兑换")
            return True
        elif quantity_2_location is not None:
            print("找到数量为2的卡片，可以继续兑换")
            return True
        else:
            print("未找到数量为0、1、2的卡片，所有卡片已满三")
            return False

    def _click_add_button_with_offset(self):
        """
        点击添加按钮，使用与收取卡片位置偏差值的方式
        
        Returns:
            bool: 是否成功点击
        """
        # 预设的添加按钮偏移量，相对于收取卡片按钮的位置
        add_button_x_offset = 0  # 添加按钮的x轴偏移量（像素）
        add_button_y_offset = 380  # 添加按钮的y轴偏移量（像素）
        
        print(f"正在点击添加按钮，偏移量：({add_button_x_offset}, {add_button_y_offset})")
        
        while True:
            # 先找到收取卡片按钮的位置
            collect_location = ClickUtils.get_img_location(CardTraderConstants.collect_cards_img)
            if collect_location is not None:
                # 计算添加按钮的位置（基于收取卡片按钮的位置）
                add_button_x = collect_location.x + add_button_x_offset
                add_button_y = collect_location.y + add_button_y_offset
                
                success = ClickUtils.click_by_pos(add_button_x, add_button_y)
                if success:
                    print(f"成功点击添加按钮，位置：({add_button_x}, {add_button_y})")
                    time.sleep(1.5)
                    return True
            time.sleep(1)

    def run(self, card_rarity="precious"):
        """
        执行卡片商人兑换卡片功能（循环10次）
        
        Args:
            card_rarity: 卡片稀有度
        """
        print(f"开始执行卡片商人兑换卡片功能，循环10次，稀有度：{card_rarity}")
        
        for i in range(10):
            print(f"第 {i+1} 次执行卡片商人兑换卡片")
            success = self.exchange_cards(card_rarity)
            if not success:
                print(f"第 {i+1} 次执行失败")
                break
            print(f"第 {i+1} 次执行完成")
        
        print("卡片商人兑换卡片功能全部执行完成")
