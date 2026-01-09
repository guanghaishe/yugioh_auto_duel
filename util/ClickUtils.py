import time

import pyautogui
import pyscreeze

from util import CommonUtils


def click_by_img(target_img, x_offset=0, y_offset=0, confidence=0.9):
    try:
        location = pyautogui.locateCenterOnScreen(target_img, confidence=confidence)
        pyautogui.click(location.x + x_offset, location.y + y_offset, clicks=1, interval=0.2, duration=0.2, button="left")
        time.sleep(1)
        return True
    except pyautogui.ImageNotFoundException:
        print(f"没有找到图片：{target_img}")
        return False
    except Exception as e:
        print(f"click_by_img 异常: {e}")
        return False

def click_by_img_if_exist(target_img):
    while get_img_location(target_img) is not None:
        click_by_img(target_img)
        time.sleep(1)
        CommonUtils.click_retry()


def click_by_pos(pos_x, pos_y):
    try:
        pyautogui.click(pos_x, pos_y, clicks=1, interval=0.2, duration=0.2, button="left")
        time.sleep(1)
        return True
    except Exception as e:
        print(f"click_by_pos 异常: {e}")
        return False


def click_by_location(location):
    try:
        pyautogui.click(location.x, location.y, clicks=1, interval=0.2, duration=0.2, button="left")
        time.sleep(1)
        return True
    except Exception as e:
        print(f"click_by_location 异常: {e}")
        return False

def click_by_location_if_exist(location):
    if location is not None:
        click_by_location(location)


def get_img_location(target_img, confidence=0.9):
    try:
        location = pyautogui.locateCenterOnScreen(target_img, confidence=confidence)
        return location
    except pyautogui.ImageNotFoundException:
        # print(f"没有找到图片：{target_img}")
        return None
    except Exception as e:
        print(f"get_img_location 异常: {e}")
        return None

