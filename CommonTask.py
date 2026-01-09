import time

from constant import OtherConstants
from util import ClickUtils, DuelUtils


def collect_gems():
    # 1. 点击收取所有
    ClickUtils.click_by_img(OtherConstants.collect_all_img)
    time.sleep(2)
    # 2. 点击好
    hao_loc = DuelUtils.get_hao_loc()
    while hao_loc is None:
        hao_loc = DuelUtils.get_hao_loc()
        time.sleep(1)
    ClickUtils.click_by_location(hao_loc)
    time.sleep(2)

    # 3. 向左翻页
    ClickUtils.click_by_img(OtherConstants.turn_left_img)
    time.sleep(2)


if __name__ == '__main__':
    # 收取宝石
    for i in range(30):
        collect_gems()
