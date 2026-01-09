'''
特殊事件决斗相关
'''
import os

from util import CommonUtils


rescue_duel_logo_dir = 'img/guojifu/event/rescue duel logos/'


event_img = CommonUtils.build_img_path('event', rescue_duel_logo_dir)
duel_img = CommonUtils.build_img_path('duel', rescue_duel_logo_dir)
# 让它立刻出现
appear_immediately_img = CommonUtils.build_img_path('appear immediately', rescue_duel_logo_dir)
# 使用
use_img = CommonUtils.build_img_path('use', rescue_duel_logo_dir)
# 出现了
appeared_img = CommonUtils.build_img_path('appeared', rescue_duel_logo_dir)
# 救援决斗
rescue_duel_img = CommonUtils.build_img_path('rescue duel', rescue_duel_logo_dir)

