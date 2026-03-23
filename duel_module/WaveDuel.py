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

        # 处理对话框，直到对话框消失
        while ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is not None:
            print("检测到对话框，处理对话框")
            if ClickUtils.get_img_location(CommonConstants.dialog_fast_forward_img) is not None:
                print("点击对话框快进图标")
                ClickUtils.click_by_img(CommonConstants.dialog_fast_forward_img)
            else:
                ClickUtils.click_by_img(CommonConstants.dialog_mark_img)
            time.sleep(1)

    # # 决斗结束后
    # def after_duel(self):
    #     self.runtime_context.duel_loc = None
    #
    #     if self.runtime_context.duel_success_flag is False:
    #         return
    #
    #     # 1. 点击奖励直到不存在奖励标志和出现奖励结束标志
    #     while ClickUtils.get_img_location(WaveDuelConstants.slot_start_img) is None:
    #         flag = False
    #         time.sleep(1)
    #
    #         # 点击决斗评价加速
    #         if ClickUtils.get_img_location(CommonConstants.duel_evaluation_img) is not None:
    #             ClickUtils.click_by_img(CommonConstants.duel_evaluation_img)
    #             time.sleep(1)
    #
    #         if ClickUtils.get_img_location(CommonConstants.next_step_img) is not None:
    #             ClickUtils.click_by_img(CommonConstants.next_step_img)
    #             flag = True
    #             print("点击下一步")
    #             CommonUtils.click_retry()
    #
    #         if DuelUtils.get_hao_loc() is not None:
    #             ClickUtils.click_by_location(DuelUtils.get_hao_loc())
    #             flag = True
    #             print("点击好")
    #             CommonUtils.click_retry()
    #
    #         # 循环点击对话框直到对话框消失
    #         while ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is not None:
    #             print("活动结束后点击对话框")
    #             if ClickUtils.get_img_location(CommonConstants.dialog_fast_forward_img) is not None:
    #                 print("点击对话框快进图标")
    #                 ClickUtils.click_by_img(CommonConstants.dialog_fast_forward_img)
    #             else:
    #                 ClickUtils.click_by_img(CommonConstants.dialog_mark_img)
    #             CommonUtils.click_retry()
    #             time.sleep(1)
    #
    #         # 点击取消、关闭、后退
    #         while ClickUtils.get_img_location(CommonConstants.cancel_img) is not None \
    #                 or ClickUtils.get_img_location(CommonConstants.close_button_img) is not None:
    #
    #             time.sleep(3)
    #             if ClickUtils.click_by_img(CommonConstants.cancel_img):
    #                 CommonUtils.click_retry()
    #                 continue
    #             time.sleep(1)
    #             if ClickUtils.click_by_img(CommonConstants.close_button_img):
    #                 CommonUtils.click_retry()
    #                 continue
    #             time.sleep(1)
    #
    #             flag = True
    #
    #         if flag is False and ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is None \
    #                 and ClickUtils.get_img_location(CommonConstants.guanqia_img) is None:
    #             # 什么都没点击到，并且没有出现对话框
    #             print("随便点击一个位置")
    #             ClickUtils.click_by_location(self.runtime_context.end_duel_loc)
    #             CommonUtils.click_retry()
    #         time.sleep(2)










