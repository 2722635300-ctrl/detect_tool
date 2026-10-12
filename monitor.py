import pyautogui
import pytesseract
import time
from playsound3 import playsound

# 改成你电脑 tesseract.exe 的路径
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 在这里填入游戏弹窗要检测的关键词
target_words = ["弹窗文字"]

def check_screen():
    screenshot = pyautogui.screenshot()
    text = pytesseract.image_to_string(screenshot, lang='chi_sim+eng')
    for word in target_words:
        if word in text:
            return True
    return False

if __name__ == "__main__":
    print("开始监控屏幕，等待目标弹窗...")
    while True:
        if check_screen():
            print("检测到目标弹窗！播放提醒音")
            playsound("alert.wav")
        time.sleep(1)
