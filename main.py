"""
国际服主程序
International Server Main - 游戏王决斗链接国际服自动化脚本

包含功能：
1. 路人决斗（PasserDuelV2）
2. 传送门决斗（PortalDuel）
3. 决斗者王国（DuelistKingdomDuel）
4. 救援决斗（RescueDuel）
5. 波动决斗（WaveDuel）
6. 技能获取（SkillUtils）

使用方法：
- 运行程序后在 GUI 界面选择对应功能并点击开始
"""
import time
import tkinter as tk
from config.Config import Config
from config.RuntimeContext import RuntimeContext
from duel_module.PasserDuelV2 import PasserDuelV2
from duel_module.RescueDuel import RescueDuel
from gui.YugiohGUI import YugiohGUI

if __name__ == "__main__":
    config = Config()
    runtime_context = RuntimeContext()

    # passerDuel = PasserDuelV2(config, runtime_context)
    # for i in range(100):
    #     print(f"准备运行第 {i+1} 次 路人决斗")
    #     passerDuel.run()
    #     time.sleep(300)  # 每次决斗后等待5分钟
    #     print(f"第 {i+1} 次 路人决斗 完成, 时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

    # rescueDuel = RescueDuel(config, runtime_context)
    # for i in range(100):
    #     rescueDuel.work()
    #     print(f"第 {i+1} 次救援决斗完成, 时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")

    root = tk.Tk()
    app = YugiohGUI(root, config, runtime_context)
    root.mainloop()

