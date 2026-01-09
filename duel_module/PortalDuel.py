import time

from constant import PortalConstants, CommonConstants
from duel_module.BaseDuel import BaseDuel
from service.EventDispatcherService import EventDispatcherService
from util import EventUtils, ClickUtils, CommonUtils, DuelUtils


class PortalDuel(BaseDuel):
    def __init__(self, config, runtime_context):
        super().__init__(config, runtime_context)
        self.eventDispatcherService = EventDispatcherService(config, runtime_context)

    def prepare(self):
        if EventUtils.if_exist_activity() and self.config.if_special_event_duel is True:
            self.runtime_context.special_event_file_name = EventUtils.get_activity_file_name()

        if self.runtime_context.special_event_file_name is not None:
            self.eventDispatcherService.dispatchEvent()
            DuelUtils.change_world(self.config.portal_duel_return_world_idx)

        # 1. 点击传送门，直到出现决斗按钮
        duel_logo_loc = None
        while duel_logo_loc is None:
            ClickUtils.click_by_img(PortalConstants.portal_img)
            CommonUtils.click_retry()
            time.sleep(1)
            duel_logo_loc = DuelUtils.get_duel_logo_loc()
            time.sleep(1)

        # 2. 点击决斗直到出现对话框
        while ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is None:
            ClickUtils.click_by_location(duel_logo_loc)
            CommonUtils.click_retry()
            time.sleep(1)



