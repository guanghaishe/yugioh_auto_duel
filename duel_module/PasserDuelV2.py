import os
import time

from config import RuntimeContext
from constant import DuelConstants, CommonConstants
from constant.YuGiOhSeries import YuGiOhSeries
from duel_module.BaseDuel import BaseDuel
from service.EventDispatcherService import EventDispatcherService
from util import ClickUtils, CommonUtils, DuelUtils, EventUtils


class PasserDuelV2(BaseDuel):

    def __init__(self, config, runtime_context: RuntimeContext):
        super().__init__(config, runtime_context)
        self.passer_list = self.init_passer_list()
        self.exclamation_mark_list = self.init_exclamation_mark_list()
        self.eventDispatcherService = EventDispatcherService(config, runtime_context)


    def run(self):

        if self.config.if_special_event_duel is True and EventUtils.if_exist_activity():
            self.runtime_context.special_event_file_name = EventUtils.get_activity_file_name()

        # 1. 清理路人 + 小红帽
        print("查找当前世界是否存在路人")

        while True:
            if self.config.if_special_event_duel is True and self.runtime_context.special_event_file_name is not None:
                self.eventDispatcherService.dispatchEvent()
                DuelUtils.change_world(self.config.special_event_duel_return_world_idx)

            passer_loc = self.get_passer_loc()
            if passer_loc is None:
                print("当前世界路人已经清理完毕")
                break

            print("开始清理路人")
            ClickUtils.click_by_location(passer_loc)
            CommonUtils.click_retry()
            self.duel()

        # 2. 清理其他世界的路人
        while True:
            if self.config.if_special_event_duel is True and self.runtime_context.special_event_file_name is not None:
                self.eventDispatcherService.dispatchEvent()
                DuelUtils.change_world(self.config.special_event_duel_return_world_idx)

            world_change_loc = DuelUtils.get_world_change_loc()
            if world_change_loc is None:
                print("未能找到世界切换图标")
                break

            ClickUtils.click_by_location(world_change_loc)
            time.sleep(1)
            passer_loc = self.get_passer_loc()
            if passer_loc is None:
                ClickUtils.click_by_location(world_change_loc)
                break

            print("开始清理路人")
            while ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is None:
                ClickUtils.click_by_location(passer_loc)
                CommonUtils.click_retry()
            self.duel()
        DuelUtils.change_world(self.runtime_context.world_idx)
        print("所有世界路人清理完毕")

        print("准备捡钥匙任务")
        # 1. 点击 WORLD 图标，因图标是动态，故采用坐标法
        ClickUtils.click_by_img(CommonConstants.guanqia_img, 130, 20)
        time.sleep(1)

        # 2. 搜索钥匙
        key_cnt = 0
        for i in range(5):
            exclamation_mark_loc = self.get_exclamation_mark_loc()
            while exclamation_mark_loc is not None:
                key_cnt = key_cnt + 1
                ClickUtils.click_by_location(exclamation_mark_loc)
                # 等待 【好】 图标
                hao_loc = DuelUtils.get_hao_loc()
                while hao_loc is None:
                    hao_loc = DuelUtils.get_hao_loc()
                    CommonUtils.click_retry()
                ClickUtils.click_by_location(hao_loc)
                time.sleep(1)
                # 搜索下一个感叹号
                exclamation_mark_loc = self.get_exclamation_mark_loc()
            ClickUtils.click_by_img(CommonConstants.turn_right_button_img)
            time.sleep(2)

        # 3. 点击 HOME 图标，因图标是动态，故采用坐标法
        ClickUtils.click_by_img(CommonConstants.guanqia_img, 130, 20)
        print("一共拾取了 " + str(key_cnt) + " 把钥匙")
        print("捡钥匙任务完成")



    def get_passer_loc(self, exclude_list=None):
        passer_loc = None
        for file in self.passer_list:
            passer_loc = ClickUtils.get_img_location(DuelConstants.passer_logo_dir_v2 + file)
            if passer_loc is not None:
                break
        return passer_loc

    def get_exclamation_mark_loc(self, exclude_list=None):
        exclamation_mark_loc = None
        for file in self.exclamation_mark_list:
            exclamation_mark_loc = ClickUtils.get_img_location(DuelConstants.exclamation_mark_dir + file)
            if exclamation_mark_loc is not None:
                break
        return exclamation_mark_loc


    def init_passer_list(self) -> list:
        '''
        初始化路人列表
        :return:
        '''
        passer_list = []
        for filename in os.listdir(DuelConstants.passer_logo_dir_v2):
            passer_list.append(filename)
        print("路人列表初始化完成")
        return passer_list

    def init_exclamation_mark_list(self):
        '''
        初始化感叹号列表
        :return:
        '''
        passer_list = []
        for filename in os.listdir(DuelConstants.exclamation_mark_dir):
            passer_list.append(filename)
        print("感叹号列表初始化完成")
        return passer_list
        pass