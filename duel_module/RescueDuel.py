import time

from config.Config import Config
from config.RuntimeContext import RuntimeContext
from constant import CommonConstants, SpecialEventConstants, RescueDuelConstants
from duel_module.BaseDuel import BaseDuel
from util import ClickUtils, CommonUtils, DuelUtils, EventUtils


class RescueDuel(BaseDuel):
    def __init__(self, config: Config, runtime_context: RuntimeContext):
        super().__init__(config, runtime_context)

    def RescueDuel(self):
        pass

    def prepare(self):

        while ClickUtils.get_img_location(SpecialEventConstants.special_event_logo_dir + self.runtime_context.special_event_file_name) is not None:
            ClickUtils.click_by_img(SpecialEventConstants.special_event_logo_dir + self.runtime_context.special_event_file_name)
            if ClickUtils.get_img_location(CommonConstants.close_button_img) is not None:
                ClickUtils.click_by_img(CommonConstants.close_button_img)
                time.sleep(1)
            CommonUtils.click_retry()

        time.sleep(3)

        while DuelUtils.get_hao_loc() is not None \
               or ClickUtils.get_img_location(CommonConstants.cancel_img) is not None:
            if ClickUtils.click_by_location(DuelUtils.get_hao_loc()):
                time.sleep(1.5)
            if ClickUtils.click_by_img(CommonConstants.cancel_img):
                time.sleep(1.5)

        while ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is None:
            ClickUtils.click_by_img(RescueDuelConstants.duel_img)
            time.sleep(1)

        self.runtime_context.special_event_file_name = None

    def work(self):

        clear_copy_flag = True

        while ClickUtils.get_img_location(RescueDuelConstants.event_img) is not None:
            ClickUtils.click_by_img(RescueDuelConstants.event_img)
            time.sleep(2)
            CommonUtils.click_retry()

        duel_exist_flag = False
        while ClickUtils.get_img_location(RescueDuelConstants.duel_img) is not None:
            ClickUtils.click_by_img(RescueDuelConstants.duel_img)
            time.sleep(1)
            CommonUtils.click_retry()
            duel_exist_flag = True

        if not duel_exist_flag:
            # 清理副本
            if clear_copy_flag:
                prepare_clear_copy(self)
            # 救援
            else:
                prepare_rescue_duel(self)

        self.before_duel()
        self.in_duel()
        self.after_duel()

def prepare_clear_copy(self):
    ClickUtils.click_by_img_if_exist(RescueDuelConstants.appear_immediately_img)
    ClickUtils.click_by_img(CommonConstants.close_button_img, 0, -90)
    ClickUtils.click_by_img_if_exist(RescueDuelConstants.appeared_img)
    time.sleep(2)

    while ClickUtils.get_img_location(RescueDuelConstants.duel_img) is None:
        print("等待决斗图标出现")
        time.sleep(2)
        CommonUtils.click_retry()
    ClickUtils.click_by_img(RescueDuelConstants.duel_img)

def prepare_rescue_duel(self):
    while ClickUtils.get_img_location(RescueDuelConstants.rescue_duel_img) is not None:
        ClickUtils.click_by_img(RescueDuelConstants.rescue_duel_img)
        time.sleep(1)
        CommonUtils.click_retry()