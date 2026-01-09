# 项目主文件说明

本项目包含两个主要的入口文件，分别用于国服和国际服的自动化功能。

## 文件结构

### 1. GuofuMain.py - 国服主程序
**适用于：** 游戏王决斗链接国服

**包含功能：**
- ✅ 先手投降自动化 (`FirstHandSurrenderDuel`)
- ✅ 卡片商人兑换卡片 (`CardTraderExchange`)

**使用方法：**
```bash
python GuofuMain.py
```

**代码示例：**
```python
# 先手投降（默认启用）
first_hand_surrender = FirstHandSurrenderDuel(config, runtime_context)
for i in range(1000):
    first_hand_surrender.run()

# 卡片商人兑换
card_trader = CardTraderExchange(config, runtime_context)
card_trader.run(card_rarity="precious")  # 珍贵卡片
```

**所需图片目录：**
- 先手投降：`img/guofu/first_hand_surrender/`
- 卡片商人：`img/guofu/card_trader/`

---

### 2. main.py - 国际服主程序
**适用于：** 游戏王决斗链接国际服

**包含功能：**
- ✅ 路人决斗 (`PasserDuelV2`)
- ✅ 传送门决斗 (`PortalDuel`)
- ✅ 决斗者王国 (`DuelistKingdomDuel`)
- ✅ 救援决斗 (`RescueDuel`)
- ✅ 波动决斗 (`WaveDuel`)
- ✅ 技能获取 (`SkillUtils`)

**使用方法：**
```bash
python main.py
```

**代码示例：**
```python
# 决斗者王国（默认启用）
duelist_kingdom_duel = DuelistKingdomDuel(config, runtime_context)
for i in range(1000):
    duelist_kingdom_duel.duel()

# 路人决斗
# passer_duel = PasserDuelV2(config, runtime_context)
# for i in range(1000):
#     passer_duel.run()
```

---

## 快速开始

### 运行国服功能
1. 准备好对应功能所需的图片
2. 打开 `GuofuMain.py`
3. 取消想要运行的功能的注释
4. 运行：`python GuofuMain.py`

### 运行国际服功能
1. 打开 `main.py`
2. 取消想要运行的功能的注释
3. 运行：`python main.py`

---

## 注意事项

1. **图片准备：** 运行前请确保已准备好对应功能所需的所有图片
2. **窗口可见：** 确保游戏窗口不被遮挡
3. **分辨率一致：** 截图时的分辨率应与运行时保持一致
4. **测试运行：** 建议先测试运行一次，确保所有图片识别正常

---

## 目录结构

```
yugioh_auto_duel/
├── GuofuMain.py              # 国服主程序
├── main.py                    # 国际服主程序
├── duel_module/               # 决斗模块
│   ├── FirstHandSurrenderDuel.py    # 先手投降
│   ├── CardTraderExchange.py        # 卡片商人兑换
│   ├── PasserDuelV2.py              # 路人决斗
│   ├── PortalDuel.py                # 传送门决斗
│   ├── DuelistKingdomDuel.py        # 决斗者王国
│   ├── RescueDuel.py                # 救援决斗
│   └── WaveDuel.py                  # 波次决斗
├── constant/                  # 常量定义
│   ├── FirstHandSurrenderConstants.py  # 先手投降常量
│   ├── CardTraderConstants.py          # 卡片商人常量
│   └── ...
└── img/                       # 图片资源
    ├── guofu/                 # 国服图片
    │   ├── first_hand_surrender/
    │   └── card_trader/
    └── guojifu/               # 国际服图片
        └── ...
```

---

## 常见问题

**Q: 如何切换运行的功能？**
A: 在对应的主文件中，注释掉当前运行的功能，取消注释想要运行的功能即可。

**Q: 图片识别不准确怎么办？**
A: 可以在代码中调整 `confidence` 参数（默认0.9），或重新截取更清晰的图片。

**Q: 可以同时运行多个功能吗？**
A: 不建议。建议一次只运行一个功能，避免冲突。

**Q: 如何停止运行？**
A: 按 `Ctrl + C` 即可中断程序。

---

## 联系与反馈

如有问题或建议，欢迎反馈！

