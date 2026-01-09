import time

import pyautogui

from constant import OtherConstants, CommonConstants
from util import ClickUtils, DuelUtils


def get_skill():
    while True:
        skill_logo_loc = get_skill_logo_loc()
        if skill_logo_loc is None:
            print("所有技能都已获取完毕")
            break

        # 1. 点击技能
        ClickUtils.click_by_location(skill_logo_loc)
        time.sleep(1)

        # 2. 判断是否可交易
        skill_detail_loc = None
        while ClickUtils.get_img_location(OtherConstants.tradeable_img) is None:
            if skill_detail_loc is None:
                skill_detail_loc = ClickUtils.get_img_location(OtherConstants.skill_detail_img)
                ClickUtils.click_by_pos(skill_detail_loc.x, skill_detail_loc.y + 100)

            time.sleep(0.5)
            pyautogui.scroll(-10000)
            print("向下滑动")
            continue

        # 3. 点击交易
        ClickUtils.click_by_img(OtherConstants.tradeable_img)
        time.sleep(1)
        ClickUtils.click_by_img(OtherConstants.trade_img)

        # 4. 点击好
        hao_loc = DuelUtils.get_hao_loc()
        while hao_loc is None:
            hao_loc = DuelUtils.get_hao_loc()
            time.sleep(1)
        ClickUtils.click_by_location(hao_loc)


def get_skill_logo_loc():
    if ClickUtils.get_img_location(OtherConstants.skill_logo_img) is not None:
        return ClickUtils.get_img_location(OtherConstants.skill_logo_img)

    if ClickUtils.get_img_location(OtherConstants.skill_logo_v2_img) is not None:
        return ClickUtils.get_img_location(OtherConstants.skill_logo_v2_img)

    return None
