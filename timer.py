import tkinter as tk
from tkinter import ttk
import time

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("计时器 By:yuange666")

        icon_path = "./timer.ico"  # 修改为你的图标文件路径
        if icon_path:
            master.iconbitmap(icon_path)

        master.resizable(False, False)
        # 设置样式
        style = ttk.Style()
        style.configure('TButton', padding=10, font=('微软雅黑', 12), width=10)
        style.map('TButton', foreground=[('active', 'black')], background=[('active', '#d9d9d9')])

        # 计时器显示
        self.time_label = tk.Label(master, text="00:00:00.000", font=("Consolas", 48))
        self.time_label.pack(pady=20)

        # 创建一个框架来放置按钮
        button_frame = tk.Frame(master)
        button_frame.pack()

        # 开始按钮
        self.start_button = ttk.Button(button_frame, text="开始", command=self.start, style='TButton', takefocus=False)
        self.start_button.grid(row=0, column=0, padx=10)

        # 停止按钮
        self.stop_button = ttk.Button(button_frame, text="停止", command=self.stop, style='TButton', takefocus=False)
        self.stop_button.grid(row=0, column=1, padx=10)

        # 清零按钮
        self.reset_button = ttk.Button(button_frame, text="清零", command=self.reset, style='TButton', takefocus=False)
        self.reset_button.grid(row=0, column=2, padx=10)

        # 计时器变量
        self.running = False
        self.start_time = 0
        self.elapsed_time_ms = 0
        self.mode = 2  # 0: 开始, 1: 停止, 2: 清零(初始值)
        self.update_clock()

        # 初始化焦点
        self.master.focus_set()

        # 绑定快捷键
        # master.bind('<Return>', lambda event: self.start())  # 回车键开始
        # master.bind('<space>', lambda event: self.stop())  # 空格键停止
        # master.bind('<Escape>', lambda event: self.reset())  # Esc键清零

        # 绑定快捷键
        master.bind('<space>', self.toggle_mode)

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - (self.elapsed_time_ms / 1000)
            self.mode = 0

    def stop(self):
        if self.running:
            self.running = False
            self.elapsed_time_ms = int((time.time() - self.start_time) * 1000)
            self.mode = 1


    def reset(self):
        self.running = False
        self.elapsed_time_ms = 0
        self.time_label.config(text="00:00:00.000")
        self.mode = 2

    def toggle_mode(self, event=None):
        if self.mode == 0:
            self.stop()
        elif self.mode == 1:
            self.reset()
        elif self.mode == 2:
            self.start()

    def update_clock(self):
        if self.running:
            current_time = time.time()
            elapsed_time_ms = int((current_time - self.start_time) * 1000)
        else:
            elapsed_time_ms = self.elapsed_time_ms

        total_seconds = elapsed_time_ms / 1000
        milliseconds = elapsed_time_ms % 1000
        minutes, seconds = divmod(total_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        time_string = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}.{milliseconds:03d}"
        self.time_label.config(text=time_string)
        self.master.after(10, self.update_clock)  # 每10毫秒更新一次

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()


# @echo off
# D:\Python\python.exe D:/Code/PythonCode/newlearnProject/littletools/timer.py
# exit
