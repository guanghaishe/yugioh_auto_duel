import os
import time

from config.Config import Config
from config.RuntimeContext import RuntimeContext
from constant import CommonConstants, SpecialEventConstants
from duel_module.BaseDuel import BaseDuel
from util import ClickUtils, CommonUtils, DuelUtils, EventUtils

class SpecialEventDuel(BaseDuel):
    def __init__(self, config: Config, runtime_context: RuntimeContext):
        super().__init__(config, runtime_context)

    def special_event_duel(self):
        # 点击 "前往人物出现的地方" 或 "出现"
        ClickUtils.click_by_img(SpecialEventConstants.special_event_logo_dir + self.runtime_context.special_event_file_name)
        time.sleep(3)

        while EventUtils.if_exist_activity():
            self.duel()
            time.sleep(2)


    def before_duel(self):
        # 如果还有出现图标，继续点击
        if ClickUtils.get_img_location(SpecialEventConstants.appear_img) is not None:
            ClickUtils.click_by_img(SpecialEventConstants.appear_img)
            print("点击出现")
            CommonUtils.click_retry()

        for file in EventUtils.get_event_logo_list():
            if ClickUtils.get_img_location(SpecialEventConstants.event_logo_dir + file) is None:
                continue

            # 获取位置并点击
            event_logo_loc = None
            while event_logo_loc is None:
                event_logo_loc = ClickUtils.get_img_location(SpecialEventConstants.event_logo_dir + file)
                time.sleep(1)

            print("获取到event位置，点击event")
            ClickUtils.click_by_pos(event_logo_loc.x, event_logo_loc.y + 20)
            CommonUtils.click_retry()

            # 点击对话框直到出现决斗按钮
            duel_logo_loc = None
            while duel_logo_loc is None:
                # 点击对话框
                time.sleep(1)
                print("点击对话框直到出现等级标签")
                ClickUtils.click_by_img(CommonConstants.dialog_mark_img)
                CommonUtils.click_retry()
                time.sleep(1)

                # 点击取消按钮
                if ClickUtils.get_img_location(CommonConstants.cancel_img) is not None:
                    print("点击取消按钮")
                    ClickUtils.click_by_img(CommonConstants.cancel_img)
                    time.sleep(1)

                # 选择伙伴按钮
                partner_loc = ClickUtils.get_img_location(SpecialEventConstants.partner_img)
                if partner_loc is not None:
                    print("选择伙伴")
                    ClickUtils.click_by_img(partner_loc)
                    CommonUtils.click_retry()

                # Rush Duel：选择角色和卡组按钮
                selectRoleAndDeckLoc = ClickUtils.get_img_location(SpecialEventConstants.select_role_and_deck_img)
                if selectRoleAndDeckLoc is not None:
                    print("选择角色和卡组")
                    ClickUtils.click_by_pos(selectRoleAndDeckLoc.x, selectRoleAndDeckLoc.y + 130)

                event_level_loc = DuelUtils.get_event_level_loc()
                duel_logo_loc = DuelUtils.get_duel_logo_loc()

                if event_level_loc is not None:
                    print("选择决斗等级")
                    ClickUtils.click_by_location(event_level_loc)
                    time.sleep(1)

            # 点击决斗
            if duel_logo_loc is not None:
                print("点击决斗")
                ClickUtils.click_by_location(duel_logo_loc)
                time.sleep(1)






