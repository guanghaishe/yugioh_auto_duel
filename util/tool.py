import pyautogui

def getPosition():
    # 上一次的位置
    last_pos = pyautogui.position()
    try:
        while True:
            # 新位置
            new_pos = pyautogui.position()
            if last_pos != new_pos:
                print(new_pos)
                last_pos = new_pos
    except KeyboardInterrupt:
        print('\nExit.')




if __name__ == '__main__':
    getPosition()

