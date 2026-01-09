import time

from constant import DuelistKingdomConstants, CommonConstants
from duel_module.BaseDuel import BaseDuel
from util import ClickUtils, CommonUtils, DuelUtils


class DuelistKingdomDuel(BaseDuel):
    def __init__(self, config, runtime_context):
        super().__init__(config, runtime_context)

    def prepare(self):

        # 1. 点击决斗者王国
        while ClickUtils.get_img_location(DuelistKingdomConstants.pegasus_city_img) is None:
            ClickUtils.click_by_img(DuelistKingdomConstants.duelist_kingdom_img)
            CommonUtils.click_retry()
            time.sleep(1)

        # 2. 点击帕伽索斯城
        while ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is None:
            ClickUtils.click_by_img(DuelistKingdomConstants.pegasus_city_img)
            CommonUtils.click_retry()
            time.sleep(1)

        # 3. 点击对话框
        duel_logo_loc = None
        while duel_logo_loc is None:
            ClickUtils.click_by_img(CommonConstants.dialog_mark_img)
            CommonUtils.click_retry()
            time.sleep(1)
            if ClickUtils.get_img_location(DuelistKingdomConstants.very_hard_img) is not None:
                ClickUtils.click_by_img(DuelistKingdomConstants.very_hard_img)
                time.sleep(1)

            duel_logo_loc = DuelUtils.get_duel_logo_loc()

        self.runtime_context.duel_loc = duel_logo_loc


    def finish(self):
        self.runtime_context.duel_success_flag = True
        time.sleep(2)
