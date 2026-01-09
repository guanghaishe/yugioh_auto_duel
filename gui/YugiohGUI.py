import threading
import time
import tkinter as tk
from tkinter import messagebox

from config.Config import Config
from config.RuntimeContext import RuntimeContext
from duel_module.PasserDuel import PasserDuel
from duel_module.PasserDuelV2 import PasserDuelV2
from duel_module.PortalDuel import PortalDuel


class YugiohGUI:
    def __init__(self, master, config: Config, runtime_context: RuntimeContext):
        self.master = master
        self.master.title("Yugioh Bot")

        # 设置窗口大小和居中显示
        window_width = 400
        window_height = 200
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # 计算窗口的居中位置
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)
        # 格式化字符串，用来指定窗口的宽度、高度和在屏幕上的位置
        self.master.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')

        # 窗口是否允许缩放
        self.master.resizable(True, True)

        # 决斗相关变量
        self.duel_type = tk.StringVar()
        self.special_event = tk.BooleanVar()
        self.config = config
        self.runtime_context = runtime_context

        # 用于控制停止的标志
        self.stop_flag = False
        self.duel_thread = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="请选择决斗类型：").pack()

        tk.Radiobutton(self.master, text="路人决斗", variable=self.duel_type, value="passer_duel").pack()
        tk.Radiobutton(self.master, text="传送门决斗", variable=self.duel_type, value="portal_duel").pack()
        # 默认选择路人决斗
        self.duel_type.set("passer_duel")

        # 添加特殊事件决斗选项
        tk.Checkbutton(self.master, text="特殊事件决斗", variable=self.special_event).pack()

        tk.Button(self.master, text="运行", command=self.run_duel).pack()
        tk.Button(self.master, text="停止", command=self.stop_duel).pack()

    def run_duel(self):
        # 禁用运行按钮，避免重复运行
        if self.duel_thread and self.duel_thread.is_alive():
            messagebox.showinfo("警告", "决斗正在进行")
            return

        self.stop_flag = False  # 重置停止标志
        duel_type = self.duel_type.get()

        if duel_type == "passer_duel":
            self.duel_thread = threading.Thread(target=self.run_passer_duel)
        elif duel_type == "portal_duel":
            self.duel_thread = threading.Thread(target=self.run_portal_duel)
        else:
            messagebox.showwarning("错误", "请选择决斗类型")
            return

        self.duel_thread.start()

    def run_passer_duel(self):
        passer_duel = PasserDuelV2(self.config, self.runtime_context)
        cnt = 1
        while not self.stop_flag:
            print("开始第 " + str(cnt) + " 次路人决斗")
            passer_duel.run()
            cnt += 1
            time.sleep(1)
            print("第 " + str(cnt) + " 次路人决斗结束")
        print("路人决斗结束")

    def run_portal_duel(self):
        portal_duel = PortalDuel(self.config, self.runtime_context)
        cnt = 1
        while not self.stop_flag:
            print("开始第 " + str(cnt) + " 次传送门决斗")
            portal_duel.run()
            cnt += 1
            time.sleep(1)
            print("第 " + str(cnt) + " 次传送门决斗结束")
        print("传送门决斗结束")

    def stop_duel(self):
        if self.duel_thread and self.duel_thread.is_alive():
            self.stop_flag = True
            self.duel_thread.join()
            messagebox.showinfo("信息", "决斗已停止")
        else:
            messagebox.showinfo("警告", "没有进行中的决斗")
