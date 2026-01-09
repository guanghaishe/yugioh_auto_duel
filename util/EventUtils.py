import os

from constant import SpecialEventConstants
from util import ClickUtils

activity_logo_list = []
event_Logo_list = []

def if_exist_activity():
    """
    判断是否存在活动事件
    :return: 存在返回True, 不存在返回False
    """
    for filename in get_activity_logo_list():
        if ClickUtils.get_img_location(SpecialEventConstants.special_event_logo_dir + filename):
            print("发现了活动事件:" + filename)
            return True

    for filename in get_event_logo_list():
        if ClickUtils.get_img_location(SpecialEventConstants.event_logo_dir + filename):
            print("发现了活动事件:" + filename)
            return True
    return False


def get_activity_file_name():
    """
    获取活动事件名
    :return: 活动事件名
    """
    activity_file_name = None
    for filename in get_activity_logo_list():
        if ClickUtils.get_img_location(SpecialEventConstants.special_event_logo_dir + filename):
            print("获取到活动事件名:" + filename)
            activity_file_name = filename
    for filename in get_event_logo_list():
        if ClickUtils.get_img_location(SpecialEventConstants.event_logo_dir + filename):
            print("获取到活动事件名:" + filename)
            activity_file_name = filename
    return activity_file_name

def get_activity_logo_list():
    global activity_logo_list
    if not activity_logo_list or len(activity_logo_list) == 0:
        for filename in os.listdir(SpecialEventConstants.special_event_logo_dir):
            activity_logo_list.append(filename)
    return activity_logo_list

def get_event_logo_list():
    global event_Logo_list
    if not event_Logo_list or len(event_Logo_list) == 0:
        for filename in os.listdir(SpecialEventConstants.event_logo_dir):
            event_Logo_list.append(filename)
    return event_Logo_list