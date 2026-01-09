# 点击重试
import time

from util import ClickUtils




def click_retry():
    time.sleep(1)
    retry_img = build_img_path('retry', 'img/guojifu/common/')
    while ClickUtils.get_img_location(retry_img) is not None:
        ClickUtils.click_by_img(retry_img)
        time.sleep(3)


def build_img_path(img_name, img_path='img/guojifu/Common/', suffix='.png'):
    return img_path + img_name + suffix

def cal_dis(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5