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
- 取消对应功能的注释即可运行
- 国服功能请使用 GuofuMain.py
"""

import time

import SkillUtils
from config.Config import Config
from config.RuntimeContext import RuntimeContext
from duel_module.DuelistKingdomDuel import DuelistKingdomDuel
from duel_module.PasserDuelV2 import PasserDuelV2
from duel_module.PortalDuel import PortalDuel
from duel_module.RescueDuel import RescueDuel
from duel_module.TagDuelTournamentDuel import TagDuelTournamentDuel
from duel_module.WaveDuel import WaveDuel
from duel_module.RewardExtract import RewardExtract

if __name__ == "__main__":
    config = Config()
    runtime_context = RuntimeContext()

    # root = tk.Tk()
    # app = YugiohGUI(root, config, runtime_context)
    # root.mainloop()
    
    # --------------------------------------------------
    # 路人决斗 - PasserDuelV2
    # --------------------------------------------------
    passer_duel = PasserDuelV2(config, runtime_context)
    for i in range(1000):
        passer_duel.run()
        print("第 " + str(i+1) + " 次路人清理结束")
        time.sleep(120)

    # --------------------------------------------------
    # 传送门决斗 - PortalDuel
    # --------------------------------------------------
    # portal_duel = PortalDuel(config, runtime_context)
    # for i in range(1000):
    #     portal_duel.duel()

    # --------------------------------------------------
    # 决斗者王国 - DuelistKingdomDuel
    # --------------------------------------------------
    # duelist_kingdom_duel = DuelistKingdomDuel(config, runtime_context)
    # for i in range(1000):
    #     duelist_kingdom_duel.duel()

    # --------------------------------------------------
    # 技能获取 - SkillUtils
    # --------------------------------------------------
    # SkillUtils.get_skill()

    # --------------------------------------------------
    # 救援决斗 - RescueDuel
    # --------------------------------------------------
    # rescue_duel = RescueDuel(config, runtime_context)
    # for i in range(1000):
    #     rescue_duel.work()

    # --------------------------------------------------
    # 波动决斗 - WaveDuel
    # --------------------------------------------------
    # waveDuel = WaveDuel(config, runtime_context)
    # for i in range(1000):
    #     waveDuel.duel()


    # --------------------------------------------------
    # 组队决斗 - TagDuel
    # --------------------------------------------------
    # tagDuelTournamentDuel = TagDuelTournamentDuel(config, runtime_context)
    # for i in range(1000):
    #     tagDuelTournamentDuel.duel()
    #     time.sleep(3)

    # --------------------------------------------------
    # 奖励抽取 - RewardExtract
    # --------------------------------------------------
    # reward_extract = RewardExtract(config, runtime_context)
    # for i in range(1000):
    #     reward_extract.extractLotteryReward()
    #     time.sleep(0.5)

