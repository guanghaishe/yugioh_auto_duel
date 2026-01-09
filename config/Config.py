import configparser
import os


class Config:

    # 是否进行特殊事件决斗
    if_special_event_duel = False
    special_event_duel_return_world_idx = 1
    portal_duel_return_world_idx = 1


    def __init__(self):
        # 配置文件路径
        config_file_path = os.path.join(os.path.dirname(__file__), 'config.txt')

        # 创建配置解析器
        config = configparser.ConfigParser()

        # 读取配置文件
        config.read(config_file_path)

        # 从配置文件中获取变量的值，并赋值给类变量
        if 'Settings' in config:
            if 'if_special_event_duel' in config['Settings']:
                self.if_special_event_duel = config.getboolean('Settings', 'if_special_event_duel')
            if 'special_event_duel_return_world_idx' in config['Settings']:
                self.special_event_duel_return_world_idx = config.getint('Settings', 'special_event_duel_return_world_idx')
            if 'portal_duel_return_world_idx' in config['Settings']:
                self.portal_duel_return_world_idx = config.getint('Settings', 'portal_duel_return_world_idx')


