"""
国服主程序
GuoFu Main - 游戏王决斗链接国服自动化脚本

包含功能：
1. 先手投降自动化（FirstHandSurrenderDuel）
2. 卡片商人兑换卡片（CardTraderExchange）
3. 自动领取技能（SkillCollect）

使用方法：
- 取消对应功能的注释即可运行
- 国际服功能请使用 main.py
"""

import time

from config.Config import Config
from config.RuntimeContext import RuntimeContext
from duel_module.FirstHandSurrenderDuel import FirstHandSurrenderDuel
from duel_module.CardTraderExchange import CardTraderExchange
from duel_module.SkillCollect import SkillCollect

if __name__ == "__main__":
    config = Config()
    runtime_context = RuntimeContext()

    # --------------------------------------------------
    # 先手投降自动化 - FirstHandSurrenderDuel
    # --------------------------------------------------
    # first_hand_surrender = FirstHandSurrenderDuel(config, runtime_context)
    # for i in range(1000):
    #     first_hand_surrender.run()
    #     print(f"第 {i+1} 次先手投降流程完成")
    #     time.sleep(5)

    # --------------------------------------------------
    # 卡片商人兑换卡片 - CardTraderExchange
    # --------------------------------------------------
    # 稀有度选项：precious(珍贵), rare(稀有), super_rare(超凡), normal(普通)
    # card_trader = CardTraderExchange(config, runtime_context)
    # card_trader.run(card_rarity="precious")  # 珍贵卡片
    # card_trader.run(card_rarity="rare")      # 稀有卡片
    # card_trader.run(card_rarity="super_rare") # 超凡卡片
    # card_trader.run(card_rarity="normal")    # 普通卡片

    # --------------------------------------------------
    # 自动领取技能 - SkillCollect
    # --------------------------------------------------
    skill_collect = SkillCollect(config, runtime_context)
    skill_collect.run()

