import time

from duel_module.BaseDuel import BaseDuel
from util import ClickUtils, DuelUtils, CommonUtils
from constant import WaveDuelConstants, CommonConstants

'''
车轮战决斗混战
'''
class WaveDuel(BaseDuel):
    def __init__(self, config, runtime_context):
        super().__init__(config, runtime_context)


    def prepare(self):
        # 1. 点击车轮战Event
        ClickUtils.click_by_img_if_exist(WaveDuelConstants.wave_duel_event_img)
        time.sleep(2)

        # 2. 点击"槽位开始"
        slot_start_loc = ClickUtils.get_img_location(WaveDuelConstants.slot_start_img)
        duel_logo_loc = DuelUtils.get_duel_logo_loc()
        while slot_start_loc is None and duel_logo_loc is None:
            slot_start_loc = ClickUtils.get_img_location(WaveDuelConstants.slot_start_img)
            time.sleep(1.5)

        if slot_start_loc is not None:
            ClickUtils.click_by_location(slot_start_loc)
            time.sleep(3)

        # 3. 获取自动决斗位置
        while duel_logo_loc is None:
            duel_logo_loc = DuelUtils.get_duel_logo_loc()
            time.sleep(1.5)
        self.runtime_context.duel_loc = duel_logo_loc


    def before_duel(self):
        if self.runtime_context.duel_loc is None:
            self.runtime_context.duel_success_flag = False
            return

        # 获取所有可能的决斗按钮位置并依次点击
        duel_logo_locs = DuelUtils.get_all_duel_logo_locs()
        entered = False
        for loc in duel_logo_locs:
            print(f"尝试点击决斗标签位置: {loc}")
            ClickUtils.click_by_location(loc)
            time.sleep(2)
            CommonUtils.click_retry()
            # 点击后检查决斗标签是否消失
            if DuelUtils.get_duel_logo_loc() is None:
                self.runtime_context.duel_loc = loc
                entered = True
                print("成功进入决斗")
                break

        if not entered:
            print("未能进入决斗")
            self.runtime_context.duel_success_flag = False
            return

        self.runtime_context.duel_success_flag = True

        while ClickUtils.get_img_location(WaveDuelConstants.change_role_img) is not None:
            ClickUtils.click_by_img(CommonConstants.confirm_img)
            time.sleep(1)
            CommonUtils.click_retry()





