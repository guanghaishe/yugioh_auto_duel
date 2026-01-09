import time

from constant import TagDuelTournamentConstants, CommonConstants
from duel_module.BaseDuel import BaseDuel
from util import ClickUtils, CommonUtils, DuelUtils, EventUtils


class TagDuelTournamentDuel(BaseDuel):
    def __init__(self, config, runtime_context):
        super().__init__(config, runtime_context)

    def prepare(self):

        # 1. 点击组队决斗
        while ClickUtils.get_img_location(CommonConstants.dialog_fast_forward_img) is None:
            ClickUtils.click_by_img(TagDuelTournamentConstants.tag_duel_img)
            CommonUtils.click_retry()
            time.sleep(1)

        # 2. 点击对话框快进
        while ClickUtils.get_img_location(TagDuelTournamentConstants.hard_img) is None:
            ClickUtils.click_by_img(CommonConstants.dialog_fast_forward_img)
            CommonUtils.click_retry()
            time.sleep(1)

        # 3. 点击困难
        ClickUtils.click_by_img(TagDuelTournamentConstants.hard_img)
        time.sleep(1)

        # 4. 点击对话框快进直到出现自动决斗按钮
        duel_logo_loc = DuelUtils.get_duel_logo_loc()
        while duel_logo_loc is None:
            ClickUtils.click_by_img(CommonConstants.dialog_mark_img)
            CommonUtils.click_retry()
            time.sleep(1)

            duel_logo_loc = DuelUtils.get_duel_logo_loc()

        self.runtime_context.duel_loc = duel_logo_loc


    def after_duel(self):
        if self.runtime_context.duel_success_flag is False:
            return

        # 1. 点击奖励直到不存在奖励标志和出现奖励结束标志
        while DuelUtils.if_exist_reward() is True or DuelUtils.if_exist_end_reward() is False:
            flag = False
            time.sleep(1)

            # 点击决斗评价加速
            if ClickUtils.get_img_location(CommonConstants.duel_evaluation_img) is not None:
                ClickUtils.click_by_img(CommonConstants.duel_evaluation_img)
                time.sleep(1)

            if ClickUtils.get_img_location(CommonConstants.next_step_img) is not None:
                ClickUtils.click_by_img(CommonConstants.next_step_img)
                flag = True
                print("点击下一步")
                CommonUtils.click_retry()

            if DuelUtils.get_hao_loc() is not None:
                ClickUtils.click_by_location(DuelUtils.get_hao_loc())
                flag = True
                print("点击好")
                CommonUtils.click_retry()

            if flag is False and ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is None\
                    and ClickUtils.get_img_location(CommonConstants.guanqia_img) is None:
                # 什么都没点击到，并且没有出现对话框
                print("随便点击一个位置")
                ClickUtils.click_by_location(self.runtime_context.end_duel_loc)
                CommonUtils.click_retry()
            time.sleep(2)

        # 2. 循环点击对话框直到对话框消失
        while ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is not None:
            print("活动结束后点击对话框")
            if(ClickUtils.get_img_location(CommonConstants.dialog_fast_forward_img) is not None):
                print("点击对话框快进")
                ClickUtils.click_by_img(CommonConstants.dialog_fast_forward_img)
                CommonUtils.click_retry()
                time.sleep(1)
                continue

            ClickUtils.click_by_img(CommonConstants.dialog_mark_img)
            CommonUtils.click_retry()
            time.sleep(1)

        # 3. 决斗结束后点击取消、关闭、后退
        while ClickUtils.get_img_location(CommonConstants.cancel_img) is not None \
               or ClickUtils.get_img_location(CommonConstants.close_button_img) is not None \
                or DuelUtils.get_hao_loc() is not None:

            time.sleep(3)
            if self.config.if_special_event_duel is True and EventUtils.if_exist_activity():
                self.runtime_context.special_event_file_name = EventUtils.get_activity_file_name()
            if ClickUtils.click_by_img(CommonConstants.cancel_img):
                CommonUtils.click_retry()
                continue
            time.sleep(1)
            if ClickUtils.click_by_img(CommonConstants.close_button_img):
                CommonUtils.click_retry()
                continue
            time.sleep(1)
            if DuelUtils.get_hao_loc() is not None:
                ClickUtils.click_by_location(DuelUtils.get_hao_loc())
                print("点击好")
                CommonUtils.click_retry()

        print("决斗流程结束")
        self.runtime_context.duel_loc = None


    def finish(self):
        self.runtime_context.duel_success_flag = True
        time.sleep(2)
