import time

from constant import RewardConstants
from util import ClickUtils, DuelUtils


class RewardExtract:
    def __init__(self, config, runtime_context):
        self.config = config
        self.runtime_context = runtime_context

    def extractLotteryReward(self):
        """
        彩票奖励抽取
        1. 点击彩票奖励列表往下固定偏移量位置
        2. 当没有出现好的情况下,循环点击该位置
        3. 出现好之后,点击好
        """
        # 1. 获取彩票奖励列表位置
        lottery_list_loc = ClickUtils.get_img_location(RewardConstants.lottery_reward_list_img)
        if lottery_list_loc is None:
            print("未找到彩票奖励列表按钮")
            return
        
        # 2. 计算点击位置(向下偏移)
        click_x = lottery_list_loc.x
        click_y = lottery_list_loc.y + RewardConstants.LOTTERY_CLICK_OFFSET_Y
        
        # 3. 循环点击直到出现"好"按钮
        while DuelUtils.get_hao_loc() is None:
            ClickUtils.click_by_pos(click_x, click_y)
            time.sleep(0.5)
        
        # 4. 点击"好"按钮
        ClickUtils.click_by_location(DuelUtils.get_hao_loc())
        print("彩票奖励抽取完成")
