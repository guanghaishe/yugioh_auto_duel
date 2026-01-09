# 卡片商人兑换卡片功能

## 功能说明
这个功能可以自动执行卡片商人兑换卡片的完整流程，支持不同稀有度的卡片筛选和兑换。

## 图片文件说明
请将以下图片文件放在 `img/guofu/card_trader/` 目录下：

### 必需图片文件：
1. `card_exchange_shop.png` - 卡片兑换商店按钮
2. `more_options_triangle.png` - 更多选项（倒三角形）按钮
3. `filter_conditions.png` - 筛选条件按钮
4. `filter_conditions_confirm.png` - 筛选条件确认按钮（字比较大的《筛选条件》）
5. `collect_cards.png` - 收取卡片按钮
6. `back_button.png` - 返回按钮
7. `confirm_button.png` - 确认按钮
8. `trade_button.png` - 交易按钮
9. `card_quantity_0.png` - 卡片数量为0的图片（用于检查是否还有可兑换的卡片）
10. `card_quantity_1.png` - 卡片数量为1的图片（用于检查是否还有可兑换的卡片）
11. `card_quantity_2.png` - 卡片数量为2的图片（用于检查是否还有可兑换的卡片）

**注意：** 添加按钮不再需要图片，采用与收取卡片位置偏差值的方式点击

### 稀有度筛选图片（选择其中一个）：
- `precious_filter.png` - 珍贵筛选选项
- `rare_filter.png` - 稀有筛选选项
- `super_rare_filter.png` - 超凡筛选选项
- `normal_filter.png` - 普通筛选选项

## 使用方法

### 在main.py中调用：
```python
# 卡片商人兑换卡片功能
card_trader = CardTraderExchange(config, runtime_context)
# 参数说明：
# card_rarity: 卡片稀有度，可选值：precious(珍贵), rare(稀有), super_rare(超凡), normal(普通)
card_trader.run(card_rarity="precious")
```

### 参数说明：
- `card_rarity`: 要兑换的卡片稀有度
  - `"precious"` - 珍贵
  - `"rare"` - 稀有
  - `"super_rare"` - 超凡
  - `"normal"` - 普通

### 偏移量设置：
偏移量已预设，如需修改请编辑 `duel_module/CardTraderExchange.py` 文件中的相关方法：

**收取卡片偏移量**（`_click_collect_cards_with_offset` 方法）：
```python
def _click_collect_cards_with_offset(self):
    # 预设的偏移量，您可以根据实际情况修改这些值
    x_offset = 0  # x轴偏移量（像素）
    y_offset = 900  # y轴偏移量（像素）
```

**添加按钮偏移量**（`_click_add_button_with_offset` 方法）：
```python
def _click_add_button_with_offset(self):
    # 预设的添加按钮偏移量，相对于收取卡片按钮的位置
    add_button_x_offset = 0  # 添加按钮的x轴偏移量（像素）
    add_button_y_offset = 100  # 添加按钮的y轴偏移量（像素）
```

## 执行流程
1. 点击卡片兑换商店
2. 点击更多选项（倒三角形）
3. 点击筛选条件
4. 向下滑动找到对应稀有度并点击
5. 点击筛选条件确认按钮
6. 等待2秒界面加载
7. 检查卡片数量，如果找不到数量为0、1、2的图片，说明所有卡片已满三，停止脚本
8. 点击收取卡片按钮（应用偏移量）
9. 点击添加按钮（使用偏移量）
10. 点击返回按钮
11. 点击确认按钮
12. 点击交易按钮
13. 等待5秒
14. 重复执行10次

## 注意事项
- 所有图片文件必须是PNG格式
- 脚本会循环执行10次
- 每个步骤之间有1.5秒的等待时间
- 如果某个步骤找不到对应图片，脚本会一直等待直到找到为止
- 偏移量已预设，如需修改请编辑代码中的 `_click_collect_cards_with_offset` 方法
