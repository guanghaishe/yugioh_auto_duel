import os
import time

from pyautogui import Point

from constant import DuelConstants, CommonConstants, SpecialEventConstants
from util import ClickUtils, CommonUtils

duel_logo_list = []
reward_logo_list = []
end_reward_logo_list = []
activity_logo_list = []
hao_logo_list = []


def get_duel_logo_loc():
    """
    获取决斗图标的位置, 如果没有则返回None
    :return: 决斗图标的位置
    """
    global duel_logo_list
    if not duel_logo_list or len(duel_logo_list) == 0:
        for filename in os.listdir(DuelConstants.duel_logo_dir):
            duel_logo_list.append(filename)
        duel_logo_list.sort()

    for filename in duel_logo_list:
        if ClickUtils.get_img_location(DuelConstants.duel_logo_dir + filename):
            return ClickUtils.get_img_location(DuelConstants.duel_logo_dir + filename)
    return None

def get_event_level_loc():
    if ClickUtils.get_img_location(SpecialEventConstants.level_60_img, 0.9) is not None:
        return ClickUtils.get_img_location(SpecialEventConstants.level_60_img, 0.9)

    if ClickUtils.get_img_location(SpecialEventConstants.level_40_img) is not None:
        return ClickUtils.get_img_location(SpecialEventConstants.level_40_img)

    return None

def if_exist_reward() -> bool:
    """
    判断是否存在奖励图标
    :return: 存在返回True, 不存在返回False
    """
    global reward_logo_list
    if not reward_logo_list or len(reward_logo_list) == 0:
        for filename in os.listdir(CommonConstants.reward_logo_dir):
            reward_logo_list.append(filename)

    for filename in reward_logo_list:
        if ClickUtils.get_img_location(CommonConstants.reward_logo_dir + filename):
            return True

    return False


def if_exist_end_reward() -> bool:
    """
    判断是否存在奖励领取结束页面
    :return: 存在返回True, 不存在返回False
    """
    global end_reward_logo_list
    if not end_reward_logo_list or len(end_reward_logo_list) == 0:
        for filename in os.listdir(CommonConstants.end_reward_logo_dir):
            end_reward_logo_list.append(filename)

    for filename in end_reward_logo_list:
        if ClickUtils.get_img_location(CommonConstants.end_reward_logo_dir + filename):
            return True
    return False


def change_world(world_idx):
    '''
    切换世界
    :param world_idx: 世界序数
    :return: 切换成功返回True, 失败返回False
    '''

    # 获取关卡位置
    world_change_loc = get_world_change_loc()
    if world_change_loc is not None:
        # 点击转换世界按钮
        ClickUtils.click_by_location(world_change_loc)
        time.sleep(1)

        world_img = CommonUtils.build_img_path('0' + str(world_idx), DuelConstants.world_logo_dir)
        if ClickUtils.get_img_location(world_img) is None:
            print("未能找到值为 " + str(world_idx) + " 的图标")
            return False

        # 能找到当前对应的世界图标
        ClickUtils.click_by_img(world_img)
        time.sleep(1)
        CommonUtils.click_retry()

        if ClickUtils.get_img_location(world_img) is not None:
            print("当前世界已经为 " + str(world_idx))
            ClickUtils.click_by_location(world_change_loc)
            time.sleep(1)
        return True

def get_world_change_loc():
    guanqia_loc = ClickUtils.get_img_location(CommonConstants.guanqia_img)
    if guanqia_loc is not None:
        return Point(guanqia_loc.x - 43, guanqia_loc.y + 50)
    return None

def get_hao_loc():
    global hao_logo_list
    if not hao_logo_list or len(hao_logo_list) == 0:
        for filename in os.listdir(CommonConstants.hao_logo_dir):
            hao_logo_list.append(filename)

    for filename in hao_logo_list:
        if ClickUtils.get_img_location(CommonConstants.hao_logo_dir + filename):
            return ClickUtils.get_img_location(CommonConstants.hao_logo_dir + filename)
    return None

