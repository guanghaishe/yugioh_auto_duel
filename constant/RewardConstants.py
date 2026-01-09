'''
奖励抽取相关常量
'''
from util import CommonUtils

reward_logo_dir = 'img/guojifu/event/reward logos/'

# 彩票奖励列表按钮图片路径 (请填写实际图片名称)
lottery_reward_list_img = CommonUtils.build_img_path('lottery_reward_list', reward_logo_dir)

# 点击偏移量 - 从彩票奖励列表按钮向下偏移的像素值
LOTTERY_CLICK_OFFSET_Y = 170
