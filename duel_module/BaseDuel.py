import time
from functools import wraps

from config.Config import Config
from config.RuntimeContext import RuntimeContext
from constant import CommonConstants
from util import ClickUtils, CommonUtils, DuelUtils, EventUtils


class BaseDuel:
    def __init__(self, config: Config, runtime_context: RuntimeContext):
        self.config = config
        self.runtime_context = runtime_context

    def check_before(self, func):
        """
        检查当前决斗状态是否正常
        :param func:
        :return:
        """

        @wraps(func)
        def wrapper(*args, **kwargs):
            # 检查环境是否正常
            if self.runtime_context.duel_success_flag is False:
                return
            # 执行原始方法
            return func(*args, **kwargs)
        return wrapper

    def duel(self):
        self.prepare()
        self.before_duel()
        self.in_duel()
        self.after_duel()
        self.finish()

    # 决斗开始前
    def before_duel(self):
        if self.runtime_context.duel_success_flag is False:
            return
        retry_cnt = 0

        #  点击对话框直到出现自动决斗图像
        while self.runtime_context.duel_loc is None:
            if ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is None:
                print("没有找到对话框")
                if retry_cnt < 5:
                    retry_cnt = retry_cnt + 1
                    time.sleep(1)
                    continue
                else:
                    self.runtime_context.duel_success_flag = False
                    print("没有进入对话")
                    return

            time.sleep(2)
            print("点击对话框直到出现决斗标签")
            ClickUtils.click_by_img(CommonConstants.dialog_mark_img)
            CommonUtils.click_retry()
            time.sleep(2)
            if ClickUtils.get_img_location(CommonConstants.cancel_img) is not None:
                print("点击取消按钮")
                ClickUtils.click_by_img(CommonConstants.cancel_img)
                time.sleep(1)
            self.runtime_context.duel_loc = DuelUtils.get_duel_logo_loc()

        #  点击自动决斗
        time.sleep(2)
        ClickUtils.click_by_location(self.runtime_context.duel_loc)
        time.sleep(2)
        CommonUtils.click_retry()
        self.runtime_context.duel_success_flag = True
        print("进入决斗")

    # 决斗进行中
    def in_duel(self):
        if self.runtime_context.duel_success_flag is False:
            return

        self.runtime_context.end_duel_loc = None
        # 循环等待决斗结束
        while self.runtime_context.end_duel_loc is None:
            CommonUtils.click_retry()
            print("决斗尚未结束，继续等待5秒")
            time.sleep(5)
            self.runtime_context.end_duel_loc = ClickUtils.get_img_location(CommonConstants.end_duel_img)
        ClickUtils.click_by_location(self.runtime_context.end_duel_loc)
        print("决斗结束")
        time.sleep(3)
        CommonUtils.click_retry()

    # 决斗结束后
    def after_duel(self):
        if self.runtime_context.duel_success_flag is False:
            return

        # 1. 点击奖励直到不存在奖励标志和出现奖励结束标志
        while DuelUtils.if_exist_reward() is True or DuelUtils.if_exist_end_reward() is False:
            flag = False
            time.sleep(1)

            # 点击决斗评价加速
            if ClickUtils.get_img_location(CommonConstants.duel_evaluation_img) is not None:
                ClickUtils.click_by_img(CommonConstants.duel_evaluation_img)
                time.sleep(1)

            if ClickUtils.get_img_location(CommonConstants.next_step_img) is not None:
                ClickUtils.click_by_img(CommonConstants.next_step_img)
                flag = True
                print("点击下一步")
                CommonUtils.click_retry()

            if DuelUtils.get_hao_loc() is not None:
                ClickUtils.click_by_location(DuelUtils.get_hao_loc())
                flag = True
                print("点击好")
                CommonUtils.click_retry()

            if ClickUtils.get_img_location(CommonConstants.back_img) is not None:
                ClickUtils.click_by_img(CommonConstants.back_img)
                flag = True
                print("点击后退")
                CommonUtils.click_retry()

            if flag is False and ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is None\
                    and ClickUtils.get_img_location(CommonConstants.guanqia_img) is None:
                # 什么都没点击到，并且没有出现对话框
                print("随便点击一个位置")
                ClickUtils.click_by_location(self.runtime_context.end_duel_loc)
                CommonUtils.click_retry()
            time.sleep(2)

        # 2. 循环点击对话框直到对话框消失
        while ClickUtils.get_img_location(CommonConstants.dialog_mark_img) is not None:
            print("活动结束后点击对话框")
            ClickUtils.click_by_img(CommonConstants.dialog_mark_img)
            CommonUtils.click_retry()
            time.sleep(1)

        if self.config.if_special_event_duel is True and EventUtils.if_exist_activity():
            self.runtime_context.special_event_file_name = EventUtils.get_activity_file_name()

        # 3. 决斗结束后点击取消、关闭、后退
        while ClickUtils.get_img_location(CommonConstants.cancel_img) is not None \
               or ClickUtils.get_img_location(CommonConstants.close_button_img) is not None \
               or ClickUtils.get_img_location(CommonConstants.back_img) is not None:

            time.sleep(3)
            if self.config.if_special_event_duel is True and EventUtils.if_exist_activity():
                self.runtime_context.special_event_file_name = EventUtils.get_activity_file_name()
            if ClickUtils.click_by_img(CommonConstants.cancel_img):
                CommonUtils.click_retry()
                continue
            time.sleep(1)
            if ClickUtils.click_by_img(CommonConstants.close_button_img):
                CommonUtils.click_retry()
                continue
            time.sleep(1)
            if ClickUtils.click_by_img(CommonConstants.back_img):
                CommonUtils.click_retry()
                continue
            time.sleep(1)

        print("决斗流程结束")
        self.runtime_context.duel_loc = None


    def prepare(self):
        pass

    def finish(self):
        self.runtime_context.duel_success_flag = True
