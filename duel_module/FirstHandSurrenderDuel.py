import time

from config.Config import Config
from config.RuntimeContext import RuntimeContext
from constant import FirstHandSurrenderConstants
from util import ClickUtils, CommonUtils


class FirstHandSurrenderDuel:
    """
    先手投降决斗类
    用于国服先手投降的脚本
    """

    def __init__(self, config: Config, runtime_context: RuntimeContext):
        self.config = config
        self.runtime_context = runtime_context

    def run(self):
        """
        执行先手投降流程
        """
        print("=" * 50)
        print("开始先手投降流程")
        print("=" * 50)

        # 步骤1: 在主页面，点击决斗按钮
        self.click_duel_button()

        # 步骤2: 等待进入决斗
        self.wait_enter_duel()

        # 步骤3-8: 判断回合并执行相应操作
        self.handle_turn()

        print("=" * 50)
        print("先手投降流程结束")
        print("=" * 50)

    def click_duel_button(self):
        """
        步骤1: 点击主页面的决斗按钮
        """
        print("=" * 50)
        print("步骤1: 等待并点击主页面决斗按钮")
        print("=" * 50)
        
        wait_count = 0
        while True:
            if ClickUtils.click_by_img(FirstHandSurrenderConstants.duel_button_img):
                print(f"[成功] 找到并点击了决斗按钮")
                time.sleep(2)
                return
            else:
                wait_count += 1
                if wait_count % 5 == 1:  # 每5次打印一次日志，避免刷屏
                    print(f"[等待中] 未找到决斗按钮，继续等待... (已等待 {wait_count} 次)")
                time.sleep(2)

    def wait_enter_duel(self):
        """
        步骤2: 等待进入决斗（检测到回合图片）
        """
        print("=" * 50)
        print("步骤2: 等待进入决斗界面")
        print("=" * 50)
        
        wait_count = 0
        while True:
            # 检测是否进入决斗（出现回合图片）
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.round_img) is not None:
                print(f"[成功] 检测到回合标识，已进入决斗")
                time.sleep(2)
                return
            else:
                wait_count += 1
                if wait_count % 3 == 1:  # 每3次打印一次日志
                    print(f"[等待中] 等待进入决斗界面... (已等待 {wait_count * 2} 秒)")
                time.sleep(2)

    def handle_turn(self):
        """
        步骤3-8: 判断回合并执行相应操作
        """
        print("=" * 50)
        print("步骤3: 判断当前回合归属")
        print("=" * 50)

        # 等待回合1图片出现
        print("[等待中] 等待回合1图片出现...")
        wait_count = 0
        while True:
            # 检测对手是否提前投降
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.confirm_img) is not None:
                print(f"[检测到] 对手在回合开始前就投降了")
                self.handle_opponent_surrender()
                return
            
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.round1_img) is not None:
                print(f"[成功] 检测到回合1标识")
                break
            wait_count += 1
            if wait_count % 3 == 1:
                print(f"[等待中] 继续等待回合1图片... (已等待 {wait_count * 2} 秒)")
            time.sleep(2)

        # 判断是自己先手还是对手先手
        time.sleep(2)
        print("[检测中] 判断回合归属...")
        
        wait_count = 0
        while True:
            # 检测对手是否在判断回合归属时投降
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.confirm_img) is not None:
                print(f"[检测到] 对手在回合归属判断时投降了")
                self.handle_opponent_surrender()
                return
            
            is_your_turn = ClickUtils.get_img_location(FirstHandSurrenderConstants.your_turn_img) is not None
            is_opponent_turn = ClickUtils.get_img_location(FirstHandSurrenderConstants.opponent_turn_img) is not None

            if is_your_turn:
                # 情况1: 自己先手
                print("[判断成功] 检测到自己先手（回合1是你）")
                self.surrender_immediately()
                return
            elif is_opponent_turn:
                # 情况2: 对手先手
                print("[判断成功] 检测到对手先手（回合1是对手）")
                self.handle_opponent_first_turn()
                return
            else:
                wait_count += 1
                if wait_count % 3 == 1:
                    print(f"[等待中] 等待回合归属标识出现... (已等待 {wait_count * 2} 秒)")
                time.sleep(2)

    def surrender_immediately(self):
        """
        步骤5: 自己先手时立即投降
        """
        print("=" * 50)
        print("步骤5: 自己先手，开始投降流程")
        print("=" * 50)
        self.execute_surrender()
        self.wait_return_home()

    def execute_surrender(self):
        """
        执行投降操作: 点击菜单 -> 点击认输 -> 点击确定
        """
        # 步骤1: 点击菜单按钮
        print("[投降流程] 第1步: 等待并点击菜单按钮")
        wait_count = 0
        while True:
            if ClickUtils.click_by_img(FirstHandSurrenderConstants.menu_img):
                print(f"[成功] 找到并点击了菜单按钮")
                time.sleep(2)
                break
            wait_count += 1
            if wait_count % 3 == 1:
                print(f"[等待中] 未找到菜单按钮，继续等待... (已等待 {wait_count * 2} 秒)")
            time.sleep(2)

        # 步骤2: 点击认输按钮（如果菜单关闭了需要重新打开）
        print("[投降流程] 第2步: 等待并点击认输按钮")
        wait_count = 0
        while True:
            # 先检查认输按钮是否存在
            if ClickUtils.click_by_img(FirstHandSurrenderConstants.surrender_img):
                print(f"[成功] 找到并点击了认输按钮")
                time.sleep(2)
                break
            
            # 如果没有找到认输按钮，检查菜单按钮是否又出现了（说明菜单界面关闭了）
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.menu_img) is not None:
                print(f"[检测到] 菜单界面已关闭，重新打开菜单")
                if ClickUtils.click_by_img(FirstHandSurrenderConstants.menu_img):
                    print(f"[成功] 重新点击了菜单按钮")
                    time.sleep(2)
                    continue  # 继续下一次循环尝试点击认输
            
            wait_count += 1
            if wait_count % 3 == 1:
                print(f"[等待中] 未找到认输按钮，继续等待... (已等待 {wait_count * 2} 秒)")
            time.sleep(2)

        # 步骤3: 点击确定按钮
        print("[投降流程] 第3步: 等待并点击确定按钮")
        wait_count = 0
        while True:
            if ClickUtils.click_by_img(FirstHandSurrenderConstants.confirm_img):
                print(f"[成功] 找到并点击了确定按钮")
                time.sleep(2)
                break
            wait_count += 1
            if wait_count % 3 == 1:
                print(f"[等待中] 未找到确定按钮，继续等待... (已等待 {wait_count * 2} 秒)")
            time.sleep(2)

        print("[投降流程] 投降操作完成")
        time.sleep(1)

    def handle_opponent_first_turn(self):
        """
        步骤6-8: 处理对手先手的情况
        """
        print("=" * 50)
        print("步骤6: 对手先手，等待对手回合结束")
        print("=" * 50)
        print("[等待中] 不断点击【对手】图片，等待对手操作完成")

        click_count = 0
        while True:
            # 检查是否还能看到对手图片
            opponent_loc = ClickUtils.get_img_location(FirstHandSurrenderConstants.opponent_turn_img)

            # 检查对手是否投降
            has_confirm = ClickUtils.get_img_location(FirstHandSurrenderConstants.confirm_img) is not None
            
            if has_confirm:
                print(f"[检测到] 对手投降标识")
                self.handle_opponent_surrender()
                return

            # 检查是否已经到回合2
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.your_turn_img) is not None \
                or ClickUtils.get_img_location(FirstHandSurrenderConstants.round2_img) is not None:
                print(f"[检测到] 回合2标识，对手未投降")
                self.handle_round2()
                return

            # 如果还能看到对手图片，继续点击
            if opponent_loc is not None:
                ClickUtils.click_by_location(opponent_loc)
                click_count += 1
                if click_count % 5 == 1:  # 每5次打印一次
                    print(f"[等待中] 点击对手图片，加速回合结束... (已点击 {click_count} 次)")
                time.sleep(2)
            else:
                # 对手图片消失，等待判断是投降还是进入回合2
                if click_count % 3 == 1:
                    print(f"[等待中] 对手图片消失，等待判断情况...")
                time.sleep(2)

    def handle_opponent_surrender(self):
        """
        步骤7: 处理对手投降的情况
        """
        print("=" * 50)
        print("步骤7: 对手已投降，准备返回主页面")
        print("=" * 50)
        time.sleep(2)

        # 点击确定按钮
        print("[等待中] 等待并点击确定按钮")
        wait_count = 0
        while True:
            if ClickUtils.click_by_img(FirstHandSurrenderConstants.confirm_img):
                print(f"[成功] 找到并点击了确定按钮")
                time.sleep(2)
                break
            wait_count += 1
            if wait_count % 3 == 1:
                print(f"[等待中] 等待确定按钮出现... (已等待 {wait_count * 2} 秒)")
            time.sleep(2)

        self.wait_return_home()

    def handle_round2(self):
        """
        步骤8: 处理回合2的情况（对手不投降）
        """
        print("=" * 50)
        print("步骤8: 对手未投降，进入回合2")
        print("=" * 50)
        time.sleep(2)

        # 不断点击【你】图片，直到检测到确定按钮
        print("[等待中] 不断点击【你】图片，加速游戏进程")
        click_count = 0

        while True:
            # 检查是否出现确定按钮
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.confirm_img) is not None:
                print(f"[检测到] 确定按钮出现，准备返回")
                break

            # 尝试点击【你】图片
            your_turn_loc = ClickUtils.get_img_location(FirstHandSurrenderConstants.your_turn_img)
            if your_turn_loc is not None:
                ClickUtils.click_by_location(your_turn_loc)
                click_count += 1
                if click_count % 5 == 1:  # 每5次打印一次
                    print(f"[等待中] 点击【你】图片，加速回合结束... (已点击 {click_count} 次)")
            else:
                if click_count % 3 == 1:
                    print(f"[等待中] 未检测到【你】图片，继续等待确定按钮...")

            time.sleep(2)

        # 点击确定按钮
        print("[等待中] 等待并点击确定按钮")
        wait_count = 0
        while True:
            if ClickUtils.click_by_img(FirstHandSurrenderConstants.confirm_img):
                print(f"[成功] 找到并点击了确定按钮")
                time.sleep(2)
                break
            wait_count += 1
            if wait_count % 3 == 1:
                print(f"[等待中] 等待确定按钮... (已等待 {wait_count * 2} 秒)")
            time.sleep(2)

        self.wait_return_home()

    def wait_return_home(self):
        """
        等待返回主页面
        不断点击确定或下一步，直到检测到决斗按钮
        """
        print("=" * 50)
        print("等待返回主页面")
        print("=" * 50)
        print("[等待中] 不断点击确定/下一步按钮直到返回主页面")
        
        click_count = 0
        wait_count = 0

        while True:
            # 检查是否已经回到主页面（出现决斗按钮）
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.duel_button_img) is not None:
                print(f"[成功] 检测到决斗按钮，已返回主页面")
                time.sleep(2)
                return

            # 尝试点击确定按钮
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.confirm_img) is not None:
                ClickUtils.click_by_img(FirstHandSurrenderConstants.confirm_img)
                click_count += 1
                if click_count % 3 == 1:
                    print(f"[操作中] 点击确定按钮... (第 {click_count} 次)")
                time.sleep(2)
                continue

            # 尝试点击下一步按钮
            if ClickUtils.get_img_location(FirstHandSurrenderConstants.next_step_img) is not None:
                ClickUtils.click_by_img(FirstHandSurrenderConstants.next_step_img)
                click_count += 1
                if click_count % 3 == 1:
                    print(f"[操作中] 点击下一步按钮... (第 {click_count} 次)")
                time.sleep(2)
                continue

            # 如果没有检测到任何按钮，等待一下
            wait_count += 1
            if wait_count % 5 == 1:
                print(f"[等待中] 等待返回主页面相关按钮出现... (已等待 {wait_count * 2} 秒)")
            time.sleep(2)

