import os
import time

from config import RuntimeContext
from constant import DuelConstants, CommonConstants
from constant.YuGiOhSeries import YuGiOhSeries
from duel_module.BaseDuel import BaseDuel
from service.EventDispatcherService import EventDispatcherService
from util import ClickUtils, CommonUtils, DuelUtils, EventUtils


class PasserDuel(BaseDuel):

    def __init__(self, config, runtime_context: RuntimeContext):
        super().__init__(config, runtime_context)
        self.passer_list = self.init_passer_list()
        self.eventDispatcherService = EventDispatcherService(config, runtime_context)


    def run(self):
        for world_cnt in range(8):
            print("开始世界为 " + YuGiOhSeries.get_name_by_number(self.runtime_context.world_idx) + " 的路人清理")
            # 一个世界循环4次
            for i in range(4):
                if EventUtils.if_exist_activity():
                    if self.config.if_special_event_duel is False:
                        print("发现活动事件, 跳过")
                    self.eventDispatcherService.dispatchEvent()

                time.sleep(1)
                self.clear_passer()
                ClickUtils.click_by_img(CommonConstants.turn_right_button_img)
                CommonUtils.click_retry()
                time.sleep(3)

            print("世界为 " + YuGiOhSeries.get_name_by_number(self.runtime_context.world_idx) + " 的路人清理完成")

            self.runtime_context.world_idx = self.runtime_context.world_idx % 8 + 1
            if not DuelUtils.change_world(self.runtime_context.world_idx):
                print("切换世界失败, 任务异常")
                return
        print("所有世界路人清理完成")

    def clear_passer(self):
        '''
        清理路人
        :return:
        '''
        found_passer_flag = True

        while found_passer_flag:
            found_passer_flag = False
            for file in self.passer_list:
                loc = ClickUtils.get_img_location(DuelConstants.passer_logo_dir + file)
                if loc is None:
                    continue

                found_passer_flag = True

                # 发现特殊事件
                if file.startswith("event"):
                    ClickUtils.click_by_pos(loc.x, loc.y + 20)
                else:
                    ClickUtils.click_by_location(loc)

                time.sleep(2)
                CommonUtils.click_retry()

                # 发现路人
                print("发现了编号为" + file + "的路人")
                self.duel()

    def init_passer_list(self) -> list:
        '''
        初始化路人列表
        :return:
        '''
        passer_list = []
        for filename in os.listdir(DuelConstants.passer_logo_dir):
            passer_list.append(filename)
        print("路人列表初始化完成")
        return passer_list
