import sys
import threading
import time
import tkinter as tk
from tkinter import messagebox, scrolledtext

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


class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str):
        self.text_widget.insert(tk.END, str)
        self.text_widget.see(tk.END)

    def flush(self):
        pass


class YugiohGUI:
    def __init__(self, master, config: Config, runtime_context: RuntimeContext):
        self.master = master
        self.master.title("Yugioh Bot - 决斗助手")

        # 设置窗口大小和居中显示
        window_width = 600
        window_height = 700
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # 计算窗口的居中位置
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)
        self.master.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

        # 决斗相关变量
        self.duel_type = tk.StringVar()
        self.duel_times = tk.StringVar(value="1000")  # 默认运行1000次
        self.config = config
        self.runtime_context = runtime_context

        # 用于控制停止的标志
        self.stop_flag = False
        self.duel_thread = None

        self.create_widgets()

        # 重定向标准输出
        sys.stdout = StdoutRedirector(self.log_text)

    def create_widgets(self):
        # 功能选择区域
        options_frame = tk.LabelFrame(self.master, text="功能选择", padx=10, pady=10)
        options_frame.pack(fill="x", padx=10, pady=5)

        functions = [
            ("路人决斗", "passer_duel"),
            ("传送门决斗", "portal_duel"),
            ("决斗者王国", "duelist_kingdom"),
            ("技能获取", "skill_get"),
            ("救援决斗", "rescue_duel"),
            ("波动决斗", "wave_duel"),
            ("组队决斗", "tag_duel"),
            ("奖励抽取", "reward_extract"),
        ]

        # 每行显示3个功能
        for i, (text, value) in enumerate(functions):
            row = i // 3
            col = i % 3
            tk.Radiobutton(options_frame, text=text, variable=self.duel_type, value=value).grid(row=row, column=col, sticky="w", padx=10)

        self.duel_type.set("passer_duel")

        # 次数设置区域
        times_frame = tk.LabelFrame(self.master, text="运行次数设置", padx=10, pady=10)
        times_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(times_frame, text="运行次数:").pack(side="left", padx=5)
        tk.Entry(times_frame, textvariable=self.duel_times, width=10).pack(side="left", padx=5)

        # 按钮区域
        button_frame = tk.Frame(self.master)
        button_frame.pack(pady=10)

        self.start_button = tk.Button(button_frame, text="开始", command=self.run_duel, width=15, bg="#4CAF50", fg="white")
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(button_frame, text="停止", command=self.stop_duel, width=15, bg="#f44336", fg="white")
        self.stop_button.pack(side="left", padx=10)

        # 日志区域
        log_frame = tk.LabelFrame(self.master, text="日志面板", padx=10, pady=10)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, height=15)
        self.log_text.pack(fill="both", expand=True)

    def run_duel(self):
        if self.duel_thread and self.duel_thread.is_alive():
            messagebox.showinfo("警告", "功能正在运行中")
            return

        # 验证运行次数输入
        try:
            duel_times = int(self.duel_times.get())
            if duel_times <= 0:
                messagebox.showerror("错误", "运行次数必须大于0")
                return
        except ValueError:
            messagebox.showerror("错误", "运行次数必须是整数")
            return

        self.stop_flag = False
        duel_type = self.duel_type.get()

        # 获取功能名称用于显示
        func_name = ""
        for text, val in [
            ("路人决斗", "passer_duel"),
            ("传送门决斗", "portal_duel"),
            ("决斗者王国", "duelist_kingdom"),
            ("技能获取", "skill_get"),
            ("救援决斗", "rescue_duel"),
            ("波动决斗", "wave_duel"),
            ("组队决斗", "tag_duel"),
            ("奖励抽取", "reward_extract"),
        ]:
            if val == duel_type:
                func_name = text
                break

        print(f"--- {func_name} 功能启动 (共运行 {duel_times} 次) ---")

        target_func = None
        if duel_type == "passer_duel":
            target_func = self.worker_passer_duel
        elif duel_type == "portal_duel":
            target_func = self.worker_portal_duel
        elif duel_type == "duelist_kingdom":
            target_func = self.worker_duelist_kingdom
        elif duel_type == "skill_get":
            target_func = self.worker_skill_get
        elif duel_type == "rescue_duel":
            target_func = self.worker_rescue_duel
        elif duel_type == "wave_duel":
            target_func = self.worker_wave_duel
        elif duel_type == "tag_duel":
            target_func = self.worker_tag_duel
        elif duel_type == "reward_extract":
            target_func = self.worker_reward_extract

        if target_func:
            self.duel_thread = threading.Thread(target=target_func, args=(func_name, duel_times))
            self.duel_thread.daemon = True
            self.duel_thread.start()

    def worker_passer_duel(self, name, duel_times):
        passer_duel = PasserDuelV2(self.config, self.runtime_context)
        for i in range(duel_times):
            if self.stop_flag: break
            print(f"准备运行第 {i+1} 次 {name}")
            passer_duel.run()
            print(f"第 {i+1} 次 {name} 结束, 时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
            for _ in range(120): # sleep 120s but check stop_flag
                if self.stop_flag: break
                time.sleep(1)
        print(f"--- {name} 已停止 ---")

    def worker_portal_duel(self, name, duel_times):
        portal_duel = PortalDuel(self.config, self.runtime_context)
        for i in range(duel_times):
            if self.stop_flag: break
            print(f"准备运行第 {i+1} 次 {name}")
            portal_duel.duel()
            print(f"第 {i+1} 次 {name} 结束")
        print(f"--- {name} 已停止 ---")

    def worker_duelist_kingdom(self, name, duel_times):
        duelist_kingdom_duel = DuelistKingdomDuel(self.config, self.runtime_context)
        for i in range(duel_times):
            if self.stop_flag: break
            print(f"准备运行第 {i+1} 次 {name}")
            duelist_kingdom_duel.duel()
            print(f"第 {i+1} 次 {name} 结束")
        print(f"--- {name} 已停止 ---")

    def worker_skill_get(self, name, duel_times):
        for i in range(duel_times):
            if self.stop_flag: break
            print(f"准备运行第 {i+1} 次 {name}")
            SkillUtils.get_skill()
            print(f"第 {i+1} 次 {name} 结束")
        print(f"--- {name} 已停止 ---")

    def worker_rescue_duel(self, name, duel_times):
        rescue_duel = RescueDuel(self.config, self.runtime_context)
        for i in range(duel_times):
            if self.stop_flag: break
            print(f"准备运行第 {i+1} 次 {name}")
            rescue_duel.work()
            print(f"第 {i+1} 次 {name} 结束")
        print(f"--- {name} 已停止 ---")

    def worker_wave_duel(self, name, duel_times):
        wave_duel = WaveDuel(self.config, self.runtime_context)
        for i in range(duel_times):
            if self.stop_flag: break
            print(f"准备运行第 {i+1} 次 {name}")
            wave_duel.duel()
            print(f"第 {i+1} 次 {name} 结束")
        print(f"--- {name} 已停止 ---")

    def worker_tag_duel(self, name, duel_times):
        tag_duel = TagDuelTournamentDuel(self.config, self.runtime_context)
        for i in range(duel_times):
            if self.stop_flag: break
            print(f"准备运行第 {i+1} 次 {name}")
            tag_duel.duel()
            print(f"第 {i+1} 次 {name} 结束")
            time.sleep(3)
        print(f"--- {name} 已停止 ---")

    def worker_reward_extract(self, name, duel_times):
        reward_extract = RewardExtract(self.config, self.runtime_context)
        for i in range(duel_times):
            if self.stop_flag: break
            print(f"准备运行第 {i+1} 次 {name}")
            reward_extract.extractLotteryReward()
            print(f"第 {i+1} 次 {name} 结束")
            time.sleep(0.5)
        print(f"--- {name} 已停止 ---")

    def stop_duel(self):
        if self.duel_thread and self.duel_thread.is_alive():
            self.stop_flag = True
            # 不使用 join() 避免 UI 卡死，由线程自己检测 stop_flag 退出
            messagebox.showinfo("信息", "正在停止功能，请稍候...")
        else:
            messagebox.showinfo("警告", "没有进行中的功能")
