import time
import winsound
import tkinter as tk
from tkinter import messagebox
from mss import mss
from PIL import Image
import pytesseract

# ==================== 配置区，自行修改 ====================
TARGET_TEXT = "谎言探测仪"  # 你想要识别的目标文字
AUDIO_PATH = "haoyunlai.mp3" # 提示音（和脚本放同一文件夹）
SCAN_INTERVAL = 1.0         # 屏幕扫描间隔(秒)，不要太小，防止占用过高CPU
# ==========================================================

# 隐藏tk窗口
root = tk.Tk()
root.withdraw()

# Tesseract路径，按你电脑安装位置修改
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 截图区域：全屏监控
sct = mss()
monitor = sct.monitors[1]

print(f"屏幕文字监控已启动，正在检测文字：【{TARGET_TEXT}】")
print("按 Ctrl+C 退出程序")

try:
    while True:
        # 截取屏幕
        sct_img = sct.grab(monitor)
        img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
        
        # OCR识别文字
        text = pytesseract.image_to_string(img, lang='chi_sim')
        
        if TARGET_TEXT in text:
            messagebox.showinfo("检测提醒", f"发现目标文字：{TARGET_TEXT}")
            # 播放提示音频
            winsound.PlaySound(AUDIO_PATH, winsound.SND_FILENAME)
            
        time.sleep(SCAN_INTERVAL)

except KeyboardInterrupt:
    print("\n程序已退出")
